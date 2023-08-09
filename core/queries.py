import openai
import streamlit as st
from core.info import options


class Chatbot:
    def __int__(self):
        st.session_state.messages = [
            {"role": "system",
             "content": f"you are an excellent chatbot-navigator for a financing company that identifies which segment from this list {options} the user is looking for. You job is to identify which leaf node the user is looking for. \n"
                        f"So for example the chosen segments can be one of the following: ['Automobile', 'consumer_finance', 'credit_limit'], but cannot be one of the following: ['Retail services','Auto & Trucks','Corporate & Medical centers']. \n"
                        f"once you identify which segment the user want, write: '::stop::' followed by the segment name, This will navigate the user to the correct page with all information needed. \n"
                        f"You don't need to elaborate about what each loan does you just needs to guide the user to identify which segment he's looking for to navigate him to the right spot."},
        ]

    def reset(self):
        st.session_state.messages = [
            {"role": "system",
             "content": f"you are an excellent chatbot-navigator for a financing company that identifies which segment from this list {options} the user is looking for. You job is to identify which leaf node the user is looking for. \n"
                        f"So for example the chosen segments can be one of the following: ['Automobile', 'consumer_finance', 'credit_limit'], but cannot be one of the following: ['Retail services','Auto & Trucks','Corporate & Medical centers']. \n"
                        f"once you identify which segment the user want, write: '::stop::' followed by the segment name, This will navigate the user to the correct page with all information needed. \n"
                        f"You don't need to elaborate about what each loan does you just needs to guide the user to identify which segment he's looking for to navigate him to the right spot."},
        ]

    def query(self, question):
        st.session_state.messages.append({"role": "user", "content": question})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        answer = ""
        for choice in response.choices:
            answer += choice.message.content

        if "::stop::" in answer:
            self.reset()
            return "Stop"

        st.session_state.messages.append({"role": "assistant", "content": answer})
        return answer
