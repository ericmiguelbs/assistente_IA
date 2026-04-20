import streamlit as st
import requests
from datetime import datetime
from collections import defaultdict

st.title("Histórico de Consultas")

@st.cache_data(ttl=60)
def get_api_data():
    try:
        response = requests.get("http://api:5000/historico", timeout=5)
        return response.json()
    except Exception as e:
        st.error(f"Erro ao conectar com a API: {e}")
        return []

dados = get_api_data()

if not dados:
    st.warning("Nenhum registro encontrado no banco de dados.")
else:
    sessoes = defaultdict(list)
    for msg in dados:
        sessoes[msg['session_id']].append(msg)
    
    for session_id, mensagens_da_sessao in reversed(sessoes.items()):
        
        primeira_msg = mensagens_da_sessao[0]
        data_obj = datetime.fromisoformat(primeira_msg['data'])
        data_formatada = data_obj.strftime("%d/%m/%Y %H:%M")
        
        titulo = "Sessão sem perguntas"
        for m in mensagens_da_sessao:
            if m['papel'] == 'user':
                titulo = m['interacao'][:50] + "..."
                break
        
        with st.expander(f"📅 {data_formatada} - {titulo}"):
            for item in mensagens_da_sessao:
                if item['papel'] == 'user':
                    st.write("**Você:**")
                    st.info(item['interacao'])
                elif item['papel'] == 'assistant':
                    st.write("**CodePilot:**")
                    st.success(item['interacao'])
                    st.divider()