# Choosing a Vector Database

Without a doubt, vector databases are an essential part of any RAG system. And, as the image below shows...there are a lot to choose from.

So, how should you go about choosing a vector database for Retrieval-Augmented Generation (RAG) applications?

<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/0*iAX7Y3NfVOtn0dOr.png">
[Image Source](https://blog.det.life/why-you-shouldnt-invest-in-vector-databases-c0cd3f59d23c)

Well, there are several key factors to consider...

## 🚀 Similarity search performance
 
RAG relies heavily on efficient similarity search to retrieve relevant documents or passages. The vector database should provide fast and accurate similarity search capabilities, such as cosine similarity or Euclidean distance, to quickly retrieve relevant information.

## 📊 Scalability

As the amount of data grows, the vector database should be able to scale horizontally and handle large-scale indexing and querying. It should efficiently store and manage high-dimensional vectors and support distributed search across multiple nodes if necessary.

## 🔗 Integration with LLM frameworks

The vector database should integrate well with popular LLM orchestration frameworks like LlamaInde, LangChain, or Instructor. This integration allows seamless interaction between the RAG model and the vector database, enabling efficient retrieval and generation.

## 🌐 Support for various data types

RAG applications may deal with different data types, such as text, images, or audio. The vector database should support storing and indexing vectors derived from various data types, allowing flexibility in the data types that can be retrieved.

## 🛠️ Indexing and updating capabilities

The vector database should provide efficient indexing mechanisms to quickly build and update the index as new data is added or modified. It should handle incremental updates and support real-time indexing if required by the application.

## 🔍 Retrieval flexibility

The vector database should offer flexibility in retrieval options, such as specifying the number of nearest neighbors to retrieve, setting similarity thresholds, or applying filters based on metadata. This flexibility allows fine-tuning the retrieval process based on the specific requirements of the RAG application.

## 💾 Data persistence and reliability

The vector database should ensure data persistence and provide data backup and recovery mechanisms. It should be reliable and able to handle potential failures or data loss scenarios.

## 🫂 Community support and documentation

Consider the level of community support and documentation available for the vector database. An active community and comprehensive documentation can greatly assist in troubleshooting, optimizing performance, and staying updated with the latest features and best practices.

## 🎮 Ease of use and deployment

The vector database should be easy to set up, configure, and deploy. It should provide clear APIs or client libraries for integration with the RAG application and have straightforward deployment options, whether on-premises or in the cloud.

## 💰 Cost and licensing

Consider the vector database's cost and licensing model. Consider pricing, scalability costs, and any limitations or restrictions imposed by the licensing terms.

# We're using Qdrant in this course

For all the reasons mentioned above.

Not only that, but...

- 🦙 Qdrant is [one of the most popular vector databases based on downloads on LlamaHub](https://llamahub.ai/?tab=vector_stores).

- 📖 Their documentation is a breath of fresh air – clear, to the point, and without any fluff. It makes getting up and running a breeze if you want to go deeper than the LlamaIndex abstractions.

- 🌍 The development is open, and the team behind Qdrant is technically savvy. It's reassuring to see the level of transparency and expertise.

- 🔐 They've recently added built-in authentication to the dev version. It's a game changer if you're looking for that extra layer of security.

- 🆓 They offer an extremely generous free tier via their hosted cloud, making it easy to test drive Qdrant and see if it fits your needs without any commitment.

- 🤖 OpenAI is rumoured to use Qdrant as an embedding vector database, according to a [Reddit post](https://www.reddit.com/r/ChatGPT/comments/17plmqj/openai_is_using_qdrant_as_a_vector_database/).

- 🤖 X AI also uses Qdrant, as [evidenced by the fork in their GitHub](https://github.com/xai-org).