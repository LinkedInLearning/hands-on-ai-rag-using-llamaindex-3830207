# Introduction to RAG Evaluation

📏 Evaluation gives you concrete numbers that tell you how accurate the system is, how relevant its answers are, and how well it's working overall.

🔍 With an evaluation system in place you can compare different models, prompts, and context to figure out what works best.

📈 Regular evaluation will help you assess the quality of your RAG pipeline over time.

Without checking in on how the RAG system is doing, it's tough to know what needs fixing and how to make it better.

## Recall the basic steps in creating a RAG system

 - Create an Index

 - Retrieval relevant context from our Index that are similar to our query

 - Generate responses based on the retrieved context by injecting the retrieved context into a prompt and sending that to an LLM

<img src="../image_assets/rag_system_diagram.png">
Diagram illustrating the components of a RAG system, including the retriever and generator processes. 

Source: [AI Makerspace](https://youtu.be/Anr1br0lLz8)

Take a moment to pause and think about what the two primary components of this system are.

## Evaluating Different RAG Components

A RAG pipeline has two main parts: retrieval and generation.

### **🔍 Retrieval component**

This feteches external context from the vector database.

If the retriever makes mistakes, those mistakes will carry over to the generator. The retrieved sources must be relevant to the user's query.

So, You need a way to measure how closely the retrieved context matches what the user is asking about.

### **🤖 Generation component**

This combines a prompt template, the user's question, and the context it retrieved to generate an answer using an LLM. 

You want the generated response to be grounded in the retrieved context, relevant to the user's query, and adhere to any guidelines you have in place.

You need a way to measure the relevance of responses to the retrieved context as well as the coherence and fluency of the generated responses.

We need to check how well these components work on their own and 
together.

# Aspects of Evaluation

When looking at retrieval and generation, there are two main things to measure: quality and generation.

### 📊 Measuring Quality

Quality is measured via relevance and faithfulness.

 **🎯 Relevance** 
 
 Relevance should be measured for the retrieved context and the generated response.
 
 The retrieved context should be *precise and specific*. The more relvant each bit of retrieved context is, the better generation will be.

 The generated answers should be directly relevant with the user's query.

 **🤝 Faithfulness** 
 
 This makes sure the answers the system generates *are faithful to the context it retrieved*. The generated response shouldn't have any contradictions or inconsistencies.

### 🏹 Measuring Ability

**🔇 Noise Robustness:** This checks how well the model handles noisy context. That is, context that are related to the question but don't have useful info.

**🙅‍♂️ Negative Rejection:** This looks at how well the model knows when to say, "I don't know." If the retrieved context doesn't have the info needed to answer the question, it should not try to answer.

**🧩 Information Integration:** This tests how good the model is at putting together context from multiple documents. This is important for handling complex questions that need context from different sources.

**🔮 Counterfactual Robustness:** This checks if the model can spot and ignore things in retrieved context that it knows are wrong, even if it's told there might be some misinformation info in them.

When evaluating **retrieval quality**, context relevance and noise robustness are important, while for evaluating **generation quality**, answer faithfulness, answer relevance, negative rejection, information integration, and counterfactual robustness should be considered.

