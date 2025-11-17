import streamlit as st

def build_sidebar():
    wg = st.sidebar.selectbox("Waveguide Type", ["TEM", "Rectangular", "Circular"])
    mode = st.sidebar.radio("Mode", ["TE", "TM"])
    return wg, mode
