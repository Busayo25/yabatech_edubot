import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="YabatechEdubot", page_icon="🤖")

st.title("YabatechEdubot 🤖")
st.markdown("Ask me anything about Yabatech!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", "")

if user_input:
    response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")