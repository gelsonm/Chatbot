# Local-LLM-ChatBot
## Personal Assistant with Streamlit and Ollama LLM

This project implements a personal assistant using Streamlit, LangChain, and a locally downloaded Llama 3.2 model via Ollama. The assistant is designed to engage in interactive conversations, where user input is processed, and responses are generated by the language model. This assistant supports a continuous chat history, providing a conversational experience.

## Features
- Chat interface powered by Streamlit.
- Integration with LangChain for prompt handling and response generation.
- Use of a locally downloaded Llama 3.2 model through Ollama.
- Session-based message history to maintain context across interactions.

## Installation

### Prerequisites

- Python 3.7+
- Streamlit
- LangChain
- Ollama

You will need to install the following dependencies:

```bash
pip install streamlit langchain langchain_ollama
