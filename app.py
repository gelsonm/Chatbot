import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from config import CHAT_PROMPT_TEMPLATE

# Title on the page
st.markdown(
    "<h2 style='text-align: center; color: #4CAF50; font-family: Arial;'>🤖 Personal Assistant</h2>",
    unsafe_allow_html=True,
)
template = CHAT_PROMPT_TEMPLATE

prompt = ChatPromptTemplate.from_template(template)

# We load our own local llama3.2 downloaded using Ollama 
model = OllamaLLM(model="llama3.2")

chain = prompt | model

# We initialize the message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# We will display the chat messages from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Taking user input
if prompt := st.chat_input("What is up?"):
    # Adding user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Invoking our chain and genarating our assistant's response
    with st.chat_message("assistant"):
        response = chain.invoke({"question": f"{prompt}"})  
        st.markdown(response)

    # Adding the assistant message to session state
    st.session_state.messages.append({"role": "assistant", "content": response})