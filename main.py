import openai
import streamlit as st
from PIL import Image

# init
from core.queries import Chatbot
from core.sidebar import sidebar

st.set_page_config(page_title="Synapse Email Parser", page_icon="📖", layout="wide")

# image
image = Image.open('src/logo.png')
st.image(image)
# Title
st.header("Synapse Email Parser")

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

# create class
chat_bot = st.session_state.get("CHATBOT")
if not chat_bot:
    chat_bot = Chatbot()
    st.session_state["CHATBOT"] = chat_bot
# create message log
if not st.session_state.get("messages"):
    st.session_state["messages"] = []
# chat
question = st.text_input("Chat:")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    # query
    answer = chat_bot.query(question)
    st.session_state.messages.append({"role": "assistant", "content": answer})
# display old chat
for msg in reversed(st.session_state.messages):
    st.chat_message(msg["role"]).write(msg["content"])
