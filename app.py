import yfinance as yf
import streamlit as st 
import pandas as pd
from datetime import date

st.set_page_config(page_title='StockLite', layout='wide', initial_sidebar_state='expanded')
st.title('StockLite - Multi- Stock Real- Time Dashboard')
ticker = st.text_input('Enter Stock Ticker', 'AAPL')

st.sidebar.header("⚙️ Select Options")

# Multi-stock dropdown
stock_options = ['AAPL', 'TSLA', 'GOOGL', 'INFY', 'RELIANCE.NS', 'HDFCBANK.NS', 'MSFT', 'AMZN']
selected_stocks = st.sidebar.multiselect("Choose stocks to compare:", stock_options, default=['AAPL', 'TSLA'])

# Date range selector
start_date = st.sidebar.date_input("Start Date", value=date(2023, 1, 1))
end_date = st.sidebar.date_input("End Date", value=date.today())

# Theme toggle (Light / Dark)
theme = st.sidebar.radio("Choose Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #0e1117;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    
if selected_stocks:
    for ticker in selected_stocks:
        st.subheader(f"📌 {ticker} Stock Data")
        data = yf.download(ticker, start=start_date, end=end_date)
        
        if data.empty:
            st.warning(f"No data found for {ticker} in the selected range.")
            continue

        # Line chart of closing prices
        st.line_chart(data['Close'], use_container_width=True)

        # Show table with statistics
        st.markdown("**Summary Statistics**")
        st.dataframe(data.describe(), use_container_width=True)

else:
    st.info("Please select at least one stock to view data.")

st.markdown("---")
st.markdown("📌 *Built by Aswathy using Streamlit & yfinance.*")