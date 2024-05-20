# Choosing an LLM and Embeddings Provider

Several options are available to you for choosing an LLM and embeddings provider.

You can choose from companies that build and serve their own LLMs, like:

- [OpenAI](https://platform.openai.com/docs/models)

- [Anthropic](https://docs.anthropic.com/claude/docs/models-overview)

- [Cohere](https://docs.cohere.com/docs/the-cohere-platform)

- [Mistral](https://docs.mistral.ai/platform/pricing/)

- [Google Gemini](https://ai.google.dev/)

Or you can choose from companies that host and serve open-source models via an API, like:

- [Fireworks AI](https://fireworks.ai/models)

- [Together AI](https://www.together.ai/pricing)

- [Predibase](https://docs.predibase.com/user-guide/inference/models)

- [Hugging Face](https://huggingface.co/docs/text-generation-inference/en/supported_models)

- [Basten](https://www.baseten.co/library/)

- [Replicate](https://replicate.com/collections/language-models)

- [Lepton AI](https://www.lepton.ai/docs)

- [Clarifai](https://clarifai.com/explore/models)

With countless other providers continuously entering the market and trying to capture a share.

LlamaIndex has integrations with dozens of LLM and Embeddings providers. You can see them all [here](https://github.com/run-llama/llama_index/tree/main/llama-index-integrations/llms).

Whatever you end up choosing, the installation process will go something like this:

```bash
pip install llama-index-llms-<whatever-llm-provider-you-choose>
```

To instantiate the LLM, it will follow a pattern as shown below. Note that `LLMSProviderClass` is just a placeholder. Your chosen LLM provider will have some classes you need to import.

```python

from llama_index.llms.<whatever-llm-provider-you-choose> import  LLMSProviderClass

llm = LLMSProviderClass(api_key = your_api_key, model="whatever-model-you-want-to-use")

```

## We'll primarily use the Cohere API in this course.

For the simple reason that it's free! Well, it's free to prototype with, anyway. And you don't need to enter any payment information. You just need to sign up with GitHub, Google, or your e-mail and you're good to go.

Also, their [`Command-R` and `Command-R-Plus`](https://txt.cohere.com/command-r/) model performs well for RAG tasks.

#### For RAG evaluation we'll make use of OpenAI

It's just faster and easier to do, that's all. 
---

# But in the "real world," choosing the right large language model (LLM) and embeddings provider for your project requires careful consideration of several factors. 

Here are just a few points to help guide your decision:

## 🎯 Identify your business objectives and use cases

* Understand your business's present and future objectives and ensure your chosen LLM can fulfill those needs.

* Determine the LLM's specific use case, such as content generation, sentiment analysis, customer support, or fraud detection.

## 🔍 Evaluate popular LLMs and their capabilities

* Each model has unique strengths and weaknesses.

* Familiarize yourself with as many LLMs as you possibly can. Test them for accuracy, relevance and quality of generated text. Even the best LLMs may sometimes provide inaccurate information, so aim to find one that does so less frequently.

* Understand each model's strengths and weaknesses, such as advanced coding, complex reasoning, commonsense reasoning, or efficiency in building AI assistants.

* Consider the input size the LLM can handle. Larger context windows allow more input and context to be passed to the model.

## 🪪 License

* Different providers may have varying restrictions on how their models can be used. 

* Some licenses may limit the use of the LLM or embeddings to non-commercial applications, require attribution, or restrict the types of applications for which the model can be used. 

* Make sure you inspect the license and ensure that your project complies with the terms.

## 🌐 Consider language support and multilingual capabilities

* If your project requires support for multiple languages, ensure the LLM and embedding provider you choose can handle the languages you need.

* Evaluate the quality of the model's output in each language and its ability to understand and generate text in a culturally appropriate manner.

## 🔒 Evaluate security and privacy compliance

* Assess the security measures in place to protect your data and the privacy of your users.

* Look for features like data encryption, secure data handling, and compliance with relevant privacy regulations (e.g., GDPR, HIPAA).

## 💰⚡ Assess cost and performance

* Understand the cost structure of each LLM, including any usage-based pricing.

* Evaluate the performance of different models in terms of accuracy, speed, and response times.

## 🔮🛠️ Ensure long-term relevance and support

* Investigate the LLM provider's future plans and how regularly the model receives updates.

* Consider the vendor's reputation, the LLM's ability to seamlessly integrate with your existing infrastructure, and its ability to scale to address your business's growing demands.

## 🧑‍🤝‍🧑 Assess community support and resources

* Look for an active community of developers and users around the LLM and embedding provider you're considering.

* A strong community can provide valuable resources, such as tutorials, forums, and open-source projects, which can help you get started and troubleshoot issues more quickly.