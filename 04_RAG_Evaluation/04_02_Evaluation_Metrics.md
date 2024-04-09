# 📐 Evaluation Metrics

A robust RAG evaluation requires carefully measuring the retriever and generator performance.

It is essential to use the right metrics and construct datasets that match how the system will be used in the real world. A close look at each component is the key to determining where RAG systems need to improve.

**🤝 Faithfulness:** This looks at how factually accurate the answer is based on the context the retriever found. We want to ensure the LLM isn't hallucinating (making up plausible-sounding text that is inaccurate).

**🔍 Answer Relevancy:** This measures how relevant the answer is to the user query, according to the retrieved context, and if it covers what the question asks for.

**🪡Context Precision:** Evaluates whether all ground-truth relevant items present in the contexts are appropriately ranked.

**✅ Answer Correctness:** This measures how accurate the generated answer is compared to the ground truth.

**📊 Context Recall:** This is the number of relevant context chunks the retriever manages to retrieve compared to the total number of relevant chunks.

Before computing evaluation metrics, you need to make sure:

📂 The evaluation datasets cover many question types, complexities, and domains, helping assess the RAG system's performance across different scenarios and use cases.

🌍 Datasets that closely resemble real-world queries and information needs. This provides a more accurate assessment of how the RAG system would perform in practical applications.

# 👨🏽‍⚖️ LLM-as-a-Judge 

LLM-as-a-Judge is a technique that uses an LLM to automatically evaluate the outputs of other LLMs in a way that aims to approximate human judgment.

The key idea is to leverage strong LLMs to assess generated text that usually requires human evaluation, such as the abovementioned metrics. Using LLMs as judges is a scalable and cost-effective way to evaluate RAG systems. It enables faster benchmarking and iteration cycles during AI development.

However, LLM judges have some limitations and biases that need to be carefully addressed, such as:

- Position bias: Favoring certain positions in a text

- Verbosity bias: Preferring longer outputs

- Limited reasoning capabilities for complex topics like math

Despite these challenges, studies have shown that with proper prompt engineering and debiasing techniques, strong LLM judges like GPT-4 can achieve high agreement (>80%) with human preferences and expert ratings across different benchmarks. LLM-as-a-Judge is a promising complement to human evaluation for assessing open-ended AI tasks at scale.

# ragas

We'll use the [`ragas`](https://github.com/explodinggradients/ragas) as our RAG evaluation framework. To compute RAG evaluation metrics in `ragas`, you need to build an evaluation dataset with the following features:

❓ `question`: This is the user's query that goes into the RAG pipeline. 

🤖 `answer`: The LLM generates this as a response to the question. It's the final output you want to evaluate.

📚 `contexts`: The retrieved context the retriever pulls from external sources to help answer the question. 

✅ `ground_truths`: This is the "correct answer" to the question, provided by human annotators or generated via a powerful LLM. It's the gold standard answer to which you'll compare any iteration of your RAG system's answer. This is only needed to measure the `context_recall` metric.

In the following lessons, I'll explain each of these metrics in more detail, including how to calculate them. Then, we'll build an evaluation dataset.