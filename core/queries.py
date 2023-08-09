import openai
import streamlit as st
from core.info import options, get_key, outputs


def reset():
    st.session_state.messages = [
        {"role": "system",
         "content": f"you are an excellent chatbot-navigator for a financing company that identifies which segment from this list {options} the user is looking for. You job is to identify which leaf node the user is looking for. \n"
                    f"So for example the chosen segments can be one of the following: ['Automobile', 'consumer_finance', 'credit_limit'], but cannot be one of the following: ['Retail services','Auto & Trucks','Corporate & Medical centers', 'Credit limit' ]. \n"
                    f"once you identify which segment the user want, write: '::stop::' followed by the segment name, This will navigate the user to the correct page with all information needed. \n"
                    f"You don't need to elaborate about what each loan does you just needs to guide the user to identify which segment he's looking for to navigate him to the right spot. \n"
                    f"An example output will be '::stop:: Automobile' if the user was looking for a car loan. \n"
                    f"You will in no way give answers that aren't given in the options."},
    ]


def subquery(key, question):
    message = [
        {"role": "system", "content": f"Report this data: {outputs[key]}"}]
    message.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    answer = ""
    for choice in response.choices:
        answer += choice.message.content
    return answer


def query(question):
    st.session_state.messages.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state.messages
    )
    answer = ""
    for choice in response.choices:
        answer += choice.message.content

    if "::stop::" in answer:
        reset()
        key = get_key(answer)
        if key:
            return subquery(key, question)
        return answer

    st.session_state.messages.append({"role": "assistant", "content": answer})
    return answer
