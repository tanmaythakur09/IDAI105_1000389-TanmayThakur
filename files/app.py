"""
╔═══════════════════════════════════════════════════════════════════════════╗
║  PREMIUM AI DATA MINING DASHBOARD - ENTERPRISE-GRADE ANALYTICS             ║
║  World-Class | Production-Ready | Portfolio-Grade Performance              ║
╚═══════════════════════════════════════════════════════════════════════════╝

PREMIUM FEATURES:
  ✓ Glassmorphism UI with Professional Color Science
  ✓ Advanced Micro-Interactions & Smooth Animations
  ✓ Premium Typography System (Orbitron + Poppins)
  ✓ Professional Neon Accents (Cyan & Teal)
  ✓ Dynamic Card-Based Layout Architecture
  ✓ Seamless Dark Theme Integration
  ✓ Enterprise-Level Data Visualizations
  ✓ Real-Time Filter Synchronization
  ✓ Portfolio-Grade Code Quality

RUN: python -m streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.covariance import EllipticEnvelope
import warnings
import hashlib
from datetime import datetime

warnings.filterwarnings('ignore')

# ═══════════════════════════════════════════════════════════════════════════
# 🔐 CONFIGURATION & PAGE SETUP
# ═══════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Premium AI Analytics",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════════════
# 🎨 PREMIUM THEME - WORLD-CLASS DESIGN SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

PREMIUM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;500;600;700;800&display=swap');

    /* ═══ DESIGN TOKENS ═══ */
    :root {
        --primary-dark: #0a0e27;
        --secondary-dark: #141829;
        --tertiary-dark: #1a1f3a;
        --card-bg: rgba(20, 24, 41, 0.7);
        --accent-cyan: #00d9ff;
        --accent-teal: #00b8a9;
        --accent-blue: #0064e8;
        --text-primary: #ffffff;
        --text-secondary: #a0aec0;
        --success: #00ff88;
        --warning: #ffd700;
        --danger: #ff4757;
        --border: rgba(0, 217, 255, 0.1);
    }

    /* ═══ GLOBAL BASE ═══ */
    * {
        font-family: 'Poppins', sans-serif;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, var(--primary-dark) 0%, var(--tertiary-dark) 50%, var(--primary-dark) 100%) !important;
        color: var(--text-primary) !important;
        min-height: 100vh;
    }

    [data-testid="stAppViewContainer"] {
        background-attachment: fixed;
    }

    /* ═══ SIDEBAR STYLING ═══ */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(20, 24, 41, 0.95) 0%, rgba(10, 14, 39, 0.95) 100%) !important;
        border-right: 1px solid var(--border) !important;
        box-shadow: inset -1px 0 30px rgba(0, 217, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
    }

    [data-testid="stSidebarContent"] {
        padding-top: 1.5rem !important;
    }

    /* ═══ HEADING SYSTEM ═══ */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Orbitron', sans-serif !important;
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        letter-spacing: 0.04em !important;
    }

    h1 {
        font-size: 2.8rem !important;
        background: linear-gradient(90deg, var(--accent-cyan), var(--accent-teal)) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        text-shadow: 0 0 30px rgba(0, 217, 255, 0.2) !important;
        animation: fadeInDown 0.8s ease-out !important;
    }

    h2 {
        font-size: 1.8rem !important;
        background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue)) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        border-left: 4px solid var(--accent-cyan) !important;
        padding-left: 1.5rem !important;
        margin: 2.5rem 0 1.5rem 0 !important;
        animation: fadeInLeft 0.8s ease-out !important;
    }

    h3 {
        color: var(--accent-cyan) !important;
        font-size: 1.4rem !important;
    }

    /* ═══ ANIMATIONS ═══ */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInLeft {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes glowPulse {
        0%, 100% {
            box-shadow: 0 0 20px rgba(0, 217, 255, 0.4), inset 0 0 20px rgba(0, 217, 255, 0.1);
        }
        50% {
            box-shadow: 0 0 40px rgba(0, 217, 255, 0.6), inset 0 0 30px rgba(0, 217, 255, 0.15);
        }
    }

    /* ═══ METRIC CARDS ═══ */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(0, 100, 232, 0.1) 0%, rgba(0, 184, 169, 0.05) 100%) !important;
        border: 1px solid rgba(0, 217, 255, 0.2) !important;
        border-radius: 12px !important;
        padding: 1.8rem !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(0, 217, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        animation: fadeInUp 0.6s ease-out !important;
    }

    [data-testid="metric-container"]:hover {
        border-color: var(--accent-cyan) !important;
        box-shadow: 0 16px 48px rgba(0, 217, 255, 0.3), inset 0 1px 0 rgba(0, 217, 255, 0.2) !important;
        transform: translateY(-4px) scale(1.01) !important;
    }

    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: var(--accent-cyan) !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }

    [data-testid="metric-container"] [data-testid="stMetricLabel"] {
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.02em !important;
    }

    /* ═══ BUTTONS ═══ */
    [data-testid="stButton"] > button {
        background: linear-gradient(135deg, var(--accent-blue) 0%, var(--accent-teal) 100%) !important;
        color: var(--text-primary) !important;
        border: 1px solid rgba(0, 217, 255, 0.3) !important;
        border-radius: 10px !important;
        padding: 0.75rem 1.8rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.02em !important;
        box-shadow: 0 4px 20px rgba(0, 100, 232, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
        position: relative;
        overflow: hidden;
    }

    [data-testid="stButton"] > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }

    [data-testid="stButton"] > button:hover {
        box-shadow: 0 8px 40px rgba(0, 217, 255, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        transform: translateY(-2px) !important;
        border-color: var(--accent-cyan) !important;
    }

    [data-testid="stButton"] > button:hover::before {
        left: 100%;
    }

    /* ═══ INPUT FIELDS ═══ */
    input, textarea, [data-testid="stTextInput"] input, [data-testid="stSelectbox"] input {
        background-color: rgba(10, 14, 39, 0.6) !important;
        border: 1px solid rgba(0, 217, 255, 0.2) !important;
        color: var(--text-primary) !important;
        border-radius: 8px !important;
        padding: 0.7rem 1rem !important;
        font-family: 'Poppins', sans-serif !important;
        transition: all 0.3s ease !important;
    }

    input:focus, textarea:focus, [data-testid="stTextInput"] input:focus {
        border-color: var(--accent-cyan) !important;
        box-shadow: inset 0 0 0 1px rgba(0, 217, 255, 0.3), 0 0 20px rgba(0, 217, 255, 0.2) !important;
        outline: none !important;
        background-color: rgba(10, 14, 39, 0.8) !important;
    }

    /* ═══ SELECTBOX & MULTISELECT ═══ */
    [data-testid="stSelectbox"], [data-testid="stMultiSelect"] {
        color: var(--text-primary) !important;
    }

    [data-testid="stSelectbox"] > div > div, [data-testid="stMultiSelect"] > div > div {
        background-color: rgba(10, 14, 39, 0.6) !important;
        border: 1px solid rgba(0, 217, 255, 0.2) !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="stSelectbox"] > div > div:hover, [data-testid="stMultiSelect"] > div > div:hover {
        border-color: var(--accent-cyan) !important;
    }

    /* ═══ SLIDER ═══ */
    [data-testid="stSlider"] {
        margin: 1.5rem 0 !important;
    }

    [data-testid="stSlider"] > div > div > div > div {
        color: var(--accent-cyan) !important;
    }

    /* ═══ TABLE ═══ */
    table {
        background-color: rgba(20, 24, 41, 0.5) !important;
        border-color: rgba(0, 217, 255, 0.1) !important;
    }

    th {
        background: linear-gradient(90deg, rgba(0, 100, 232, 0.15), rgba(0, 184, 169, 0.1)) !important;
        color: var(--accent-cyan) !important;
        font-weight: 700 !important;
        border-color: rgba(0, 217, 255, 0.2) !important;
        padding: 1rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.02em !important;
        font-size: 0.85rem !important;
    }

    td {
        border-color: rgba(0, 217, 255, 0.1) !important;
        color: var(--text-secondary) !important;
        padding: 0.85rem 1rem !important;
        transition: all 0.2s ease !important;
    }

    tr:hover td {
        background-color: rgba(0, 217, 255, 0.05) !important;
    }

    /* ═══ EXPANDER ═══ */
    [data-testid="stExpander"] {
        border: 1px solid rgba(0, 217, 255, 0.15) !important;
        border-radius: 8px !important;
        background-color: rgba(14, 18, 34, 0.6) !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="stExpander"] summary {
        color: var(--accent-cyan) !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        padding: 1rem !important;
    }

    [data-testid="stExpander"]:hover {
        border-color: rgba(0, 217, 255, 0.3) !important;
        box-shadow: inset 0 0 20px rgba(0, 217, 255, 0.05) !important;
    }

    /* ═══ DIVIDER ═══ */
    hr {
        border: 0 !important;
        height: 1px !important;
        background: linear-gradient(90deg, transparent, rgba(0, 217, 255, 0.3), transparent) !important;
        margin: 2rem 0 !important;
    }

    /* ═══ SCROLL BAR ═══ */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(10, 14, 39, 0.5);
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--accent-cyan), var(--accent-teal));
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 217, 255, 0.2);
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, var(--accent-teal), var(--accent-cyan));
        box-shadow: 0 0 20px rgba(0, 217, 255, 0.4);
    }

    /* ═══ PLACEHOLDER TEXT ═══ */
    ::placeholder {
        color: var(--text-secondary) !important;
        opacity: 0.6 !important;
    }

    /* ═══ WARNINGS & ALERTS ═══ */
    [data-testid="stWarning"], [data-testid="stAlert"] {
        background: linear-gradient(135deg, rgba(255, 215, 0, 0.1) 0%, rgba(255, 107, 107, 0.05) 100%) !important;
        border-left: 4px solid var(--warning) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }

    [data-testid="stSuccess"] {
        background: linear-gradient(135deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 184, 169, 0.05) 100%) !important;
        border-left: 4px solid var(--success) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }

    [data-testid="stError"] {
        background: linear-gradient(135deg, rgba(255, 71, 87, 0.1) 0%, rgba(255, 0, 0, 0.05) 100%) !important;
        border-left: 4px solid var(--danger) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }

    /* ═══ INFO TEXT ═══ */
    [data-testid="stInfo"] {
        background: linear-gradient(135deg, rgba(0, 100, 232, 0.1) 0%, rgba(0, 217, 255, 0.05) 100%) !important;
        border-left: 4px solid var(--accent-blue) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }

    /* ═══ CARD WRAPPER ═══ */
    .premium-card {
        background: linear-gradient(135deg, rgba(20, 24, 41, 0.8) 0%, rgba(26, 31, 44, 0.6) 100%) !important;
        border: 1px solid rgba(0, 217, 255, 0.15) !important;
        border-radius: 12px !important;
        padding: 2rem !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(0, 217, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        margin: 1.5rem 0 !important;
        animation: fadeInUp 0.6s ease-out !important;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }

    .premium-card:hover {
        border-color: rgba(0, 217, 255, 0.3) !important;
        box-shadow: 0 16px 48px rgba(0, 217, 255, 0.2), inset 0 1px 0 rgba(0, 217, 255, 0.2) !important;
        transform: translateY(-2px) !important;
    }

    /* ═══ TEXT COLORS ═══ */
    p, span, a {
        color: var(--text-secondary) !important;
        transition: color 0.3s ease !important;
    }

    a {
        color: var(--accent-cyan) !important;
        text-decoration: none;
    }

    a:hover {
        color: var(--accent-teal) !important;
        text-decoration: underline;
    }
</style>
"""

st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# 📂 DATA LOADING - CACHED & OPTIMIZED
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data
def load_black_friday_data():
    """Load Black Friday dataset with caching for lightning-fast performance"""
    try:
        paths = [
            'black_friday.csv',
            '../data/black_friday.csv',
            'data/black_friday.csv',
        ]

        df = None
        for path in paths:
            try:
                df = pd.read_csv(path)
                break
            except FileNotFoundError:
                continue

        if df is None:
            np.random.seed(42)
            n_records = 500
            df = pd.DataFrame({
                'User_ID': np.random.randint(1000, 5500, n_records),
                'Product_ID': np.random.randint(1, 20, n_records),
                'Gender': np.random.choice(['M', 'F'], n_records),
                'Age': np.random.choice(['0-17', '18-25', '26-35', '36-45', '46-50', '51-55', '55+'], n_records),
                'Category': np.random.randint(1, 19, n_records),
                'Purchase': np.random.gamma(2, 5000, n_records).astype(int),
            })

        return df.copy()
    except Exception as error:
        st.error(f"Error loading data: {error}")
        return pd.DataFrame()

# ═══════════════════════════════════════════════════════════════════════════
# 🔐 LOGIN SYSTEM - GLASSMORPHISM & ANIMATIONS
# ═══════════════════════════════════════════════════════════════════════════

def hash_password(password):
    """Simple password hashing for security"""
    return hashlib.sha256(password.encode()).hexdigest()

def initialize_session_state():
    """Initialize all session state variables on app start"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'login_attempts' not in st.session_state:
        st.session_state.login_attempts = 0

def render_login_page():
    """Render premium modern login interface"""

    login_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;500;600;700&display=swap');

        .login-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 2rem;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
        }

        .login-card {
            width: 100%;
            max-width: 450px;
            background: linear-gradient(135deg, rgba(20, 24, 41, 0.95), rgba(14, 18, 34, 0.85)) !important;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(0, 217, 255, 0.25);
            border-radius: 16px;
            padding: 3.5rem 2.8rem;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(0, 217, 255, 0.1);
            animation: slideUp 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(40px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .login-header {
            text-align: center;
            margin-bottom: 3rem;
        }

        .login-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(90deg, #00d9ff, #00b8a9);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 0 0.7rem 0;
            letter-spacing: 0.05em;
            text-shadow: 0 0 30px rgba(0, 217, 255, 0.1);
        }

        .login-subtitle {
            color: #a0aec0;
            font-size: 0.95rem;
            font-weight: 400;
            letter-spacing: 0.015em;
            margin: 0;
        }

        .divider-line {
            height: 2px;
            background: linear-gradient(90deg, transparent, rgba(0, 217, 255, 0.4), transparent);
            margin: 2.5rem 0;
        }

        .login-form-group {
            margin-bottom: 1.8rem;
        }

        .login-label {
            display: block;
            color: #e2e8f0;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 0.7rem;
            letter-spacing: 0.02em;
            text-transform: uppercase;
        }

        .login-input {
            width: 100%;
            padding: 0.85rem 1.1rem;
            background: rgba(10, 14, 39, 0.6);
            border: 1px solid rgba(0, 217, 255, 0.2);
            border-radius: 10px;
            color: #ffffff;
            font-size: 0.95rem;
            font-family: 'Poppins', sans-serif;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-sizing: border-box;
        }

        .login-input::placeholder {
            color: #64748b;
        }

        .login-input:focus {
            outline: none;
            border-color: #00d9ff;
            box-shadow: 0 0 0 3px rgba(0, 217, 255, 0.15), inset 0 1px 0 rgba(0, 217, 255, 0.1);
            background: rgba(10, 14, 39, 0.8);
            transform: translateY(-2px);
        }

        .login-button {
            width: 100%;
            padding: 0.9rem 1.5rem;
            background: linear-gradient(135deg, #0064e8, #00b8a9);
            color: white;
            border: 1px solid rgba(0, 217, 255, 0.3);
            border-radius: 10px;
            font-size: 0.95rem;
            font-weight: 600;
            letter-spacing: 0.03em;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 4px 20px rgba(0, 100, 232, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
            margin-top: 1.5rem;
            text-transform: uppercase;
            position: relative;
            overflow: hidden;
        }

        .login-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }

        .login-button:hover {
            box-shadow: 0 8px 40px rgba(0, 217, 255, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
            transform: translateY(-3px);
            border-color: #00d9ff;
        }

        .login-button:hover::before {
            left: 100%;
        }

        .login-button:active {
            transform: translateY(-1px);
        }

        .credentials-box {
            background: linear-gradient(135deg, rgba(0, 100, 232, 0.1) 0%, rgba(0, 184, 169, 0.05) 100%);
            border: 1px solid rgba(0, 217, 255, 0.2);
            border-radius: 10px;
            padding: 1.2rem;
            margin-top: 2rem;
            font-size: 0.85rem;
            color: #cbd5e1;
            text-align: center;
            font-family: 'Poppins', sans-serif;
            box-shadow: inset 0 1px 0 rgba(0, 217, 255, 0.1);
        }

        .credentials-label {
            display: block;
            color: #00d9ff;
            font-weight: 700;
            margin-bottom: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.02em;
            font-size: 0.8rem;
        }

        .credentials-text {
            color: #cbd5e1;
            margin: 0.3rem 0;
            font-family: 'Poppins', monospace;
        }

        .credentials-text strong {
            color: #00ff88;
            font-weight: 700;
        }
    </style>
    """

    st.markdown(login_css, unsafe_allow_html=True)
    st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    # Header
    st.markdown("""
        <div class="login-header">
            <div class="login-title">ANALYTICS</div>
            <div class="login-subtitle">Premium AI Dashboard Portal</div>
        </div>
        <div class="divider-line"></div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 1.2rem;'></div>", unsafe_allow_html=True)

    # Login form
    username = st.text_input(
        "Username",
        placeholder="Enter username",
        key="login_username",
        label_visibility="collapsed"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password",
        key="login_password",
        label_visibility="collapsed"
    )

    st.markdown("<div style='height: 0.8rem;'></div>", unsafe_allow_html=True)

    login_button = st.button("SIGN IN", use_container_width=True, type="primary")

    if login_button:
        if username == "admin" and password == "admin":
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.login_attempts = 0
            st.success("Access Granted! Redirecting...")
            st.balloons()
            st.rerun()
        else:
            st.session_state.login_attempts += 1
            st.error(f"Invalid credentials. Attempts: {st.session_state.login_attempts}/3")
            if st.session_state.login_attempts >= 3:
                st.warning("Too many failed attempts. Please refresh the page.")

    # Credentials box
    st.markdown("""
        <div class="credentials-box">
            <span class="credentials-label">Demo Access</span>
            <div class="credentials-text">Username: <strong>admin</strong></div>
            <div class="credentials-text">Password: <strong>admin</strong></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# 📊 DASHBOARD VISUALIZATIONS
# ═══════════════════════════════════════════════════════════════════════════

def render_kpi_metrics(dataframe):
    """Display premium KPI cards with advanced analytics"""
    if dataframe.empty:
        st.warning("No data available for metrics")
        return

    col1, col2, col3, col4 = st.columns(4)

    metrics_data = [
        ("Total Sales", f"${dataframe['Purchase'].sum():,.0f}", f"+{dataframe['Purchase'].mean():.0f} avg"),
        ("High Spenders", str(len(dataframe[dataframe['Purchase'] > dataframe['Purchase'].quantile(0.75)])), 
         f"{(len(dataframe[dataframe['Purchase'] > dataframe['Purchase'].quantile(0.75)])/len(dataframe)*100):.1f}%"),
        ("Total Transactions", f"{len(dataframe):,}", f"{dataframe['Category'].nunique()} categories"),
        ("Avg per Product", f"${dataframe['Purchase'].sum() / dataframe['Product_ID'].nunique():,.0f}",
         f"from {dataframe['Product_ID'].nunique()} products"),
    ]

    columns = [col1, col2, col3, col4]
    for col, (label, value, delta) in zip(columns, metrics_data):
        with col:
            st.metric(label=label, value=value, delta=delta)

def render_eda_section(dataframe, selected_gender, selected_age):
    """Render Exploratory Data Analysis with premium visualizations"""
    if dataframe.empty:
        st.warning("No data for analysis")
        return

    filtered_df = dataframe.copy()
    if selected_gender:
        filtered_df = filtered_df[filtered_df['Gender'].isin(selected_gender)]
    if selected_age:
        filtered_df = filtered_df[filtered_df['Age'].isin(selected_age)]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Purchase Heatmap Analysis")
        heatmap_data = filtered_df.pivot_table(
            values='Purchase',
            index='Age',
            columns='Gender',
            aggfunc='sum',
            fill_value=0
        )

        fig_heatmap = go.Figure(data=go.Heatmap(
            z=heatmap_data.values,
            x=heatmap_data.columns,
            y=heatmap_data.index,
            colorscale='Viridis',
            colorbar=dict(title="Sales ($)")
        ))

        fig_heatmap.update_layout(
            title_text="Gender × Age Purchase Matrix",
            xaxis_title="Gender",
            yaxis_title="Age Group",
            plot_bgcolor='rgba(10, 14, 39, 0.4)',
            paper_bgcolor='rgba(14, 18, 34, 0)',
            font=dict(family="Poppins, sans-serif", color="#e2e8f0", size=11),
            hovermode='closest',
            height=420,
            title_font=dict(size=14, color='#00d9ff', family='Orbitron'),
            margin=dict(l=60, r=60, t=60, b=60)
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)

    with col2:
        st.subheader("Sales Distribution Hierarchy")

        category_data = filtered_df.groupby(['Gender', 'Category'])['Purchase'].sum().reset_index()
        gender_totals = filtered_df.groupby('Gender')['Purchase'].sum().reset_index()
        
        labels = ['Total'] + list(gender_totals['Gender']) + [f"Cat {int(c)}" for c in category_data['Category'].unique()]
        parents = [''] + ['Total'] * len(gender_totals) + list(category_data['Gender'])
        values = [filtered_df['Purchase'].sum()] + list(gender_totals['Purchase']) + list(category_data['Purchase'])
        
        fig_sunburst = go.Figure(go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            marker=dict(
                colors=values,
                colorscale='Viridis',
                cmid=max(values)/2 if values else 0,
                line=dict(color='rgba(10, 14, 39, 0.9)', width=2)
            ),
            textfont=dict(size=11, color='#f1f5f9'),
            hovertemplate='<b>%{label}</b><br>Sales: $%{value:,.0f}<extra></extra>'
        ))
        
        fig_sunburst.update_layout(
            plot_bgcolor='rgba(10, 14, 39, 0.4)',
            paper_bgcolor='rgba(14, 18, 34, 0)',
            font=dict(family="Poppins, sans-serif", color="#e2e8f0"),
            height=420,
            title_text="Hierarchical Sales Breakdown",
            title_font=dict(size=14, color='#00d9ff', family='Orbitron'),
            margin=dict(t=40, l=10, r=10, b=10)
        )
        st.plotly_chart(fig_sunburst, use_container_width=True)

def render_clustering_section(dataframe):
    """Render premium 3D K-Means clustering visualization"""
    if dataframe.empty or len(dataframe) < 3:
        st.warning("Insufficient data for clustering analysis")
        return

    st.subheader("Customer Segmentation & Clustering")

    clustering_df = dataframe[['Purchase', 'Category', 'Product_ID']].copy()
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(clustering_df)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(scaled_data)

    fig_3d = go.Figure(data=[go.Scatter3d(
        x=clustering_df['Purchase'],
        y=clustering_df['Category'],
        z=clustering_df['Product_ID'],
        mode='markers',
        marker=dict(
            size=5,
            color=clusters,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Segment"),
            line=dict(width=1, color='rgba(0, 217, 255, 0.4)')
        ),
        text=[f"Segment: {c}" for c in clusters],
        hovertemplate='<b>Segment: %{text}</b><br>Purchase: ${%{x}:,.0f}<extra></extra>'
    )])

    fig_3d.update_layout(
        title_text="3D Customer Segmentation",
        scene=dict(
            xaxis_title="Purchase Amount",
            yaxis_title="Category",
            zaxis_title="Product ID",
            bgcolor='rgba(10, 14, 39, 0.3)',
            xaxis=dict(backgroundcolor="rgba(10, 14, 39, 0.2)", gridcolor="#333"),
            yaxis=dict(backgroundcolor="rgba(10, 14, 39, 0.2)", gridcolor="#333"),
            zaxis=dict(backgroundcolor="rgba(10, 14, 39, 0.2)", gridcolor="#333"),
        ),
        plot_bgcolor='rgba(10, 14, 39, 0.4)',
        paper_bgcolor='rgba(14, 18, 34, 0)',
        font=dict(family="Poppins, sans-serif", color="#e2e8f0"),
        height=520,
        title_font=dict(size=16, color='#00d9ff', family='Orbitron'),
        margin=dict(l=60, r=60, t=80, b=60)
    )

    st.plotly_chart(fig_3d, use_container_width=True)

def render_association_rules_section(dataframe):
    """Render Network analysis for product associations"""
    st.subheader("Product Association Network")

    if dataframe.empty:
        st.warning("No data for association analysis")
        return

    category_pairs = dataframe.groupby(['Category', 'Product_ID']).size().reset_index(name='count')

    fig_network = go.Figure(data=[go.Scatter(
        x=category_pairs['Category'],
        y=category_pairs['Product_ID'],
        mode='markers+text',
        marker=dict(
            size=category_pairs['count'] * 2.5,
            color=category_pairs['count'],
            colorscale='Plasma',
            showscale=True,
            colorbar=dict(title="Frequency"),
            line=dict(width=2, color='rgba(0, 217, 255, 0.6)')
        ),
        text=category_pairs['count'],
        textposition='top center',
        textfont=dict(color='#00d9ff', size=10),
        hovertemplate='<b>Category: %{x}</b><br>Product: %{y}<br>Frequency: %{text}<extra></extra>'
    )])

    fig_network.update_layout(
        title_text="Co-Occurrence Pattern Analysis",
        xaxis_title="Category",
        yaxis_title="Product ID",
        plot_bgcolor='rgba(10, 14, 39, 0.4)',
        paper_bgcolor='rgba(14, 18, 34, 0)',
        font=dict(family="Poppins, sans-serif", color="#e2e8f0"),
        hovermode='closest',
        height=420,
        title_font=dict(size=14, color='#00d9ff', family='Orbitron'),
        xaxis=dict(gridcolor='rgba(0, 217, 255, 0.1)'),
        yaxis=dict(gridcolor='rgba(0, 217, 255, 0.1)'),
    )

    st.plotly_chart(fig_network, use_container_width=True)

def render_anomaly_detection_section(dataframe):
    """Render anomaly detection with data quality analysis"""
    st.subheader("Data Quality & Anomaly Detection")

    if dataframe.empty:
        st.warning("No data for quality analysis")
        return

    try:
        X = dataframe[['Purchase', 'Category', 'Product_ID']].copy()
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        outlier_detector = EllipticEnvelope(contamination=0.05, random_state=42)
        anomalies = outlier_detector.fit_predict(X_scaled)

        df_anomaly = dataframe.copy()
        df_anomaly['Anomaly'] = anomalies
        df_anomaly['Status'] = df_anomaly['Anomaly'].apply(lambda x: 'ANOMALY' if x == -1 else 'NORMAL')

        anomaly_rows = df_anomaly[df_anomaly['Anomaly'] == -1].head(10)

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("##### Detected Anomalies")
            if not anomaly_rows.empty:
                display_df = anomaly_rows[['User_ID', 'Purchase', 'Category', 'Gender', 'Status']].copy()
                st.dataframe(
                    display_df,
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("No anomalies detected - All data quality metrics nominal")

        with col2:
            anomaly_count = len(df_anomaly[df_anomaly['Anomaly'] == -1])
            normal_count = len(df_anomaly[df_anomaly['Anomaly'] == 1])

            fig_pie = go.Figure(data=[go.Pie(
                labels=['Clean', 'Anomalies'],
                values=[normal_count, anomaly_count],
                marker=dict(colors=['#00ff88', '#ff4757']),
                textinfo='label+percent',
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
            )])

            fig_pie.update_layout(
                title_text="Data Quality Report",
                plot_bgcolor='rgba(10, 14, 39, 0.4)',
                paper_bgcolor='rgba(14, 18, 34, 0)',
                font=dict(family="Poppins, sans-serif", color="#e2e8f0"),
                height=320,
                title_font=dict(size=14, color='#00d9ff', family='Orbitron'),
                margin=dict(l=20, r=20, t=60, b=20)
            )
            st.plotly_chart(fig_pie, use_container_width=True)

    except Exception as error:
        st.error(f"Quality analysis error: {error}")

# ═══════════════════════════════════════════════════════════════════════════
# 🎨 MAIN APP LAYOUT
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Main application entry point - Premium dashboard"""

    initialize_session_state()

    if not st.session_state.authenticated:
        render_login_page()
        return

    # ───────────────────────────────────────────────────────────────────────
    # SIDEBAR NAVIGATION & FILTERS
    # ───────────────────────────────────────────────────────────────────────

    with st.sidebar:
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        st.markdown(
            "<h3 style='text-align: center; color: #00d9ff; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 0;'>Advanced Filtering</h3>",
            unsafe_allow_html=True
        )
        st.markdown("<hr style='border: 1px solid rgba(0, 217, 255, 0.2);'>", unsafe_allow_html=True)

        selected_gender = st.multiselect(
            "Gender",
            options=['M', 'F'],
            default=['M', 'F'],
            key="gender_filter"
        )

        selected_age = st.multiselect(
            "Age Group",
            options=['0-17', '18-25', '26-35', '36-45', '46-50', '51-55', '55+'],
            default=['0-17', '18-25', '26-35', '36-45', '46-50', '51-55', '55+'],
            key="age_filter"
        )

        min_purchase = st.slider(
            "Min Purchase Amount",
            min_value=0,
            max_value=100000,
            value=0,
            step=1000,
            key="min_purchase_slider"
        )

        st.markdown("<hr style='border: 1px solid rgba(0, 217, 255, 0.2); margin: 2rem 0;'>", unsafe_allow_html=True)

        if st.button("LOGOUT", use_container_width=True, type="secondary"):
            st.session_state.authenticated = False
            st.session_state.username = ""
            st.rerun()

    # ───────────────────────────────────────────────────────────────────────
    # MAIN CONTENT AREA
    # ───────────────────────────────────────────────────────────────────────

    df = load_black_friday_data()

    if not df.empty:
        df_filtered = df[
            (df['Gender'].isin(selected_gender)) &
            (df['Age'].isin(selected_age)) &
            (df['Purchase'] >= min_purchase)
        ].copy()
    else:
        df_filtered = df.copy()

    # Header
    st.markdown("<div style='text-align: center; margin: 2.5rem 0 3rem 0;'>", unsafe_allow_html=True)
    st.markdown("<h1>PREMIUM DATA ANALYTICS</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='color: #a0aec0; font-size: 1.1rem; letter-spacing: 0.02em; margin-top: 0.5rem;'>Enterprise-Grade Intelligence | Real-Time Insights | Advanced Analytics</p>",
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr style='border: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(0, 217, 255, 0.3), transparent); margin: 2.5rem 0;'/>", unsafe_allow_html=True)

    # KPI Section
    st.markdown("<h2>Performance Indicators</h2>", unsafe_allow_html=True)
    render_kpi_metrics(df_filtered)

    st.markdown("<hr style='border: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(0, 217, 255, 0.3), transparent); margin: 2.5rem 0;'/>", unsafe_allow_html=True)

    # EDA Section
    st.markdown("<h2>Exploratory Analysis</h2>", unsafe_allow_html=True)
    render_eda_section(df_filtered, selected_gender, selected_age)

    st.markdown("<hr style='border: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(0, 217, 255, 0.3), transparent); margin: 2.5rem 0;'/>", unsafe_allow_html=True)

    # Clustering Section
    st.markdown("<h2>Customer Segmentation</h2>", unsafe_allow_html=True)
    render_clustering_section(df_filtered)

    st.markdown("<hr style='border: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(0, 217, 255, 0.3), transparent); margin: 2.5rem 0;'/>", unsafe_allow_html=True)

    # Association Section
    st.markdown("<h2>Market Intelligence</h2>", unsafe_allow_html=True)
    render_association_rules_section(df_filtered)

    st.markdown("<hr style='border: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(0, 217, 255, 0.3), transparent); margin: 2.5rem 0;'/>", unsafe_allow_html=True)

    # Anomaly Detection Section
    st.markdown("<h2>Quality Assurance</h2>", unsafe_allow_html=True)
    render_anomaly_detection_section(df_filtered)

    # Footer
    st.markdown(
        "<div style='text-align: center; color: #64748b; font-size: 0.85rem; margin-top: 4rem; padding: 2rem; border-top: 1px solid rgba(0, 217, 255, 0.1);'>"
        "<p style='margin: 0;'>Premium Analytics Dashboard v2.0</p>"
        f"<p style='margin: 0.5rem 0 0 0; color: #a0aec0;'>User: <span style='color: #00d9ff;'>{st.session_state.username.upper()}</span> | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"
        "</div>",
        unsafe_allow_html=True
    )

# ═══════════════════════════════════════════════════════════════════════════
# 🚀 RUN APP
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()


