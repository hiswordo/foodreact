
# @link [Build 12 Data Science Apps with Python and Streamlit - Full Course - YouTube](https://www.youtube.com/watch?v=JwSS70SZdyM) at 2021/9/8
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!\n
Enter "GOOGL"、"AAPL"、"TSM"、"2330.TW"...
""")
stockname = st.text_input('Enter some text','GOOGL')

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = stockname
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1m', start='2019-5-31', end='2020-5-31')
# tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)