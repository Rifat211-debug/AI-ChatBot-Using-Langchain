import streamlit as st
from chatbot import get_response
from langchain_core.messages import HumanMessage, AIMessage

st.header("AI Chatbot Using Langchain")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


for msg in st.session_state.chat_history:
    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):
        st.write(msg.content)


#print chat history
with st.sidebar:
    st.subheader("Chat History")
    if not st.session_state.chat_history:
        st.write("(empty)")
    else:
        for msg in st.session_state.chat_history:
            role = "AI" if isinstance(msg, AIMessage) else "Human"
            st.write(f"==> {role} : ==> {msg.content}")   

user_input = st.chat_input("Type Your Message")

if user_input:

    if user_input.strip().lower() == "exit":
        st.stop()

    st.session_state.chat_history.append(
        HumanMessage(content = user_input)
    )    
    with st.chat_message("user"):
        st.write(user_input)


    response, followup_questions = get_response(user_input)


    ai_response = f"""
=> Answer :
{response.answer}

=> Summary :
{response.summary}

=> Category :
{response.category}

=> Confidence :
{response.confidence:.2f}

=> Keywords :
{response.keywords}
"""

    if followup_questions:
        ai_response += "\n  ## Follow-up Questions : \n"
        for question in followup_questions:
            ai_response += f"-{question}\n"

    
    st.session_state.chat_history.append(
        AIMessage(content = ai_response)
    )
    with st.chat_message("assistant"):
        st.markdown(ai_response)


     




                      