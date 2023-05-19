import numpy as np
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import streamlit as st
import datetime
from empresas_import import *


st.write("""
# Mercado Financeiro IBOVESPA

Pontuacao e Precos IBOVESPA de Acoes e Fudnso

""")

#Criacao  Grafico IBOVESPA 2010/2023
ibovespa = '^BVSP'

tickerData = yf.Ticker(ibovespa)

tickerDf = tickerData.history(period='1d', start='2010-1-01', end=None)

st.line_chart(tickerDf.Close)

#Grafico Empresas

st.write("""
# Grafico Empresas  
""")
d_empresa = st.date_input(
    "Data a ser analizado a acao:",
    datetime.date(2020, 1, 1))

opcao_empresa = st.selectbox(
    'Lista Empresas:',
    (empresas_pd))

tickerData_empresa = yf.Ticker(f'{opcao_empresa}.SA')

tickerDf_empresa = tickerData_empresa.history(period='1d', start=f'{d_empresa}', end=None)

st.line_chart(tickerDf_empresa.Close)

df_empresas = pd.DataFrame(tickerData_empresa.dividends)
df_empresas.columns = ['Dividendos']

st.table(df_empresas)

st.write("""
# Grafico Fundos  
""")
d_fundos = st.date_input(
    "Data a ser analizado do Fundo:",
    datetime.date(2020, 1, 1))

opcao_fundo = st.selectbox(
    'Lista Empresas:',
    (fundos_pd))

tickerData_fundo = yf.Ticker(f'{opcao_fundo}.SA')

tickerDf_fundo = tickerData.history(period='1d', start=f'{d_fundos}', end=None)

st.line_chart(tickerDf_fundo.Close)

df_fundo = pd.DataFrame(tickerData_fundo.dividends)
df_fundo.columns = ['Dividendos']

st.table(df_empresas)





