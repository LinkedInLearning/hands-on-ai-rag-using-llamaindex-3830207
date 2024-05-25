#!/bin/bash

# Check if Conda is installed
if ! command -v conda &> /dev/null
then
    echo "Conda could not be found. Please install Conda first from the official Anaconda website: https://www.anaconda.com/products/individual"
    exit
fi

# Create a new Conda environment
echo "Creating new Conda environment named 'lil_llama_index' with Python 3.10 and python-dotenv..."
conda create --name lil_llama_index python=3.10 python-dotenv -y

# Activate the Conda environment
echo "Activating the 'lil_llama_index' environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate lil_llama_index

# Install Jupyter and JupyterLab
echo "Installing Jupyter and JupyterLab..."
conda install ipykernel jupyter jupyterlab -y

# Verify JupyterLab installation
echo "Verifying JupyterLab installation..."
jupyter lab --version

# Install LlamaIndex
echo "Installing LlamaIndex..."
pip install llama-index==0.10.37

# Install Qdrant client
echo "Installing Qdrant client..."
pip install qdrant-client==1.9.1

# Install LlamaIndex dependencies for Qdrant
echo "Installing LlamaIndex dependencies for Qdrant..."
pip install llama-index-vector-stores-qdrant==0.2.8 llama-index-readers-file==0.1.22

# Install LLM Libraries
echo "Installing LLM Libraries..."
pip install cohere==5.5.0
pip install openai==1.30.1
pip install llama-index-llms-cohere==0.2.0
pip install llama-index-llms-openai==0.1.19
pip install llama-index-embeddings-cohere==0.1.8
pip install llama-index-embeddings-openai==0.1.9
pip install llama-index-postprocessor-cohere-rerank==0.1.6

# Link IPython kernel to Conda Environment
echo "Linking IPython kernel to Conda environment..."
python -m ipykernel install --user --name=lil_llama_index --display-name "LlamaIndex (LinkedIn Learning)"

echo "Setup complete. You can now start JupyterLab with the command: jupyter lab"
