import random
import time
from datasets import Dataset
from tqdm import tqdm
from collections import defaultdict
from IPython.display import Markdown, display
from qdrant_client import QdrantClient, AsyncQdrantClient
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core.settings import Settings
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding

from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.llms.cohere import Cohere
from llama_index.llms.openai import OpenAI
from llama_index.llms.mistralai import MistralAI

from llama_index.vector_stores.qdrant import QdrantVectorStore

def setup_llm(provider, model, api_key, **kwargs):
    """
    Configures the LLM (Language Learning Model) settings.

    Parameters:
    - api_key (str): The API key for authenticating with the LLM service.
    - model (str): The model identifier for the LLM service.
    """
        
    if provider == "cohere":
        Settings.llm = Cohere(model=model, api_key=api_key, **kwargs)
    elif provider == "openai":
        Settings.llm = OpenAI(model=model, api_key=api_key, **kwargs)
    elif provider == "mistral":
        Settings.llm = MistralAI(model=model, api_key=api_key, **kwargs)
    else:
        raise ValueError(f"Invalid provider: {provider}. Pick one of 'cohere', 'openai', or 'mistral'.")

def setup_embed_model(provider, **kwargs):
    """
    Configures the embedding model settings.

    Parameters:
    - model_name (str): The model identifier for the embedding service.
    """
    if provider == "cohere":
        Settings.embed_model = CohereEmbedding(model_name="embed-english-v3.0", **kwargs)
    elif provider == "openai":
        Settings.embed_model = OpenAIEmbedding(model_name="text-embedding-3-large", **kwargs)
    elif provider == "fastembed":
        Settings.embed_model = FastEmbedEmbedding(model_name="BAAI/bge-base-en-v1.5", **kwargs)
    else:
        raise ValueError(f"Invalid provider: {provider}. Pick one of 'cohere', 'fastembed', or 'openai'.")

def setup_vector_store(qdrant_url, qdrant_api_key, collection_name, enable_hybrid=False):
    """
    Creates and returns a QdrantVectorStore instance configured with the specified parameters.

    Parameters:
    - qdrant_url (str): The URL for the Qdrant service.
    - qdrant_api_key (str): The API key for authenticating with the Qdrant service.
    - collection_name (str): The name of the collection to be used in the vector store.

    Returns:
    - QdrantVectorStore: An instance of QdrantVectorStore configured with the specified Qdrant client
    """
    client = QdrantClient(location=qdrant_url, api_key=qdrant_api_key)
    aclient = AsyncQdrantClient(location=qdrant_url, api_key=qdrant_api_key)
    vector_store = QdrantVectorStore(client=client, aclient=aclient, collection_name=collection_name, enable_hybrid=enable_hybrid)
    return vector_store

def get_documents_from_docstore(persist_dir):
    """
    Retrieves the Document objects out of a specified document store.

    Parameters:
    - persist_dir: The document store from which to retrieve the documents.

    Returns:
    - list: A list of Documents from the document store.
    """
    docstore = SimpleDocumentStore.from_persist_dir(persist_dir=persist_dir)
    documents = list(docstore.docs.values())
    return documents

def create_index(from_where, embed_model=Settings.embed_model, **kwargs):
    """
    Creates and returns a VectorStoreIndex instance configured with the specified parameters.

    Parameters:
    **kwargs: Additional keyword arguments for configuring the index, such as:
        - embed_model: The embedding model to be used in the index.
        - vector_store: The vector store to be used in the index.
        - nodes: The nodes to be used in the index.
        - storage_context: The storage context to be used in the index.

    Returns:
    - VectorStoreIndex: An instance of VectorStoreIndex configured with the specified Qdrant client and vector store.
    """
    if from_where=="vector_store":
        index = VectorStoreIndex.from_vector_store(embed_model=embed_model, **kwargs)
        return index
    elif from_where=="docs":
        index = VectorStoreIndex.from_documents(embed_model=embed_model, **kwargs)
        return index
    else:
        raise ValueError(f"Invalid option: {from_where}. Pick one of 'vector_store', or 'docs'.")

def ingest(transformations, documents, **kwargs):
    """
    Createsan IngestionPipeline and ingests the documents.

    Parameters:
    - transformations (list): A list of transformations to apply in the pipeline.
    - documents (list): A list of Document objects to be ingested.
    - **kwargs: Additional keyword arguments for configuring the pipeline, such as:
        - docstore: An instance of a document store.
        - vector_store: An instance of a vector store.
        - cache: An instance of an ingestion cache.

    Returns:
    
    """
    
    pipeline = IngestionPipeline(
        transformations=transformations,
        **kwargs
    )
    
    return pipeline.run(nodes=documents)

def create_query_pipeline(chain, verbose=True):
    """
    Creates and returns a QueryPipeline instance configured with the specified chain of components.

    Parameters:
    - chain (list): A list of components to be used in the pipeline. Each component in the list should be an instance of a module that can be used in a QueryPipeline (e.g., LLMs, query engines).
    - verbose (bool): If True, enables verbose output for the pipeline.

    Returns:
    - QueryPipeline: An instance of QueryPipeline configured with the specified chain of components.
    """
    pipeline = QueryPipeline(
        chain=chain,
        verbose=verbose
    )

    return pipeline

def create_query_engine(index, mode, **kwargs):
    """
    Creates and returns a query engine from the given index with the specified configurations.

    Parameters:
    - index: The index object from which to create the query engine. This should be an instance of VectorStoreIndex or similar, which has the as_query_engine method.
    - mode (str): The mode of the query engine to create. Possible values are "chat", "query", and "retrieve".
    - **kwargs: Additional keyword arguments for configuring the query engine, such as similarity_top_k and return_sources.

    Returns:
    - A query engine configured with the specified parameters.
    """
    if mode =="chat":
        return index.as_chat_engine(**kwargs)

    elif mode == "query":
        return index.as_query_engine(**kwargs)

    elif mode == "retrieve":
        return index.as_retriever(**kwargs)
    else:
        raise ValueError(f"Invalid mode: {mode}. Pick one of 'chat', 'query', or 'retrieve'.")

def display_prompt_dict(prompts_dict):
    """
    Display the prompts in the given prompts dictionary more compactly.

    Parameters:
    prompts_dict (dict): A dictionary containing the prompts, where the keys are the prompt keys and the values are the prompt templates.
    Returns:
    None
    """
    markdown_output = " "
    for k, p in prompts_dict.items():
        markdown_output += f"""**Prompt Key**: {k}\n**Text:**\n```\n{p.get_template()}\n```\n\n"""
    display(Markdown(markdown_output))

def group_documents_by_author(documents):
    """
    Group documents by author.

    This function organizes a list of document objects into a dictionary where each key is an author's name,
    and the value is a list of all documents authored by that person. It leverages defaultdict to automatically
    handle any authors not previously encountered without raising a KeyError.

    Args:
        documents (list): A list of document objects, each having a 'metadata' dictionary that includes an 'author' key.

    Returns:
        defaultdict: A dictionary where keys are author names and values are lists of documents for those authors.
    """
    # Initialize a defaultdict to store lists of documents, organized by author.
    documents_by_author = defaultdict(list)

    # Loop over each document in the provided list.
    for doc in documents:
        # Retrieve the 'author' from the document's metadata. Default to None if 'author' key is missing.
        author = doc.metadata.get('author', None)

        # Check if the author exists. If so, append the document to the corresponding list in the dictionary.
        if author:
            documents_by_author[author].append(doc)
        else:
            # If no author is specified, print a warning. These documents will not be added to any author group.
            print("Warning: A document without an author was encountered and skipped.")

    # Return the populated defaultdict containing grouped documents.
    return documents_by_author

def sample_documents(documents_by_author, num_samples=10):
    """
    Randomly sample a specific number of documents for each author from a grouped dictionary.
    Only documents with more than 500 characters are considered for sampling.

    This function takes a dictionary where each key is an author's name and the value is a list of document
    objects authored by that person. It attempts to sample a specified number of documents for each author.
    If an author does not have enough documents to meet the sample size, it prints a warning.

    Args:
        documents_by_author (dict): A dictionary where keys are authors' names and values are lists of documents.
        num_samples (int): The desired number of documents to sample from each author's list.

    Returns:
        list: A list containing the randomly sampled documents across all authors, up to the specified number
              per author, where possible.
    """
    # Initialize an empty list to store the sampled documents.
    sampled_documents = []

    # Iterate over each author and their corresponding documents in the dictionary.
    for author, docs in documents_by_author.items():
        # Filter documents with more than 500 characters.
        valid_docs = [doc for doc in docs if len(doc.get_content()) > 500]

        # Check if the current author has enough documents to meet the requested sample size.
        if len(valid_docs) >= num_samples:
            # If yes, randomly sample the documents and extend the sampled_documents list with the results.
            sampled_documents.extend(random.sample(valid_docs, num_samples))
        else:
            # If no, print a warning message indicating the author and the deficiency in document count.
            print(f"Author {author} does not have enough valid documents to sample {num_samples}.")

    # Return the list of all sampled documents.
    return sampled_documents

def run_generations_on_eval_set(eval_dataset, col_name, query_pipeline, time_out=True):
    """
    Processes an evaluation dataset to add a new column with answers generated by a query pipeline.
    
    This function iterates over each item in a provided dataset, uses a query pipeline to generate an answer
    for each question, and then appends these answers as a new column in the dataset. If `time_out` is True,
    the function pauses for 25 seconds after every 5 queries to comply with API rate limits. Progress is visually
    tracked using a tqdm progress bar.
    
    Parameters:
        eval_dataset (Dataset): A Hugging Face `Dataset` object containing at least a 'question' field.
        col_name (str): The name of the new column to add to the dataset with the generated answers.
        query_pipeline: The query pipeline object used to generate answers.
        time_out (bool): If True, pauses execution to respect API rate limits. Default is True.
        
    Returns:
        Dataset: The original dataset augmented with a new column containing the generated answers.
    
    Example:
        from datasets import load_dataset
        query_pipeline = setup_query_pipeline(api_key="your_api_key")
        eval_dataset = load_dataset('squad', split='validation').select(range(100))  # Example dataset
        updated_dataset = run_generations_on_eval_set(eval_dataset, 'generated_answers', query_pipeline)
        print(updated_dataset)
    """
    responses = []

    # Use tqdm to create a progress bar over the dataset iteration
    for i, row in tqdm(enumerate(eval_dataset), total=len(eval_dataset), desc="Generating answers"):
        response = query_pipeline.run(row['question'])
        responses.append(response.response)
        
        # Pause after every 5 queries to respect the API rate limit, if time_out is True
        if time_out and (i + 1) % 5 == 0:
            time.sleep(25)
    
    # Add the responses as a new column to the dataset
    eval_dataset = eval_dataset.add_column(col_name, responses)
    return eval_dataset