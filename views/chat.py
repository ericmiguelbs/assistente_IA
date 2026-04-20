import streamlit as st
import requests
import uuid

st.title("CodePilot")
st.caption("Seu copiloto de programação para resolver dúvidas e acelerar seu desenvolvimento.")
st.caption("Pergunte sobre programação ou tecnologia e receba respostas com explicações e exemplos práticos.")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])

if prompt := st.chat_input("Qual sua dúvida sobre Python?"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Analisando sua mensagem..."):
            try:
                payload = {
                    "session_id": st.session_state.session_id,
                    "pergunta": prompt
                }

                response = requests.post(
                    "http://api:5000/pergunta", 
                    json=payload
                )

                assistente_resposta = response.json()["resposta"]

                st.markdown(assistente_resposta)

                st.session_state.messages.append({"role": "assistant", "content": assistente_resposta})
            
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API: {e}")