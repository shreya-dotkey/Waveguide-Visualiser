import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.constants import pi

def handleTEM():
    r = np.linspace(1, 5, 101)
    t = np.linspace(0, 2*pi, 101)
    T, RAD = np.meshgrid(t, r)

    U = 10 / RAD
    V = T * 0

    col1, col2 = st.columns(2)

    with col1:
        fig = plt.figure(figsize=(4,4))
        plt.streamplot(T, RAD, V, U)
        st.pyplot(fig)
        plt.close(fig)

    with col2:
        fig = plt.figure(figsize=(4,4))
        plt.streamplot(T, RAD, RAD*0, RAD*0 + 1)
        st.pyplot(fig)
        plt.close(fig)
