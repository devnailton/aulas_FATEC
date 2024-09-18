# importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf


# criar as funções de carregamento de dados
	# Cotações do Itau - ITUB4 2010 a 2024
@st.cache_data #Decorator dá uma nova funcionalidade à essa função, salvar as informações em cache
def carregar_dados (empresa):
	dados_acao = yf.Ticker(empresa)
	cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end="2024-08-15")
	#cotacoes_acao[['Close']]
	cotacoes_acao = cotacoes_acao[['Close']]
	return cotacoes_acao


dados = carregar_dados("AGRO3.SA")
print(dados)
# prepara as visualizações


#criar a interface do streamlit
st.write("""
	# Preço de Ações
	O gráfico representa a evolução do preço das ações do Itaú (ITUB4) ao longo dos anos
""") # markdown

#Criar o Gráfico
st.line_chart(dados)

st.write("""
	## Nailton Silva
""")
