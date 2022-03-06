import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import plotly.express as px
import plotly.graph_objects as go
import datetime

def viz(ticker_sym : str,date):
    ticker = yf.download(ticker_sym,start=date,interval="1d")
    df = ticker.copy()
    df = df[['Close']]
    print(df)
    #df.reset_index(level=0, inplace=True)
    #df.columns=['ds','y']
    st.line_chart(df)
    #plt.plot(df.ds, df.y)
    #plt.show()
    #plt.figure(figsize=(10,10))
    rolling_mean = df.Close.rolling(window=200).mean()
    rolling_mean2 = df.Close.rolling(window=50).mean()
    df["200 DMA"] = rolling_mean
    df["50 DMA"] = rolling_mean2
    st.line_chart(df)
df = pd.read_csv("nifty500.csv")
ticker  = st.selectbox(df["Company Name"])
ticker_sym = df.loc[ticker == df["Company Name"],"Symbol"]
date_str = st.date_input("select date")
formatted_date = datetime.datetime.strptime(str(date_str), "%Y-%m-%d").strftime("%Y-%m-%d")
#interval_str = st.text_input("Valid intervals",placeholder="1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo")
form = st.form(key='my_form')
submit_button = form.form_submit_button(label='Submit')
if submit_button:
    st.markdown(formatted_date)
    viz(ticker_sym,formatted_date)
