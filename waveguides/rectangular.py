import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.constants import mu_0, epsilon_0, pi

class TE_TM_Functions:
    def __init__(self, m, n, a, b):
        self.m, self.n, self.a, self.b = m, n, a, b
        self.f = 2 * self.Fc()
        self.w = 2 * pi * self.f

    def Kc(self):
        return np.sqrt((self.m*pi/self.a)**2 + (self.n*pi/self.b)**2)

    def Fc(self):
        return (1/(2*np.sqrt(mu_0*epsilon_0))) * \
               np.sqrt((self.m/self.a)**2 + (self.n/self.b)**2)

    def beta_g(self):
        fc = self.Fc()
        return self.w*np.sqrt(mu_0*epsilon_0)*np.sqrt(1-(fc/self.f)**2)

    def v_G(self):
        return self.w / self.beta_g()

    def Z_in(self):
        return np.sqrt(mu_0/epsilon_0)

    def Z_G_TE(self):
        return self.Z_in()/np.sqrt(1-(self.Fc()/self.f)**2)

    def lambda_G(self):
        return 2*pi/self.beta_g()

    def Z_G_TM(self):
        return self.Z_in()*np.sqrt(1-(self.Fc()/self.f)**2)


def handleRectangular(m, n, A, B, mode="TE"):
    x = np.linspace(0, A, 101)
    y = np.linspace(0, B, 101)
    X, Y = np.meshgrid(x, y)

    st.image("assets/rectangular.png", use_container_width=True)
    st.markdown(f"<h3 style='text-align:center'>{mode}{m}{n} Rectangular Mode</h3>", unsafe_allow_html=True)

    if mode == "TE":
        u = np.cos(m*pi/A * X)*np.sin(n*pi/B * Y)
        v = -np.sin(m*pi/A * X)*np.cos(n*pi/B * Y)
    else:
        u = np.cos(m*pi/A * X)*np.sin(n*pi/B * Y)
        v =  np.sin(m*pi/A * X)*np.cos(n*pi/B * Y)

    col1, col2 = st.columns(2)

    with col1:
        fig = plt.figure(figsize=(5,5))
        plt.streamplot(x, y, u, v)
        plt.xlim(0, A); plt.ylim(0, B)
        st.pyplot(fig); plt.close(fig)

    with col2:
        fig = plt.figure(figsize=(5,5))
        plt.streamplot(x, y, -v, u)
        plt.xlim(0, A); plt.ylim(0, B)
        st.pyplot(fig); plt.close(fig)
