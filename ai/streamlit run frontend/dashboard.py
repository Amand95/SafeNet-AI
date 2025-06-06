import streamlit as st
import sqlite3
import requests
import pandas as pd

# Função para buscar dados do banco
@st.cache_data
def carregar_dados():
    conn = sqlite3.connect("sensores.db")
    df = pd.read_sql_query("SELECT * FROM leituras", conn)
    conn.close()
    return df

# Função para enviar dados para a IA
def enviar_para_ia(dado):
    url = "http://localhost:5000/analise"  # Alterado para servidor local
    try:
        resposta = requests.post(url, json=dado)
        if resposta.status_code == 200:
            return resposta.json()["resultado"]
        else:
            return "Erro na resposta da IA"
    except:
        return "Erro ao conectar com a IA"

st.title("Dashboard SafeNet-AI")

# Exibe os dados
dados = carregar_dados()
st.subheader("Histórico de Leituras")
st.dataframe(dados)
st.line_chart(dados[['temperatura', 'umidade']])

# Simula envio para IA
st.subheader("Análise com IA")
indice = st.number_input("Escolha o índice da linha para análise:", min_value=0, max_value=len(dados)-1, step=1)
dado = dados.iloc[indice][['temperatura', 'umidade', 'movimento']].to_dict()

if st.button("Analisar com IA"):
    resultado = enviar_para_ia(dado)
    st.success(f"Resultado da IA: {resultado}")
