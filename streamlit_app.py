import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import datetime

def viz(ticker_sym : str,date,interval):
    ticker = yf.download(ticker_sym,start=date,interval=interval)
    st.markdown("Volume Traded")
    st.bar_chart(ticker["Volume"])
    df = ticker.copy()
    df = df[['Close']]
    st.markdown(f"Position Chart - interval : {interval}")
    st.line_chart(df)
    rolling_mean = df.Close.rolling(window=200).mean()
    rolling_mean2 = df.Close.rolling(window=50).mean()
    df["200 DMA"] = rolling_mean
    df["50 DMA"] = rolling_mean2
    st.markdown("Moving Average Chart")
    st.line_chart(df)
choice = st.selectbox("Select Stocks/Crypto",("stocks","crypto"))
if choice == "stocks":
    df = pd.read_csv("nifty500.csv")
    ticker  = st.selectbox("select company name",df["Company Name"])
    ticker_sym = df.loc[ticker == df["Company Name"],"Symbol"].item()+".ns"
else:
    ticker_sym = st.text_input("Enter Crypto Ticker",placeholder = "Example : btc-inr , Eth-inr")
st.markdown(str(ticker_sym))
date_str = st.date_input("select date")
formatted_date = datetime.datetime.strptime(str(date_str), "%Y-%m-%d").strftime("%Y-%m-%d")
interval_str = st.selectbox("Valid intervals",("1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo").split(","))
form = st.form(key='my_form')
submit_button = form.form_submit_button(label='Submit')
if submit_button:
    st.markdown(formatted_date)
    viz(ticker_sym,formatted_date,interval_str)
