import streamlit as st
import assistente

st.set_page_config(
    page_title='TecAssis',
    page_icon='',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.title("CodePilot")

st.caption("Seu copiloto de programação para resolver dúvidas e acelerar seu desenvolvimento.")

st.caption("Pergunte sobre programação ou tecnologia e receba respostas com explicações e exemplos práticos.")

#histórico de mensagens na sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

#exibe as mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])

if prompt := st.chat_input("Qual sua dúvida sobre Python?"):

    st.session_state.messages.append({"role":"user","content":prompt})

    with st.chat_message("user"):
        st.markdown(prompt)
    
    messages_for_api = st.session_state.messages

    with st.chat_message("assistant"):
        with st.spinner("Analisando sua mensagem..."):
            try:
                assistente_resposta = assistente.agente(messages_for_api)
                
                st.markdown(assistente_resposta)

                st.session_state.messages.append({"role":"assistant", "content":assistente_resposta})
            
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")




