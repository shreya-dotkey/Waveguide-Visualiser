import streamlit as st

from waveguides.tem import handleTEM
from waveguides.rectangular import handleRectangular
from waveguides.circular import handleCircular

st.set_page_config(page_title="Waveguide Field Visualizer", layout="wide")

wg_type = st.sidebar.selectbox("Waveguide Type", ["TEM", "Rectangular", "Circular"])
mode = st.sidebar.radio("Mode", ["TE", "TM"])

if wg_type == "TEM":
    handleTEM()

elif wg_type == "Rectangular":
    m = st.sidebar.slider("m", 0, 5, 1)
    n = st.sidebar.slider("n", 0, 5, 1)
    A = st.sidebar.slider("a (width)", 1, 20, 10)
    B = st.sidebar.slider("b (height)", 1, 20, 5)
    handleRectangular(m, n, A, B, mode)

elif wg_type == "Circular":
    n = st.sidebar.slider("n", 0, 5, 1)
    m = st.sidebar.slider("m", 1, 5, 1)
    R = st.sidebar.slider("R (radius)", 1, 10, 5)
    handleCircular(n, m, R, mode)

