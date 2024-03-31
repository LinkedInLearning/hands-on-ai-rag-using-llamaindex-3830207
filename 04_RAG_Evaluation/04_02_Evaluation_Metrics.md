# 📐 Evaluation Metrics

A robust RAG evaluation requires carefully measuring the retriever and generator performance.

It's important to use the right metrics and construct datasets that match up with how the system will be used in the real world. Taking a close look at each component is the key to figuring out where RAG systems need to improve.

**🤝 Faithfulness:** This looks at how factually accurate the answer is, based on the context the retriever found. We want to make sure the LLM isn't just making things up!

**🔍 Answer Relevancy:** This measures how relevant the answer is to the user query, according to the retrieved context, and if it covers what the question is asking for.

**🪡Context Precision:** Evaluates whether all of the ground-truth relevant items present in the contexts are appropriately ranked.

**✅ Answer Correctness**:  This measures how accurate the generated answer is compared to the ground truth.

**📊 Context Recall:** This is the amount of relevant context chunks the retriever manages to retrieve, compared to the total amount of relevant chunks.

**🎯 Context Relevance:** This checks how closely the context the retriever finds matches up with the question being asked.


Before computing evaluation metrics you need to make sure:

📂 That the evaluation datasets cover a wide range of question types, complexities, and domains. This helps assess the RAG system's performance across different scenarios and use cases.

🌍 Datasets that closely resemble real-world queries and information needs. This provides a more accurate assessment of how the RAG system would perform in practical applications.

# ragas

We'll make use of the [`ragas`](https://github.com/explodinggradients/ragas) as our RAG evaluation framework - which will help us build evaluation datasets and perform our evaluation. In order to compute RAG evaluation metrics in `ragas`, you need to build an evaluation dataset with the following features:

❓ `question`: This is the user's query that goes into the RAG pipeline. 

🤖 `answer`: This is what the LLM generates as a response to the question. It's the final output you want to evaluate.

📚 `contexts`: These are the retrieved context the retriever pulls from external sources to help it answer the question. 

✅ `ground_truths`: This is the "correct answer" to the question, provided by human annotators, or a generated via a powerful LLM. It's the gold standard answer you'll compare any iteration of your RAG system's answer to. This is only needed for measuring the `context_recall` metric.

In the proceeding lessons I'll explain each of these metrics in more detail, including how to calculate them. Then, we'll build an evaluation dataset.