# Setting up your environment!

We'll be using `Conda` as our package manager. If you have a preference for `venv` or `poetry`, feel free to use those.

Conda is a package manager that helps manage different software environments. If you're following along on Codespaces, then it's already installed for you! If you're following along locally and you haven't already installed `Conda` then head over official [Anaconda website](https://www.anaconda.com/products/individual) for instructions on how to to download and install Conda.

# Create a new Conda environment

Open your terminal or command prompt and run the following command to create a new Conda environment named `lil_llama_index`, and install Python 3.10.

```
conda create --name lil_llama_index python==3.10 python-dotenv
```

### Activate the Conda environment

Once the environment is created, activate it using the following command:

```
conda activate lil_llama_index
```

### Install Jupyter and JupyterLab

Jupyter is a popular interactive computing platform, and JupyterLab is its next-generation user interface. You can install both using the following command:

```
conda install ipykernel jupyter jupyterlab
```

##### Verify the installation

This will open JupyterLab in your default web browser, allowing you to create and run Jupyter notebooks.

```
jupyter lab
```

# Installing 🗂️ LlamaIndex 🦙

LlamaIndex is nicely seperated into numerous smaller packages. 

For now, let's just install the starter package to get started. As we progress along the course I will add additional libraries as `pip install ...` in the first cell of every notebook.


```
pip install llama-index==0.10.22
```

LlamaIndex is a new library, and changes fast. It's important that you pin your version to the one above so you don't run into any code errors as you follow along with me throughout the course.

# Install Qdrant

We'll make use of Qdrant as our vector database through this course. Let's install the dependencies for that.

```
pip install qdrant-client==1.8.0
```

Again, it's important to pin the version to the one above so we're on the same page while coding.

### Installing LlamaIndex dependencies for Qdrant

LlamaIndex has it's dependencies nicely seperated out. Let's install what we need for Qdrant:

```
pip install llama-index-vector-stores-qdrant llama-index-readers-file
```

# Install LLM Libraries

We'll make use of Cohere, Mistral, and OpenAI throughout the course.

```
pip install cohere openai mistralai 
pip insall fastembed
pip install llama-index-llms-openai llama-index-llms-mistralai llama-index-llms-cohere 
pip install llama-index-embeddings-cohere llama-index-embeddings-openai llama-index-embeddings-mistralai llama-index-embeddings-fastembed
pip install llama-index-postprocessor-cohere-rerank
```

# Link IPython kernel to Conda Enviornment

```
python -m ipykernel install --user --name=lil_llama_index --display-name "LlamaIndex (LinkedIn Learning)"
```