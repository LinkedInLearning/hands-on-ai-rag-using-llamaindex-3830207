from IPython.display import Markdown, display
from qdrant_client import QdrantClient
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core.settings import Settings
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.llms.cohere import Cohere
from llama_index.vector_stores.qdrant import QdrantVectorStore

def setup_llm(api_key, model="command-r"):
    """
    Configures the LLM (Language Learning Model) settings.

    Parameters:
    - api_key (str): The API key for authenticating with the LLM service.
    - model (str): The model identifier for the LLM service.
    """
    Settings.llm = Cohere(model=model, api_key=api_key)

def setup_embed_model(model_name="BAAI/bge-large-en-v1.5-quantized"):
    """
    Configures the embedding model settings.

    Parameters:
    - model_name (str): The model identifier for the embedding service.
    """
    Settings.embed_model = FastEmbedEmbedding(model_name=model_name)

def setup_vector_store(qdrant_url, qdrant_api_key, collection_name):
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
    vector_store = QdrantVectorStore(client=client, collection_name=collection_name)
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

def create_index(**kwargs):
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

    index = VectorStoreIndex.from_vector_store(embed_model=Settings.embed_model, **kwargs)
    return index

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

    pipeline.run(documents)

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

    if mode == "query":
        return index.as_query_engine(**kwargs)

    if mode == "retrieve":
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