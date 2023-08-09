import openai
import streamlit as st
from PIL import Image

# init
from core.queries import query, reset
from core.sidebar import sidebar

st.set_page_config(page_title="ontact Chatbot Demo", page_icon="📖", layout="wide")

# image
image = Image.open('src/logo.png')
st.image(image)
# Title
st.header("Contact Chatbot Demo")

# sidebar
sidebar()
# open AI

openai_api_key = st.session_state.get("OPENAI_API_KEY")
if not openai_api_key:
    st.warning(
        "please enter a password to access the app!"
    )
    st.stop()
openai.api_key = openai_api_key

if not st.session_state.get("messages"):
    reset()
# create message log
if not st.session_state.get("chat_logs"):
    st.session_state["chat_logs"] = []
# chat
question = st.text_input("Chat:")
if question:
    st.session_state.chat_logs.append({"role": "user", "content": question})
    # query
    answer = query(question)
    st.session_state.chat_logs.append({"role": "assistant", "content": answer})

# display old chat
for msg in reversed(st.session_state.chat_logs):
    st.chat_message(msg["role"]).write(msg["content"])
