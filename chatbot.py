from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Streamlit page setup
st.set_page_config(
    page_title="Generative ChatBot AI",
    page_icon="🤖",
    layout="centered"
)

st.title("Generative ChatBot AI Application")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.1
)

# Input box
user_prompt = st.chat_input("Ask ChatBot...")

if user_prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Add user message to history
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_prompt
    })

    # Invoke LLM
    response = llm.invoke(
        [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.content

    # Add assistant response to history
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": assistant_response
    })

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
