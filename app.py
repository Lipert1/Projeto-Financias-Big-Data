import numpy as np
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import streamlit as st
import datetime



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
d = st.date_input(
    "Data a ser analizado a acao:",
    datetime.date(2020, 1, 1))

opcao = st.selectbox(
    'Lista Empresas:',
    ('VALE3', 'PETR4', 'ITUB3'))

tickerData = yf.Ticker(f'{opcao}.SA')

tickerDf = tickerData.history(period='1d', start=f'{d}', end=None)

st.line_chart(tickerDf.Close)

df_empresas = pd.DataFrame(tickerData.dividends)
df_empresas.columns = ['Dividendos']

st.table(df_empresas)






