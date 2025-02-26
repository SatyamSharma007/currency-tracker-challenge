
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Title
st.title("💹 Currency Value Tracker")

# Currency Selection
currencies = ["USD", "EUR", "INR", "GBP", "JPY", "AUD", "CAD", "CNY"]
base_currency = st.selectbox("Select Base Currency:", currencies, index=currencies.index("USD"))
target_currency = st.selectbox("Select Target Currency:", currencies, index=currencies.index("INR"))

# Yahoo Finance ticker format for currency pairs (e.g., "USDINR=X")
ticker = f"{base_currency}{target_currency}=X"

# Fetch real-time exchange rate
if st.button("Get Exchange Rate"):
    try:
        currency_data = yf.Ticker(ticker)
        exchange_rate = currency_data.history(period="1d")["Close"].iloc[-1]
        st.success(f"1 {base_currency} = {exchange_rate:.4f} {target_currency}")
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# Fetch historical data (Last 30 Days)
if st.button("Show Last 30 Days Trend"):
    try:
        history = yf.download(ticker, period="1mo", interval="1d")

        if history.empty:
            st.error("No data available for the selected currency pair.")
        else:
            # Plot historical trend
            fig, ax = plt.subplots()
            ax.plot(history.index, history["Close"], marker="o", linestyle="-", color="b")
            ax.set_title(f"{base_currency} to {target_currency} (Last 30 Days)")
            ax.set_xlabel("Date")
            ax.set_ylabel("Exchange Rate")
            ax.grid(True)

            st.pyplot(fig)
    except Exception as e:
        st.error(f"Error fetching historical data: {e}")

