# Importar bibliotecas necessárias
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta
from io import BytesIO
import json

# Função para carregar os dados
@st.cache_data
def carregar_dados(empresas):
    tickers = " ".join(empresas)
    dados_acao = yf.Tickers(tickers)
    cotacoes_acao = dados_acao.history(period="1d", start="2010-01-01", end="2024-08-15")
    cotacoes_acao = cotacoes_acao['Close']
    return cotacoes_acao

# Função para gerar arquivo Excel
def gerar_excel(df):
    output = BytesIO()
    df.index = df.index.tz_localize(None)  # Remover fuso horário
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer)
    return output.getvalue()

# Função para gerar arquivo PDF
def gerar_pdf(df):
    output = BytesIO()
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    pdf = canvas.Canvas(output, pagesize=letter)
    pdf.setTitle("Dados de Ações")
    pdf.drawString(100, 750, "Dados de Ações Filtrados")
    
    data = df.reset_index().values.tolist()
    y_offset = 700
    for row in data:
        pdf.drawString(100, y_offset, str(row))
        y_offset -= 20
        if y_offset < 100:
            pdf.showPage()
            y_offset = 750
    pdf.save()
    return output.getvalue()

# Função para gerar arquivo JSON
def gerar_json(df):
    output = BytesIO()
    df_json = df.reset_index().to_json(orient='records', date_format='iso')
    output.write(df_json.encode('utf-8'))
    return output.getvalue()

# Lista de ações
acoes = ["ITUB4.SA", "PETR4.SA", "VALE3.SA", "MGLU3.SA", "ABEV3.SA"]
dados = carregar_dados(acoes)

# Interface do Streamlit
st.write("""
    # Preço de Ações
    O gráfico representa a evolução do preço das ações ao longo dos anos.
""")

# Filtros
st.sidebar.header("Filtros")
lista_acoes = st.sidebar.multiselect("Escolha as Ações para visualizar", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: "Close"})

# Filtro de datas
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_datas = st.sidebar.slider("Selecione as datas", min_value=data_inicial, max_value=data_final, value=(data_inicial, data_final), step=timedelta(days=15))

dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]

# Gráfico
st.line_chart(dados)

# Botão para baixar em Excel
excel_bytes = gerar_excel(dados)
st.sidebar.download_button(
    label="Baixar dados em Excel",
    data=excel_bytes,
    file_name="dados_acoes.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# Botão para baixar em PDF
pdf_bytes = gerar_pdf(dados)
st.sidebar.download_button(
    label="Baixar dados em PDF",
    data=pdf_bytes,
    file_name="dados_acoes.pdf",
    mime="application/pdf"
)

# Botão para baixar em JSON
json_bytes = gerar_json(dados)
st.sidebar.download_button(
    label="Baixar dados em JSON",
    data=json_bytes,
    file_name="dados_acoes.json",
    mime="application/json"
)
