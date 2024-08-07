import datetime
import humanize
import streamlit as st
from currency import currency
from currency_convert import convert_currency, get_exchange_rate

def main():
    """
    Main function to run the currency converter Streamlit app.
    """
    st.title(' :dollar: Currency converter')
    st.markdown(""" Efficient currency converter program that allows users to convert between
                different currencies using up-to-date exchange rates.
                """)
    
    base_currency = st.selectbox("From currency", currency)
    target_currency = st.selectbox("To currency", currency, index=1)
    amount = st.number_input('Enter amount', min_value=0.00, value=1.00)
    
    exchange_rate, last_time_update = get_exchange_rate(base_currency, target_currency)
    convert_amount = convert_currency(amount, exchange_rate)
    
    display_exchange_rate_info(exchange_rate, last_time_update)
    display_conversion_result(amount, base_currency, convert_amount, target_currency)

def display_exchange_rate_info(exchange_rate, last_time_update):
    """
    Display the exchange rate and when it was last updated.
    
    Args:
    exchange_rate (float): The current exchange rate
    last_time_update (float): Unix timestamp of the last update
    """
    time_diff = datetime.datetime.now() - datetime.datetime.fromtimestamp(last_time_update)
    time_ago = humanize.naturaltime(time_diff)
    st.success(f"✅ Exchange Rate: {exchange_rate:.4f} (Last updated: {time_ago})")

def display_conversion_result(amount, base_currency, convert_amount, target_currency):
    """
    Display the conversion result using Streamlit columns.
    
    Args:
    amount (float): The amount to be converted
    base_currency (str): The base currency code
    convert_amount (float): The converted amount
    target_currency (str): The target currency code
    """
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Base Currency", value=f"{amount} {base_currency}")
    col2.markdown("<h1 style='text-align: center; margin: 0;'>&#8594;</h1>", unsafe_allow_html=True)
    col3.metric(label="Target Currency", value=f"{convert_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()