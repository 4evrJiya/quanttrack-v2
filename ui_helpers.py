
"""Shared visual system and sidebar helpers for QuantTrack."""

import html

import streamlit as st


# -------------------- DESIGN TOKENS --------------------

BACKGROUND = "#0B1020"
SURFACE = "#111A2E"
SURFACE_RAISED = "#172238"
BORDER = "#293852"
TEXT = "#F2F6FC"
MUTED = "#A8B6CA"
ACCENT = "#42E8C4"
ACCENT_HOVER = "#70F2D5"
BUTTON_TEXT = "#07151A"


# -------------------- GLOBAL STYLING --------------------

def apply_custom_css():
    """Apply QuantTrack styling consistently across Streamlit pages."""

    st.html(
        f"""
        <style>
        @import url(
            'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap'
        );

        :root {{
            --qt-bg: {BACKGROUND};
            --qt-surface: {SURFACE};
            --qt-raised: {SURFACE_RAISED};
            --qt-border: {BORDER};
            --qt-text: {TEXT};
            --qt-muted: {MUTED};
            --qt-accent: {ACCENT};
            --qt-accent-hover: {ACCENT_HOVER};
            --qt-button-text: {BUTTON_TEXT};
        }}

        html, body, [class*="css"],
        [data-testid="stAppViewContainer"] {{
            font-family: 'DM Sans', sans-serif;
        }}

        [data-testid="stAppViewContainer"] {{
            background: var(--qt-bg);
            color: var(--qt-text);
        }}

        [data-testid="stHeader"] {{
            background: rgba(11, 16, 32, 0.92);
        }}

        #MainMenu, footer {{
            visibility: hidden;
        }}

        .block-container {{
            max-width: 1440px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }}

        h1, h2, h3, h4 {{
            font-family: 'Space Grotesk', sans-serif !important;
            color: var(--qt-text);
            letter-spacing: -0.025em;
        }}

        h1 {{
            font-size: clamp(2rem, 4vw, 3rem) !important;
            font-weight: 700 !important;
            line-height: 1.15 !important;
        }}

        h2 {{
            font-size: 1.65rem !important;
            font-weight: 600 !important;
        }}

        h3 {{
            font-size: 1.15rem !important;
            font-weight: 600 !important;
        }}

        p, li {{
            color: #C5D0E0;
            line-height: 1.7;
        }}

        [data-testid="stCaptionContainer"] p {{
            color: var(--qt-muted);
        }}

        /* Homepage hero */

        .qt-hero {{
            padding: clamp(1.6rem, 4vw, 3.2rem);
            margin: 0 0 2rem 0;
            border: 1px solid var(--qt-border);
            border-radius: 22px;
            background:
                radial-gradient(
                    ellipse at 90% 0%,
                    rgba(66, 232, 196, 0.12),
                    transparent 38%
                ),
                linear-gradient(135deg, #121D32, #0E1729 65%, #142238);
        }}

        .qt-eyebrow {{
            color: var(--qt-accent);
            text-transform: uppercase;
            letter-spacing: 0.14em;
            font-size: 0.75rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }}

        .qt-hero h1 {{
            font-size: clamp(2.1rem, 4.2vw, 3.5rem) !important;
            max-width: 900px;
            margin: 0 0 1rem 0;
        }}

        .qt-hero-accent {{
            color: var(--qt-accent);
        }}

        .qt-hero p {{
            max-width: 760px;
            color: #C5D0E0;
            font-size: 1rem;
            margin: 0;
        }}

        .qt-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 1.5rem;
        }}

        .qt-pill {{
            display: inline-block;
            padding: 6px 11px;
            border: 1px solid #31514F;
            border-radius: 999px;
            color: #B8F7E8;
            background: rgba(66, 232, 196, 0.07);
            font-size: 0.76rem;
            font-weight: 600;
        }}

        .qt-section-label {{
            color: var(--qt-accent);
            text-transform: uppercase;
            letter-spacing: 0.13em;
            font-size: 0.72rem;
            font-weight: 700;
            margin-bottom: 0.35rem;
        }}

        /* Homepage workflow cards */

        .qt-workflow-card {{
            box-sizing: border-box;
            min-height: 255px;
            height: 100%;
            padding: 1.35rem;
            border: 1px solid var(--qt-border);
            border-radius: 16px;
            background: linear-gradient(
                155deg,
                #172238 0%,
                #111A2E 100%
            );
            transition:
                border-color 0.18s ease,
                transform 0.18s ease;
        }}

        .qt-workflow-card:hover {{
            border-color: #42776F;
            transform: translateY(-2px);
        }}

        .qt-card-top {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 1.2rem;
        }}

        .qt-card-number {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 34px;
            height: 34px;
            border-radius: 10px;
            color: var(--qt-accent);
            background: rgba(66, 232, 196, 0.09);
            font-weight: 700;
            font-size: 0.85rem;
        }}

        .qt-card-category {{
            color: var(--qt-muted);
            font-size: 0.65rem;
            font-weight: 700;
            letter-spacing: 0.08em;
        }}

        .qt-workflow-card h3 {{
            color: var(--qt-text);
            margin: 0 0 0.7rem 0;
        }}

        .qt-workflow-card p {{
            color: var(--qt-muted);
            font-size: 0.9rem;
            line-height: 1.7;
            margin: 0 0 1.2rem 0;
        }}

        .qt-card-footer {{
            padding-top: 0.8rem;
            border-top: 1px solid var(--qt-border);
            color: #C5D0E0;
            font-size: 0.73rem;
        }}

        .qt-disclaimer {{
            padding: 1.35rem;
            border: 1px solid var(--qt-border);
            border-radius: 16px;
            background: var(--qt-surface);
        }}

        .qt-disclaimer-label {{
            color: var(--qt-accent);
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            margin-bottom: 0.65rem;
        }}

        .qt-disclaimer h3 {{
            margin-top: 0;
        }}

        .qt-disclaimer p {{
            color: var(--qt-muted);
            font-size: 0.9rem;
            margin-bottom: 0;
        }}

        .qt-footer {{
            margin-top: 1.5rem;
            padding-top: 1rem;
            border-top: 1px solid var(--qt-border);
            color: var(--qt-muted);
            font-size: 0.82rem;
        }}

        /* High-contrast buttons, including primary actions */

        div.stButton > button,
        div[data-testid="stFormSubmitButton"] > button,
        div[data-testid="stPageLink"] a {{
            box-sizing: border-box;
            border-radius: 10px !important;
            min-height: 44px;
            padding: 0.65rem 1rem;
            font-weight: 700 !important;
            transition:
                background 0.15s ease,
                border-color 0.15s ease,
                transform 0.15s ease;
        }}

        div.stButton > button[kind="primary"],
        div[data-testid="stFormSubmitButton"] > button[kind="primary"] {{
            background: var(--qt-accent) !important;
            color: var(--qt-button-text) !important;
            border: 1px solid var(--qt-accent) !important;
        }}

        div.stButton > button[kind="primary"] *,
        div[data-testid="stFormSubmitButton"] > button[kind="primary"] * {{
            color: var(--qt-button-text) !important;
        }}

        div.stButton > button[kind="primary"]:hover,
        div[data-testid="stFormSubmitButton"] > button[kind="primary"]:hover {{
            background: var(--qt-accent-hover) !important;
            color: var(--qt-button-text) !important;
            border-color: var(--qt-accent-hover) !important;
        }}

        div.stButton > button:focus-visible,
        div[data-testid="stFormSubmitButton"] > button:focus-visible {{
            outline: 2px solid var(--qt-text) !important;
            outline-offset: 3px;
        }}

        /* Page links */

        div[data-testid="stPageLink"] a {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            background: var(--qt-accent) !important;
            color: var(--qt-button-text) !important;
            border: 1px solid var(--qt-accent) !important;
            text-decoration: none !important;
        }}

        div[data-testid="stPageLink"] a * {{
            color: var(--qt-button-text) !important;
        }}

        div[data-testid="stPageLink"] a:hover {{
            background: var(--qt-accent-hover) !important;
            border-color: var(--qt-accent-hover) !important;
            transform: translateY(-1px);
        }}

        /* Metrics */

        [data-testid="stMetric"] {{
            background: linear-gradient(
                150deg,
                var(--qt-raised),
                var(--qt-surface)
            );
            border: 1px solid var(--qt-border);
            border-radius: 14px;
            padding: 1rem 1.1rem;
        }}

        [data-testid="stMetricLabel"] {{
            color: var(--qt-muted);
            font-weight: 600;
        }}

        [data-testid="stMetricValue"] {{
            font-family: 'Space Grotesk', sans-serif;
            letter-spacing: -0.035em;
        }}

        /* Inputs */

        [data-testid="stTextInput"] input,
        [data-testid="stNumberInput"] input,
        [data-testid="stDateInput"] input,
        [data-testid="stSelectbox"] [data-baseweb="select"] > div,
        [data-testid="stMultiSelect"] [data-baseweb="select"] > div {{
            background: var(--qt-surface);
            border-color: var(--qt-border);
            border-radius: 10px;
        }}

        [data-testid="stTextInput"] label,
        [data-testid="stNumberInput"] label,
        [data-testid="stDateInput"] label,
        [data-testid="stSelectbox"] label,
        [data-testid="stMultiSelect"] label {{
            color: #D5DFED;
            font-weight: 600;
        }}

        /* Tables, alerts, tabs and expanders */

        [data-testid="stDataFrame"],
        [data-testid="stTable"] {{
            border: 1px solid var(--qt-border);
            border-radius: 12px;
            overflow: hidden;
        }}

        [data-testid="stAlert"] {{
            border-radius: 12px;
        }}

        [data-testid="stExpander"] {{
            border: 1px solid var(--qt-border);
            border-radius: 12px;
            background: rgba(17, 26, 46, 0.55);
        }}

        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
            border-bottom-color: var(--qt-border);
        }}

        .stTabs [data-baseweb="tab"] {{
            font-weight: 700;
            padding: 0.65rem 1rem;
        }}

        .stTabs [aria-selected="true"] {{
            color: var(--qt-accent) !important;
        }}

        hr {{
            border-color: var(--qt-border);
            margin: 1.5rem 0;
        }}

        /* Sidebar */

        [data-testid="stSidebar"] {{
            background: #0D1526;
            border-right: 1px solid var(--qt-border);
        }}

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
            color: #AEBBD0;
        }}

        [data-testid="stSidebarNav"] {{
            padding-top: 0.5rem;
        }}

        [data-testid="stSidebarNav"] a {{
            border-radius: 9px;
            margin: 2px 0;
        }}

        [data-testid="stSidebarNav"] a[aria-current="page"] {{
            background: rgba(66, 232, 196, 0.10);
        }}

        [data-testid="stSidebarNav"] a[aria-current="page"] span {{
            color: var(--qt-accent) !important;
        }}

        .brand-header {{
            display: flex;
            align-items: center;
            gap: 11px;
            padding: 0.35rem 0 0.55rem 0;
        }}

        .brand-logo {{
            width: 36px;
            height: 36px;
            flex: 0 0 36px;
            border-radius: 11px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #42E8C4, #7D8CFF);
            color: #07151A;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: 20px;
        }}

        .brand-name {{
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: 1.18rem;
            letter-spacing: -0.04em;
            color: var(--qt-text);
        }}

        .brand-tagline {{
            color: var(--qt-muted);
            font-size: 0.72rem;
            margin-top: -2px;
        }}

        .qt-sidebar-status {{
            margin-top: 0.6rem;
            padding: 0.8rem;
            border: 1px solid var(--qt-border);
            border-radius: 12px;
            background: rgba(17, 26, 46, 0.65);
            font-size: 0.84rem;
        }}

        .qt-sidebar-status strong {{
            color: var(--qt-text);
        }}

        @media (max-width: 768px) {{
            .block-container {{
                padding-top: 1.2rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }}

            .qt-hero {{
                border-radius: 16px;
            }}

            .qt-workflow-card {{
                min-height: 0;
                margin-bottom: 0.5rem;
            }}

            .qt-card-top {{
                justify-content: flex-start;
            }}
        }}
        </style>
        """
    )


# -------------------- SIDEBAR HELPERS --------------------

def render_brand_header():
    """Render the QuantTrack brand in the sidebar."""

    st.html(
        """
        <div class="brand-header">
            <div class="brand-logo">Q</div>
            <div>
                <div class="brand-name">QuantTrack</div>
                <div class="brand-tagline">
                    Quantitative research workspace
                </div>
            </div>
        </div>
        """
    )


def render_sidebar_status():
    """Display the current user's session status."""

    with st.sidebar:
        render_brand_header()
        st.divider()

        if "logged_in_username" in st.session_state:
            username = html.escape(
                str(st.session_state["logged_in_username"])
            )
            st.html(
                f"""
                <div class="qt-sidebar-status">
                    Signed in as<br>
                    <strong>{username}</strong>
                </div>
                """
            )
        else:
            st.html(
                """
                <div class="qt-sidebar-status">
                    Research workspace<br>
                    <strong>Guest session</strong>
                </div>
                """
            )
