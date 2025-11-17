import streamlit as st

def apply_layout(title, subtitle):
    st.markdown(f"<h1 style='text-align:center;'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;'>{subtitle}</h3>", unsafe_allow_html=True)
