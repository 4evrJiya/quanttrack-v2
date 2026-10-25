"""
QuantTrack — Multi-Stock Portfolio Comparison Page
"""

import streamlit as st

from config import MAX_PORTFOLIO_STOCKS
from strategies import STRATEGY_REGISTRY
from portfolio import run_portfolio_backtest, build_portfolio_returns, compare_portfolio_vs_best_single
from history import save_portfolio_result

st.set_page_config(page_title="Portfolio - QuantTrack", page_icon=":material/account_balance_wallet:", layout="wide")

from ui_helpers import apply_custom_css, render_sidebar_status
apply_custom_css()
render_sidebar_status()

st.markdown('<div class="qt-eyebrow">Portfolio analysis</div>', unsafe_allow_html=True)
st.title("Portfolio comparison")
st.caption(f"Compare an equally weighted portfolio of up to {MAX_PORTFOLIO_STOCKS} stocks with the strongest individual performer in the tested set.")

tickers_input = st.text_input(
    f"Enter up to {MAX_PORTFOLIO_STOCKS} tickers, comma-separated",
    "RELIANCE.NS,TCS.NS,INFY.NS,HDFCBANK.NS,ITC.NS"
)
portfolio_strategy_choice = st.selectbox("Strategy applied to each stock", list(STRATEGY_REGISTRY.keys()))
portfolio_button = st.button("Run portfolio backtest", type="primary", use_container_width=True)

if portfolio_button:
    tickers = [t.strip() for t in tickers_input.split(",") if t.strip()]
    strat_func = STRATEGY_REGISTRY[portfolio_strategy_choice]

    with st.spinner("Running backtest across all stocks..."):
        portfolio_results = run_portfolio_backtest(tickers, strat_func)
        portfolio_df = build_portfolio_returns(portfolio_results)

    if portfolio_df is None:
        st.session_state["portfolio_display"] = None
        st.error("Couldn't fetch valid data for any of the entered tickers. Check the symbols.")
    else:
        comparison = compare_portfolio_vs_best_single(portfolio_results, portfolio_df)
        st.session_state["portfolio_display"] = {
            "tickers": tickers,
            "strategy": portfolio_strategy_choice,
            "portfolio_df": portfolio_df,
            "comparison": comparison
        }

if "portfolio_display" in st.session_state and st.session_state["portfolio_display"] is not None:
    d = st.session_state["portfolio_display"]

    st.subheader("Portfolio equity curve")
    st.line_chart(d["portfolio_df"]["Portfolio_Equity"])

    st.subheader("Portfolio vs. best single stock")
    st.table(d["comparison"])

    st.info("Diversification can produce a lower return than the best individual stock, but it may also reduce the size of drawdowns. Compare both return and risk before drawing conclusions.")

    if "logged_in_user" in st.session_state:
        if st.button("Save portfolio to history", type="primary"):
            portfolio_metrics = d["comparison"]["Portfolio (5 stocks)"].to_dict()
            save_portfolio_result(st.session_state["logged_in_user"], d["tickers"], d["strategy"], portfolio_metrics)
            st.success("Saved to your history! View it on the Account page.")
    else:
        st.caption("Sign in from Account to save this result to your history.")

elif "portfolio_display" not in st.session_state:
    st.info(f"Enter up to {MAX_PORTFOLIO_STOCKS} tickers above and run the portfolio backtest. Results will appear here.")