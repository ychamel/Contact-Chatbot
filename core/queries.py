import openai
import streamlit as st
from core.info import options, get_key, outputs, for_more_info, get_state, get_question, States


def reset():
    """
    resets the memory of the chat
    :return:
    """
    st.session_state.messages = [
        {"role": "system",
         "content": f"You are an excellent chatbot-navigator for a company called 'Contact'. You do not disclose that you're a LLM and your goal is to chat with customers and identify which leaf segment from this list {options} they are looking for. \n"
                    f"So for example the chosen segments can be one of the following: ['Automobile', 'consumer_finance', 'credit_limit'], but cannot be one of the following: ['Retail services','Auto & Trucks','Corporate & Medical centers', 'Credit limit' ]. \n"
                    f"Once you've identified which segment the customer looking for, write: '::stop::' followed by the segment name, This will navigate the user to the correct page which contains all information he needs. \n"
                    f"Try not to give answers outside of this sheet such as life advice or general information, stay focus on the task of simply finding out which category the customer is looking for. \n"
                    f"An example output once you identifies the segment, will be '::stop:: segment_name'. \n"
         },
    ]


def subquery(key, question):
    """
    based on the information stored in the info file and the key extracted the answer is extracted and humanifyed using chatgpt
    :param key:
    :param question:
    :return: answer:
    """
    message = [
        {"role": "system", "content": f"Report this data: {outputs[key]} \n {for_more_info} \n"}]
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
    """
    receives the last user request and return an answer based on the previous information
    :param question:
    :return: answer:
    """
    # state = st.session_state.get("state")
    # if state == States.product:
    #     print("product query")
    #     return product_query(question)
    return main_query(question)


def main_query(question):
    st.session_state.messages.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state.messages
    )
    answer = ""
    for choice in response.choices:
        answer += choice.message.content

    # case navigation found
    if "::stop::" in answer:
        key = get_key(answer)
        if key:
            # change state
            state = change_state(key)
            return subquery(key, question) + f"\n {get_question(state)}"
        return answer
    if "::submit::" in answer:
        change_state("")
        return f"We successfully received your request \n {answer.split('::submit::')[1]}\n " \
               f"Our customer service representative will contact you shortly. \n" \
               f"{for_more_info} \n" \
               f"Can I help you with anything else?"
    if "::cancel::" in answer:
        change_state("")
        return "Request Cancelled! \n How can I help you?"
    st.session_state.messages.append({"role": "assistant", "content": answer})
    return answer


def product_query(question):
    """
    This section handles queries related to a product
    :param question:
    :return:
    """
    st.session_state.product_messages.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state.product_messages
    )
    answer = ""
    for choice in response.choices:
        answer += choice.message.content

    # case navigation found
    if "::submit::" in answer:
        change_state("")
        return f"We successfully received your request \n {answer.split('::submit::')[1]}\n " \
               f"Our customer service representative will contact you shortly. \n" \
               f"{for_more_info} \n" \
               f"Can I help you with anything else?"
    if "::cancel::" in answer:
        change_state("")
        return "Request Cancelled! \n How can I help you?"
    st.session_state.product_messages.append({"role": "assistant", "content": answer})
    return answer


def change_state(key):
    """
    changes the state of the application and resets the session of the application
    :param state:
    :return:
    """
    state = get_state(key)
    if st.session_state.state == state:
        return state
    st.session_state.state = state
    st.session_state.key = key
    if state == States.product:
        st.session_state.messages = [
            {"role": "system",
             "content": f"You are a chatbot for a company named contact that is responsible at identifying if the user is interested in a product and wants to buy it. \n"
                        "if the user is interested in buying the product get his name and email and return them in this format '::submit:: {'name':'','email':'' }' \n"
                        "However if the user doesn't seem interested return '::cancel::' \n"
                        f"The context is as follows: {outputs[key]} \n"
                        f"the last question was {get_question(state)}"
             },
        ]
    elif state == States.know_more:
        st.session_state.messages = [
            {"role": "system",
             "content": f"You are a chatbot for a company named contact. You are responsible at identifying if the user wants to know more information about the product or not. \n"
                        "if the user is interested in knowing more, get his name and email and return them in this format '::submit:: {'name':'','email':'' }' \n"
                        "However if the user doesn't seem interested return '::cancel::' \n"
                        f"The context is as follows: {outputs[key]} \n"
                        f"the last question was {get_question(state)}"
             },
        ]
    elif state == States.main:
        reset()
    return state
