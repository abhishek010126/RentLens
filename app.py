import streamlit as st
import pandas as pd
from frontend.Dashboard import dash
from frontend.find import find
from frontend.analyze import analysis
from frontend.copilot import property_copilot
from frontend.login import login_page
from frontend.styles import apply_custom_styles
from frontend.about import about
from frontend.capareui import compare

st.set_page_config(
    page_title="RentLens",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_custom_styles()

st.sidebar.title("🏠 RentLens")




if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if st.sidebar.button(" 📊 Dashboard", width=200):
    st.session_state.page = "Dashboard"

if st.sidebar.button(" 📝 Analyze Property", width=200):
    st.session_state.page = " 📝 Analyze Property"

if st.sidebar.button("🔍 Find Property", width=200):
    st.session_state.page = "🔍 Find Property"


if st.sidebar.button("🧠 Property Copilot", width=200):
    st.session_state.page = "🧠 Property Copilot"

st.sidebar.markdown(
        "<div style='height: 19vh;'></div>",
        unsafe_allow_html=True
    )

st.sidebar.divider()

if st.sidebar.button("ℹ️ About", width=200):
    st.session_state.page = "About"

if st.sidebar.button("🔐 Login", width=200):
    st.session_state.page = "login"




# Display selected page

if st.session_state.page == "Dashboard":
    st.title("📊 Dashboard")
    dash()
    
elif st.session_state.page == " 📝 Analyze Property":
    st.title("📝 Analyze Property")
    analysis()


elif st.session_state.page == "🧠 Property Copilot":
    st.title("🧠 Property Copilot")
    property_copilot()

elif st.session_state.page == "🔍 Find Property":
    st.title("🔍 Find Property")

    find()
elif st.session_state.page == "login":
    login_page()

elif st.session_state.page == "About":
    about()

elif st.session_state.page == "Compare":
    compare()