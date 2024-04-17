# Components of a RAG System

Now, let's get into the nitty-gritty of what goes into a RAG system.

At a high-level you can abstract a RAG system into a high-level three-step process: You retrieve context from external data sources, add it to your prompt, and send that to the LLM for generation.

## Let's explore the process more deeply by describing what we need for the system to work.

<img src="https://qdrant.tech/articles_data/what-is-rag-in-ai/how-rag-works.jpg">

**Source: [Qdrant blog](https://qdrant.tech/articles/what-is-rag-in-ai/)**

| Component | Purpose |
|-----------|---------|
| 🧠 LLM | This is the system's brain, which is responsible for taking the augmented prompt and generating text from it. |
| 📩 Prompt | Every interaction starts with a user's query or statement. The Prompt captures this initial input, setting the stage for the retrieval and generation processes. |
| 📂 Document Loader | The Document Loader imports and reads documents, preparing them for chunking and embedding. |
| ✂️ Document Chunker | A document chunker breaks documents into smaller, more digestible pieces to make the data more manageable and efficient for retrieval. |
| 🎛️ Embedding Model | Before storing or retrieving data, we need to convert textual information into a format the system can understand. The Embedder takes on this role, transforming text into vector representations. |
| 🗄️ Vector Store | This storage system houses embeddings from their corresponding textual data. |
| 🔍 Vector Store Retriever | The Vector Store Retriever fetches relevant documents from the vector store by comparing vector similarities, ensuring that the most pertinent information is always available. |
| 🙋 User Input | Last but not least, the User Input tool captures the query or statement provided by the end user, initiating the entire RAG process. |


# The RAG System and Its Subsystems

Now that you know all the components you need for a RAG system, let's build them into subsystems. Each component fits within one of the following subsystems:

1) Index

2) Retrieval

3) Augment

These work together as an orchestrated flow, transforming a user's query into a contextually rich and accurate response.

## Index System

<img src="https://qdrant.tech/articles_data/what-is-rag-in-ai/how-indexing-works.jpg">

**Source: [Qdrant blog](https://qdrant.tech/articles/what-is-rag-in-ai/)**

This subsystem prepares and organizes the data for efficient retrieval. Here are the steps of the Index system

1) Load Documents (Document loader): This process imports and reads the data the system will use.

2) Chunk Documents (Document chunker): This step breaks down the loaded documents into smaller, more manageable chunks for more efficient retrieval.

3) Embed Documents (embedding model): The text chunks are converted into vector representations, making them searchable within the system.

4) Store Embeddings (Vector Store): Stores the vector embeddings for future retrieval.

## Retrieval System

<img src="https://qdrant.tech/articles_data/what-is-rag-in-ai/how-retrieval-works.jpg">

**Source: [Qdrant blog](https://qdrant.tech/articles/what-is-rag-in-ai/)**

This subsystem fetches the most relevant information based on the user's query. Here are the steps in the Retrieval system

1) Obtain User Query (User Input): Captures the user's question or statement.

2) Embed User Query (Embedding model): Transforms the user's query into a vector format, similar to the indexed documents.

3) Vector Search (Vector Store Retriever): Search the Vector Store for documents with embeddings that closely match the embedded user query.

4) Return Relevant Documents: The system returns the top matches, ensuring that the most pertinent information is always provided.

## Augment System

<img src="https://qdrant.tech/articles_data/what-is-rag-in-ai/rag-system.jpg">

**Source: [Qdrant blog](https://qdrant.tech/articles/what-is-rag-in-ai/)**

This subsystem enhances the LLM's input prompt with the retrieved context, ensuring the model has all the necessary information to generate a comprehensive response.

1) Create Initial Prompt (Prompt): Starts with the original user query or statement.

2) Augment Prompt with Retrieved Context: Merges the initial prompt with the context retrieved from the Vector Store, creating an enriched input for the LLM.

3) Send Augmented Prompt to LLM: The enhanced prompt is fed to the LLM.

4) Receive LLM's Response: After processing the augmented prompt, it generates and returns its response.

These subsystems make up the whole RAG system, which will produce more accurate, credible, and contextually relevant outputs.