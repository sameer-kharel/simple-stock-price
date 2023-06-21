import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock  **closing price** and **volume** of Google!

""")


#define ing the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-5-31')

st.write("""
         ## closing price
         """)
st.line_chart(tickerDf.Close)

st.write(""" 
          ## volume price 
          """)
st.line_chart(tickerDf.Volume)