"""
QuantTrack — Price Forecast Page
"""

import streamlit as st

from data_ingestion import fetch_stock_data
from forecasting import generate_forecast
from history import save_forecast_result

st.set_page_config(page_title="Forecast - QuantTrack", page_icon=":material/ssid_chart:", layout="wide")

from ui_helpers import apply_custom_css, render_sidebar_status
apply_custom_css()
render_sidebar_status()

st.markdown('<div class="qt-eyebrow">Forecast exploration</div>', unsafe_allow_html=True)
st.title("30-day price forecast")
st.caption("Explore a model-based projection from historical patterns. This is an estimate, not a reliable prediction of future market prices.")

forecast_ticker = st.text_input("Enter ticker for forecast", "RELIANCE.NS")
forecast_button = st.button("Generate forecast", type="primary", use_container_width=True)

if forecast_button:
    forecast_data = fetch_stock_data(forecast_ticker)

    if forecast_data is None:
        st.session_state["forecast_display"] = None
        st.error(f"No data found for ticker '{forecast_ticker}'. Check the symbol.")
    else:
        with st.spinner("Generating forecast..."):
            forecast_result = generate_forecast(forecast_data)

        if forecast_result is None:
            st.session_state["forecast_display"] = None
            st.warning("Not enough historical data to generate a reliable forecast for this stock.")
        else:
            forecast_chart_data = forecast_result[["ds", "yhat", "yhat_lower", "yhat_upper"]].set_index("ds").tail(30)
            st.session_state["forecast_display"] = {
                "ticker": forecast_ticker,
                "chart_data": forecast_chart_data
            }

if "forecast_display" in st.session_state and st.session_state["forecast_display"] is not None:
    d = st.session_state["forecast_display"]

    st.subheader("Projected price path")
    st.line_chart(d["chart_data"])

    st.caption("The lower and upper bounds show the model's estimated uncertainty range. They are not guarantees; markets can move in response to events the model cannot anticipate.")

    st.subheader("Recent forecast values")
    st.dataframe(d["chart_data"].tail(10), use_container_width=True)

    if "logged_in_user" in st.session_state:
        if st.button("Save forecast to history", type="primary"):
            final_predicted_price = d["chart_data"]["yhat"].iloc[-1]
            save_forecast_result(st.session_state["logged_in_user"], d["ticker"], final_predicted_price)
            st.success("Saved to your history! View it on the Account page.")
    else:
        st.caption("Sign in from Account to save this forecast to your history.")

elif "forecast_display" not in st.session_state:
    st.info("Enter a ticker and generate a forecast to explore the projected price path and model uncertainty.")