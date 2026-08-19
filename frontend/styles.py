import streamlit as st

def apply_custom_styles():
    """
    Applies an ultra-premium, dark-mode SaaS design system inspired by Linear,
    Vercel, and Stripe with instant, dramatic floating card lift and radiant
    neon blue aura on hover.
    Strictly preserves 100% of the existing frontend layout, pages, sections, 
    navigation, widgets, and functionality.
    """
    custom_css = """
    <style>
    /* ==========================================================================
       FONTS: INTER & MATERIAL SYMBOLS PRESERVATION
       ========================================================================== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Preserve Streamlit Material Icons */
    [data-testid="stIconMaterial"], 
    [class*="material-icons"], 
    [class*="material-symbols"], 
    [class*="material-symbols-rounded"], 
    [class*="material-symbols-outlined"],
    [data-testid="stSidebarCollapseButton"] span,
    [data-testid="stBaseButton-headerNoPadding"] span,
    span[data-testid="stIconMaterial"] {
        font-family: 'Material Symbols Rounded', 'Material Icons', sans-serif !important;
        font-style: normal !important;
        letter-spacing: normal !important;
    }

    /* Global typography */
    html, body, .stApp, p, span, label, [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] span {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    /* Base background — very faint ambient vignette */
    .stApp {
        background-color: #080D0B !important;
        background-image: radial-gradient(circle at 50% 0%, rgba(53, 201, 138, 0.04) 0%, transparent 60%) !important;
        background-attachment: fixed !important;
        color: #F5F7F6 !important;
    }

    /* Main container spacing & alignment */
    [data-testid="block-container"] {
        max-width: 1140px !important;
        padding-top: 2.25rem !important;
        padding-bottom: 4.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }

    /* PREVENT OVERFLOW CLIPPING FOR FLOATING CARDS */
    [data-testid="stHorizontalBlock"],
    [data-testid="stColumn"],
    [data-testid="stColumn"] > div,
    [data-testid="stVerticalBlock"],
    [data-testid="element-container"],
    [data-testid="stVerticalBlockBorderWrapper"] {
        overflow: visible !important;
    }

    /* ==========================================================================
       HEADINGS — MODERN WITH CLEAN ACCENTS
       ========================================================================== */
    h1, .stHeading h1, [data-testid="stHeadingWithActionElements"] h1 {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        font-weight: 700 !important;
        color: #FFFFFF !important;
        letter-spacing: -0.04em !important;
        font-size: 1.95rem !important;
        margin-bottom: 0.4rem !important;
        margin-top: 0.2rem !important;
        text-shadow: 0 0 20px rgba(53, 201, 138, 0.3) !important;
    }

    h2, .stHeading h2 {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        font-weight: 600 !important;
        color: #C8CDD5 !important;
        letter-spacing: -0.025em !important;
        font-size: 1.15rem !important;
        margin-top: 0.6rem !important;
        margin-bottom: 0.6rem !important;
    }

    h3, .stHeading h3 {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        font-weight: 600 !important;
        color: #E2E8F0 !important;
        letter-spacing: -0.015em !important;
        font-size: 1.0rem !important;
        margin-top: 0.4rem !important;
        margin-bottom: 0.4rem !important;
    }

    p, .stMarkdown p {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #9AA8A1;
        font-size: 0.94rem;
        line-height: 1.65;
    }

    /* Muted text & Captions */
    .stCaption, [data-testid="stCaptionContainer"] p, [data-testid="stCaptionContainer"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #9AA8A1 !important;
        font-size: 0.85rem !important;
        font-weight: 400 !important;
        line-height: 1.5 !important;
    }

    /* ==========================================================================
       SIDEBAR — ELEVATED BRAND WITH GLOW
       ========================================================================== */
    [data-testid="stSidebar"] {
        background-color: #0C1210 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.07) !important;
        min-width: 240px !important;
    }

    [data-testid="stSidebar"] [data-testid="stSidebarContent"] {
        padding-top: 1.75rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    [data-testid="stSidebar"] h1 {
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.025em !important;
        color: #FFFFFF !important;
        margin-bottom: 1.25rem !important;
        padding-bottom: 0.85rem !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06) !important;
        text-shadow: 0 0 16px rgba(53, 201, 138, 0.35) !important;
        white-space: nowrap !important;
    }

    /* Sidebar navigation buttons — subtle hover with glow */
    [data-testid="stSidebar"] .stButton > button {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background: transparent !important;
        border: 1px solid transparent !important;
        color: #9AA8A1 !important;
        text-align: left !important;
        justify-content: flex-start !important;
        border-radius: 9px !important;
        font-weight: 500 !important;
        font-size: 0.91rem !important;
        padding: 0.6rem 0.9rem !important;
        transition: all 300ms cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: none !important;
        width: 100% !important;
        margin-bottom: 0.3rem !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }

        [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(53, 201, 138, 0.05) !important;
        border-color: rgba(53, 201, 138, 0.35) !important;
        color: #F5F7F6 !important;
        transform: translateX(3px) !important;
        box-shadow: 0 0 12px rgba(53, 201, 138, 0.15) !important;
    }

    [data-testid="stSidebar"] .stButton > button:active {
        background: rgba(255, 255, 255, 0.08) !important;
        transform: translateX(1px) !important;
    }

    /* Top header bar */
    [data-testid="stHeader"] {
        background: rgba(8, 9, 11, 0.8) !important;
        backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* ==========================================================================
       BORDERED CONTAINERS — BASE STYLING (ALL PAGES)
       ========================================================================== */
        div[data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stColumn"] div[data-testid="stVerticalBlockBorderWrapper"],
    .st-emotion-cache-12w0qpk {
        background-color: #111916 !important;
        background-image: linear-gradient(180deg, rgba(110, 231, 183, 0.02) 0%, transparent 100%) !important;
        border: 1px solid rgba(110, 231, 183, 0.10) !important;
        border-radius: 14px !important;
        padding: 1.5rem !important;
        min-height: 140px !important;
        box-shadow: 0 4px 16px -2px rgba(0, 0, 0, 0.4), inset 0 1px 0 0 rgba(110, 231, 183, 0.05) !important;
        position: relative !important;
        transform: translateY(0px) scale(1) !important;
        transition:
            transform 300ms cubic-bezier(0.16, 1, 0.3, 1),
            box-shadow 300ms cubic-bezier(0.16, 1, 0.3, 1),
            border-color 300ms cubic-bezier(0.16, 1, 0.3, 1),
            background-color 300ms cubic-bezier(0.16, 1, 0.3, 1),
            background-image 300ms ease !important;
        will-change: transform, box-shadow, border-color, background-color;
        cursor: default !important;
    }

    /* Card hover — Floating lift with radiant ambient glow & top lighting */
        div[data-testid="stVerticalBlockBorderWrapper"]:hover,
    [data-testid="stVerticalBlockBorderWrapper"]:hover,
    [data-testid="stColumn"] div[data-testid="stVerticalBlockBorderWrapper"]:hover,
    .st-emotion-cache-12w0qpk:hover {
        transform: translateY(-6px) scale(1.01) !important;
        border-color: rgba(110, 231, 183, 0.3) !important;
        background-color: #15211C !important;
        box-shadow:
            0 18px 45px rgba(0,0,0,0.45),
            0 0 28px rgba(53,201,138,0.16),
            inset 0 1px 0 0 rgba(110, 231, 183, 0.2) !important;
        background-image: radial-gradient(circle at 50% 0%, rgba(53, 201, 138, 0.08) 0%, transparent 80%) !important;
        z-index: 20 !important;
    }

    /* KPI metric value glowing effect on hover */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover [data-testid="stMetricValue"] div {
        color: #FFFFFF !important;
        text-shadow: 0 0 16px rgba(110, 231, 183, 0.4), 0 0 24px rgba(53, 201, 138, 0.3) !important;
        transform: scale(1.02) !important;
        transition: all 300ms cubic-bezier(0.16, 1, 0.3, 1) !important;
    }

    /* KPI label on hover — subtle blue highlight */
    div[data-testid="stVerticalBlockBorderWrapper"]:hover [data-testid="stMetricLabel"] p,
    div[data-testid="stVerticalBlockBorderWrapper"]:hover [data-testid="stMetricLabel"] span {
        color: #6EE7B7 !important;
        text-shadow: 0 0 10px rgba(110, 231, 183, 0.4) !important;
        transition: color 300ms ease, text-shadow 300ms ease !important;
    }

    /* Dividers */
    [data-testid="stDivider"], hr {
        border: none !important;
        height: 1px !important;
        background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.08) 20%, rgba(255, 255, 255, 0.08) 80%, transparent 100%) !important;
        margin: 1.6rem 0 !important;
    }

    /* ==========================================================================
       METRICS — KPI VALUES
       ========================================================================== */
    [data-testid="stMetric"] {
        background: transparent !important;
        padding: 0.2rem 0 !important;
    }

    [data-testid="stMetricLabel"] p, [data-testid="stMetricLabel"] span {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #6B7280 !important;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        margin-bottom: 0.35rem !important;
        transition: color 300ms ease, text-shadow 300ms ease !important;
    }

    [data-testid="stMetricValue"] div {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #FFFFFF !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.03em !important;
        text-shadow: 0 0 12px rgba(53, 201, 138, 0.15) !important;
        transition: all 300ms cubic-bezier(0.16, 1, 0.3, 1) !important;
    }

    /* ==========================================================================
       BUTTONS — PREMIUM WITH GLOW
       ========================================================================== */
    .stButton > button, 
    [data-testid="baseButton-secondary"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background: linear-gradient(180deg, #15211C 0%, #111916 100%) !important;
        color: #F5F7F6 !important;
        border: 1px solid rgba(255, 255, 255, 0.11) !important;
        border-radius: 9px !important;
        padding: 0.58rem 1.25rem !important;
        font-weight: 500 !important;
        font-size: 0.92rem !important;
        transition: all 300ms cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.06), 0 2px 6px rgba(0, 0, 0, 0.25) !important;
        white-space: nowrap !important;
    }

    .stButton > button:hover, 
    [data-testid="baseButton-secondary"]:hover {
        background: linear-gradient(180deg, #1A2922 0%, #15211C 100%) !important;
        border-color: rgba(53, 201, 138, 0.45) !important;
        color: #FFFFFF !important;
        transform: translateY(-2px) !important;
        box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.12),
                    0 6px 18px rgba(0, 0, 0, 0.4),
                    0 0 16px rgba(53, 201, 138, 0.22) !important;
    }

    .stButton > button:active, 
    [data-testid="baseButton-secondary"]:active {
        transform: translateY(0px) !important;
        background: #111916 !important;
        box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.4) !important;
    }

    /* Primary CTA button with glowing aura */
    .stButton > button[kind="primary"],
    [data-testid="baseButton-primary"] {
        background: linear-gradient(180deg, #35C98A 0%, #2F8F6B 100%) !important;
        border: 1px solid rgba(110, 231, 183, 0.35) !important;
        color: #FFFFFF !important;
        box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.25),
                    0 4px 14px rgba(47, 143, 107, 0.35),
                    0 0 18px rgba(53, 201, 138, 0.2) !important;
        transition: all 300ms cubic-bezier(0.16, 1, 0.3, 1) !important;
        white-space: nowrap !important;
    }

    .stButton > button[kind="primary"]:hover,
    [data-testid="baseButton-primary"]:hover {
        background: linear-gradient(180deg, #6EE7B7 0%, #35C98A 100%) !important;
        border-color: rgba(167, 243, 208, 0.6) !important;
        box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.35),
                    0 8px 22px rgba(47, 143, 107, 0.5),
                    0 0 24px rgba(53, 201, 138, 0.35) !important;
        transform: translateY(-2px) !important;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.4) !important;
    }

    /* Link buttons (st.link_button) */
    a[data-testid="stLinkButton"], 
    .stLinkButton > a {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background: linear-gradient(180deg, #15211C 0%, #111916 100%) !important;
        color: #6EE7B7 !important;
        border: 1px solid rgba(53, 201, 138, 0.2) !important;
        border-radius: 9px !important;
        padding: 0.58rem 1.25rem !important;
        font-weight: 500 !important;
        font-size: 0.92rem !important;
        text-decoration: none !important;
        transition: all 300ms cubic-bezier(0.16, 1, 0.3, 1) !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.06), 0 2px 6px rgba(0, 0, 0, 0.25) !important;
        white-space: nowrap !important;
    }

    a[data-testid="stLinkButton"]:hover, 
    .stLinkButton > a:hover {
        background: linear-gradient(180deg, rgba(53, 201, 138, 0.12) 0%, rgba(53, 201, 138, 0.06) 100%) !important;
        border-color: rgba(53, 201, 138, 0.4) !important;
        color: #6EE7B7 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.35), 0 0 6px rgba(53, 201, 138, 0.1) !important;
    }

    /* ==========================================================================
       FORM CONTROLS & INPUTS
       ========================================================================== */
    /* Widget labels */
    [data-testid="stWidgetLabel"] label, 
    [data-testid="stWidgetLabel"] p {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #9AA8A1 !important;
        font-size: 0.86rem !important;
        font-weight: 500 !important;
        margin-bottom: 0.4rem !important;
    }

    /* Text & Password inputs */
    [data-testid="stTextInput"] input, 
    [data-testid="stNumberInput"] input, 
    .stTextInput > div > div > input {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #0C1210 !important;
        color: #F5F7F6 !important;
        border: 1px solid rgba(255, 255, 255, 0.09) !important;
        border-radius: 8px !important;
        padding: 0.58rem 0.9rem !important;
        font-size: 0.92rem !important;
        box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.35) !important;
        transition: all 300ms cubic-bezier(0.16, 1, 0.3, 1) !important;
    }

    [data-testid="stTextInput"] input:focus, 
    [data-testid="stNumberInput"] input:focus, 
    .stTextInput > div > div > input:focus {
        border-color: #35C98A !important;
        box-shadow: 0 0 0 3px rgba(53, 201, 138, 0.15), inset 0 1px 2px rgba(0, 0, 0, 0.2) !important;
        outline: none !important;
        background-color: #111916 !important;
    }

    [data-testid="stTextInput"] input::placeholder {
        color: #626975 !important;
    }

    /* Selectbox */
    [data-testid="stSelectbox"] > div > div {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #0C1210 !important;
        border: 1px solid rgba(255, 255, 255, 0.09) !important;
        border-radius: 8px !important;
        color: #F5F7F6 !important;
        font-size: 0.92rem !important;
        box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.35) !important;
        transition: all 300ms cubic-bezier(0.16, 1, 0.3, 1) !important;
    }

    [data-testid="stSelectbox"] > div > div:focus-within {
        border-color: #35C98A !important;
        box-shadow: 0 0 0 3px rgba(53, 201, 138, 0.15), inset 0 1px 2px rgba(0, 0, 0, 0.2) !important;
        background-color: #111916 !important;
    }

    /* Dropdown menu popover */
    ul[data-baseweb="menu"], [data-baseweb="popover"] {
        background-color: #15211C !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.55), inset 0 1px 0 0 rgba(255, 255, 255, 0.05) !important;
        padding: 4px !important;
    }

    li[data-baseweb="menu-item"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #E2E8F0 !important;
        font-size: 0.9rem !important;
        padding: 0.55rem 0.85rem !important;
        border-radius: 6px !important;
        margin: 2px 0 !important;
        transition: all 0.15s ease !important;
    }

    li[data-baseweb="menu-item"]:hover {
        background-color: #1E2330 !important;
        color: #6EE7B7 !important;
    }

    /* Radio buttons */
    [data-testid="stRadio"] label {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #9AA8A1 !important;
        font-size: 0.9rem !important;
        cursor: pointer !important;
        transition: color 0.15s ease !important;
    }

    [data-testid="stRadio"] label:hover {
        color: #FFFFFF !important;
    }

    [data-testid="stRadio"] div[role="radiogroup"] {
        gap: 0.85rem !important;
    }

    /* Sliders — reduced glow */
    [data-testid="stSlider"] div[data-baseweb="slider"] {
        padding-top: 0.5rem !important;
    }

    [data-testid="stSlider"] div[role="slider"] {
        background-color: #35C98A !important;
        border: 2px solid #FFFFFF !important;
        box-shadow: 0 0 0 4px rgba(53, 201, 138, 0.2), 0 0 6px rgba(53, 201, 138, 0.3) !important;
    }

    /* File uploader */
    [data-testid="stFileUploader"] section {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.02) 0%, rgba(255, 255, 255, 0) 100%), #111916 !important;
        border: 1px dashed rgba(255, 255, 255, 0.12) !important;
        border-radius: 12px !important;
        padding: 1.75rem 1.5rem !important;
        box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.03) !important;
        transition: all 300ms cubic-bezier(0.16, 1, 0.3, 1) !important;
    }

    [data-testid="stFileUploader"] section:hover {
        border-color: rgba(53, 201, 138, 0.35) !important;
        background-color: #15211C !important;
        box-shadow: 0 4px 14px -4px rgba(0, 0, 0, 0.4) !important;
        transform: translateY(-1px) !important;
    }

    /* ==========================================================================
       TABS — CLEAN UNDERLINE, NO TEXT GLOW
       ========================================================================== */
    [data-testid="stTabs"] [data-baseweb="tab-list"] {
        gap: 0.5rem !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
        background: transparent !important;
        padding-bottom: 0px !important;
    }

    [data-testid="stTabs"] button[data-baseweb="tab"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background: transparent !important;
        color: #9AA8A1 !important;
        border: none !important;
        border-bottom: 2px solid transparent !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        padding: 0.65rem 1.25rem !important;
        transition: all 0.18s ease !important;
    }

    [data-testid="stTabs"] button[data-baseweb="tab"]:hover {
        color: #FFFFFF !important;
    }

    [data-testid="stTabs"] button[aria-selected="true"] {
        color: #FFFFFF !important;
        border-bottom: 2px solid #35C98A !important;
        font-weight: 600 !important;
        text-shadow: 0 0 12px rgba(53, 201, 138, 0.45) !important;
    }

    /* ==========================================================================
       DATAFRAMES & TABLES
       ========================================================================== */
    [data-testid="stDataFrame"] {
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        background-color: #111916 !important;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.25) !important;
    }

    /* ==========================================================================
       CODE BLOCKS — CONSISTENT DARK SURFACE
       ========================================================================== */
    [data-testid="stCode"], pre, code {
        background-color: #0D0F14 !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 10px !important;
    }

    /* ==========================================================================
       ALERTS & NOTIFICATIONS
       ========================================================================== */
    [data-testid="stAlert"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        border-radius: 10px !important;
        font-size: 0.9rem !important;
        padding: 0.85rem 1.15rem !important;
        backdrop-filter: blur(8px) !important;
    }

    /* Info */
    [data-testid="stAlert"]:has([data-testid="stAlertContentInfo"]),
    div[data-baseweb="notification"]:has(div[class*="info"]) {
        background: linear-gradient(90deg, rgba(53, 201, 138, 0.08) 0%, rgba(53, 201, 138, 0.02) 100%) !important;
        border: 1px solid rgba(53, 201, 138, 0.18) !important;
        border-left: 3px solid #35C98A !important;
        color: #A7F3D0 !important;
    }

    /* Success */
    [data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]) {
        background: linear-gradient(90deg, rgba(34, 197, 94, 0.08) 0%, rgba(34, 197, 94, 0.02) 100%) !important;
        border: 1px solid rgba(34, 197, 94, 0.18) !important;
        border-left: 3px solid #22C55E !important;
        color: #BBF7D0 !important;
    }

    /* Warning */
    [data-testid="stAlert"]:has([data-testid="stAlertContentWarning"]) {
        background: linear-gradient(90deg, rgba(245, 158, 11, 0.08) 0%, rgba(245, 158, 11, 0.02) 100%) !important;
        border: 1px solid rgba(245, 158, 11, 0.18) !important;
        border-left: 3px solid #F59E0B !important;
        color: #FDE68A !important;
    }

    /* Error */
    [data-testid="stAlert"]:has([data-testid="stAlertContentError"]) {
        background: linear-gradient(90deg, rgba(239, 68, 68, 0.08) 0%, rgba(239, 68, 68, 0.02) 100%) !important;
        border: 1px solid rgba(239, 68, 68, 0.18) !important;
        border-left: 3px solid #EF4444 !important;
        color: #FECACA !important;
    }

    /* ==========================================================================
       CHAT & COPILOT — NO FLOAT ON HOVER
       ========================================================================== */
    [data-testid="stChatMessage"] {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.02) 0%, rgba(255, 255, 255, 0) 100%), #111916 !important;
        border: 1px solid rgba(255, 255, 255, 0.07) !important;
        border-radius: 12px !important;
        padding: 1.1rem 1.35rem !important;
        margin-bottom: 0.85rem !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
        transition: border-color 300ms ease !important;
    }

    [data-testid="stChatMessage"]:hover {
        border-color: rgba(255, 255, 255, 0.12) !important;
    }

    [data-testid="stChatInput"] {
        background-color: transparent !important;
    }

    [data-testid="stChatInput"] textarea {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #0C1210 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        color: #F5F7F6 !important;
        font-size: 0.92rem !important;
        padding: 0.75rem 1rem !important;
        box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.35) !important;
        transition: all 300ms cubic-bezier(0.16, 1, 0.3, 1) !important;
    }

    [data-testid="stChatInput"] textarea:focus {
        border-color: #35C98A !important;
        box-shadow: 0 0 0 3px rgba(53, 201, 138, 0.15), inset 0 1px 2px rgba(0, 0, 0, 0.2) !important;
        background-color: #111916 !important;
    }

    /* ==========================================================================
       SCROLLBARS
       ========================================================================== */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }

    ::-webkit-scrollbar-track {
        background: #080D0B;
    }

    ::-webkit-scrollbar-thumb {
        background: #1A2922;
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #2F4037;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
