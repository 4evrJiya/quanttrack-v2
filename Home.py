
"""QuantTrack — Home Page."""

import streamlit as st

st.set_page_config(
    page_title="QuantTrack | Quantitative Research",
    page_icon="📈",
    layout="wide",
)

from ui_helpers import apply_custom_css, render_sidebar_status

apply_custom_css()
render_sidebar_status()

# -------------------- HERO --------------------

st.html(
    """
    <section class="qt-hero">
        <div class="qt-eyebrow">Quantitative Research Workspace</div>

        <h1>
            Research your strategy.<br>
            <span class="qt-hero-accent">Understand your risk.</span>
        </h1>

        <p>
            Explore historical market data, test rule-based strategies,
            compare portfolio performance, and investigate price forecasts
            in one focused research workspace.
        </p>

        <div class="qt-pills">
            <span class="qt-pill">Historical backtesting</span>
            <span class="qt-pill">Risk &amp; performance</span>
            <span class="qt-pill">Portfolio analysis</span>
            <span class="qt-pill">Forecast exploration</span>
        </div>
    </section>
    """
)

# -------------------- WORKSPACE --------------------

st.markdown(
    '<div class="qt-section-label">YOUR WORKSPACE</div>',
    unsafe_allow_html=True,
)
st.markdown("## Explore QuantTrack")

st.caption(
    "Choose a workflow to begin. Results are historical simulations "
    "or model estimates, not guarantees of future performance."
)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.html(
        """
        <div class="qt-workflow-card">
            <div class="qt-card-top">
                <span class="qt-card-number">01</span>
                <span class="qt-card-category">STRATEGY RESEARCH</span>
            </div>
            <h3>Backtest a strategy</h3>
            <p>
                Test a trading strategy against historical stock prices.
                Compare its performance with a buy-and-hold benchmark.
            </p>
            <div class="qt-card-footer">Historical performance · Risk metrics</div>
        </div>
        """
    )
    st.page_link(
        "pages/2_Backtest.py",
        label="Open Backtesting →",
        use_container_width=True,
    )

with col2:
    st.html(
        """
        <div class="qt-workflow-card">
            <div class="qt-card-top">
                <span class="qt-card-number">02</span>
                <span class="qt-card-category">PORTFOLIO ANALYSIS</span>
            </div>
            <h3>Compare a portfolio</h3>
            <p>
                Explore an equal-weighted portfolio and compare its
                historical behaviour with individual stock holdings.
            </p>
            <div class="qt-card-footer">Diversification · Portfolio returns</div>
        </div>
        """
    )
    st.page_link(
        "pages/3_Portfolio.py",
        label="Open Portfolio Analysis →",
        use_container_width=True,
    )

with col3:
    st.html(
        """
        <div class="qt-workflow-card">
            <div class="qt-card-top">
                <span class="qt-card-number">03</span>
                <span class="qt-card-category">MODEL EXPLORATION</span>
            </div>
            <h3>Explore a forecast</h3>
            <p>
                Examine a 30-day price projection and its uncertainty
                range. Treat forecasts as estimates, not predictions
                of guaranteed future prices.
            </p>
            <div class="qt-card-footer">Price projections · Uncertainty</div>
        </div>
        """
    )
    st.page_link(
        "pages/4_Forecast.py",
        label="Open Forecasting →",
        use_container_width=True,
    )

# -------------------- RESEARCH PRINCIPLES --------------------

st.markdown("---")

left, right = st.columns([1.2, 1], gap="large")

with left:
    st.markdown(
        '<div class="qt-section-label">THE APPROACH</div>',
        unsafe_allow_html=True,
    )
    st.markdown("### Built for transparent research")

    st.markdown(
        """
        - **Understand the assumptions:** inspect the rules behind each strategy.
        - **Compare performance and risk:** don't rely on returns alone.
        - **Keep your research organised:** use your account to manage
          your watchlist and saved results.
        """
    )

with right:
    st.html(
        """
        <div class="qt-disclaimer">
            <div class="qt-disclaimer-label">IMPORTANT</div>
            <h3>Research, not execution</h3>
            <p>
                QuantTrack does not place trades. Backtests depend on
                historical data and modelling assumptions. Transaction
                costs, data quality and overfitting can affect results.
                Past performance does not guarantee future returns.
            </p>
        </div>
        """
    )

st.markdown(
    """
    <div class="qt-footer">
        Start with Learn if you are new to quantitative finance.
        Use Account to access your watchlist and saved research.
    </div>
    """,
    unsafe_allow_html=True,
)
