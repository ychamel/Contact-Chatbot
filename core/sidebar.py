import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your password below🔑\n"  # noqa: E501
            "2. Talk with the Chatbot to navigate the available options\n"
        )

        password = st.text_input(
            "Access Password",
            type="password",
            placeholder="enter the password to access this app",
            help="you can send us an email at https://www.synapse-analytics.io/contact to get access",  # noqa: E501
            value=None
            or st.session_state.get("password", ""),
        )

        api_key_input = None
        if password == os.environ.get("password"):
            api_key_input = os.environ.get("OPENAI_API_KEY", None)

        st.session_state["OPENAI_API_KEY"] = api_key_input


