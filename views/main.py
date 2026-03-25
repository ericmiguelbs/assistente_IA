import streamlit as st

st.set_page_config(
    page_title='CodePilot',
    page_icon='🤖',
    layout='wide'
)

pag_chat = st.Page("chat.py", title="Chat Copilot", icon=":material/chat:", default=True)
pag_historico = st.Page("view_historico.py", title="Acessar histórico", icon=":material/history:")

pg = st.navigation([pag_chat, pag_historico])

pg.run()