# importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf


# criar as funções de carregamento de dados
	# Cotações do Itau - ITUB4 2010 a 2024
@st.cache_data #Decorator dá uma nova funcionalidade à essa função, salvar as informações em cache
def carregar_dados (empresas):
	tickers = " ".join(empresas)
	dados_acao = yf.Tickers(tickers)
	cotacoes_acao = dados_acao.history(period="1d", start="2022-01-01", end="2024-08-15")
	print(cotacoes_acao)
	cotacoes_acao = cotacoes_acao['Close']
	return cotacoes_acao


acoes = ["SLCE3.SA", "AGRO3.SA", "CAML3.SA", "JBSS3.SA", "MGLU3.SA", "RAIZ4.SA", "AMER3.SA"]
dados = carregar_dados(acoes)

#criar a interface do streamlit
st.write("""
	# Preço de Ações
	O gráfico representa a evolução do preço das ações do Itaú (ITUB4) ao longo dos anos
""") # markdown
# prepara as visualizações - Agora são Filtros
lista_acoes = st.multiselect("Escolha as Ações para visualizar", dados.columns)
if lista_acoes:
	dados = dados[lista_acoes]
	if len(lista_acoes) == 1:
		acao_unica = lista_acoes[0]
		dados = dados.rename(columns={acao_unica: "Close"})

#Criar o Gráfico
st.line_chart(dados)

st.write("""
	## Nailton Silva
""")