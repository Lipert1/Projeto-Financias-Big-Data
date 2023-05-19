import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import seaborn as sns
import yfinance as yfin

yfin.pdr_override()

empresas = pd.read_excel("Empresas.xlsx")
fundos = pd.read_excel("Fundos.xlsx")

fundos_pd = pd.DataFrame(fundos)
empresas_pd = pd.DataFrame(empresas)