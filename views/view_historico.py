import streamlit as st
import requests
from datetime import datetime

st.title("Histórico de Consultas")

@st.cache_data(ttl=60)
def get_api_data():
    try:
        response = requests.get("http://127.0.0.1:5000/historico", timeout=5)
        return response.json()
    except:
        return []

dados = get_api_data()

if not dados:
    st.warning("Nenhum registro encontrado no banco de dados.")
else:
    for item in reversed(dados):
        data_obj = datetime.fromisoformat(item['data'])
        data_formatada = data_obj.strftime("%d/%m/%Y %H:%M")
        
        with st.expander(f"📅 {data_formatada} - {item['pergunta'][:50]}..."):
            st.write("**Pergunta:**")
            st.info(item['pergunta'])
            
            st.write("**Resposta do CodePilot:**")
            st.success(item['resposta'])