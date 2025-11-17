import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import streamlit as st

from utils.helpers import polar_to_cartesian, streamplot_on_axis, fig_to_array

def circular_mode_fields(n, m, R, mode="TE", grid_N=151):
    if mode == "TM":
        root = special.jn_zeros(n, m)[-1]
    else:
        root = special.jnp_zeros(n, m)[-1]

    k_c = root / R
    x = np.linspace(-R, R, grid_N)
    y = np.linspace(-R, R, grid_N)
    X, Y = np.meshgrid(x, y)
    r = np.sqrt(X**2 + Y**2)
    theta = np.arctan2(Y, X)
    r_safe = np.where(r == 0, 1e-12, r)

    angfun = np.cos(n*theta)
    d_angfun = -n*np.sin(n*theta)

    if mode == "TM":
        Ez = special.jv(n, k_c*r) * angfun
        Er = -k_c * special.jvp(n, k_c*r) * angfun
        Etheta = -(1/r_safe) * special.jv(n, k_c*r) * d_angfun
        Ex, Ey = polar_to_cartesian(Er, Etheta, theta)

        Hr = (1/r_safe) * special.jv(n, k_c*r) * d_angfun
        Htheta = -k_c * special.jvp(n, k_c*r) * angfun
        Hx, Hy = polar_to_cartesian(Hr, Htheta, theta)
        Hz = np.zeros_like(Ez)

    else:
        Hz = special.jv(n, k_c*r) * angfun
        Hr = k_c * special.jvp(n, k_c*r) * angfun
        Htheta = (1/r_safe) * special.jv(n, k_c*r) * d_angfun
        Hx, Hy = polar_to_cartesian(Hr, Htheta, theta)

        Er = -(1/r_safe) * special.jv(n, k_c*r) * d_angfun
        Etheta = k_c * special.jvp(n, k_c*r) * angfun
        Ex, Ey = polar_to_cartesian(Er, Etheta, theta)
        Ez = np.zeros_like(Hz)

    return X, Y, Ex, Ey, Ez, Hx, Hy, Hz, {
        "n": n, "m": m, "R": R, "k_c": k_c, "root": root
    }


def handleCircular(n, m, R, mode="TE", density=1.2):
    X, Y, Ex, Ey, Ez, Hx, Hy, Hz, params = circular_mode_fields(n, m, R, mode)

    st.image("assets/circular.png", use_container_width=True)
    st.markdown(f"<h3 style='text-align:center'>{mode}{n}{m} Circular Mode</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        figE, axE = plt.subplots(figsize=(4,4))
        streamplot_on_axis(axE, X, Y, Ex, Ey, R, density=density)
        st.image(fig_to_array(figE))
        plt.close(figE)

    with col2:
        figH, axH = plt.subplots(figsize=(4,4))
        streamplot_on_axis(axH, X, Y, Hx, Hy, R, density=density)
        st.image(fig_to_array(figH))
        plt.close(figH)

    st.table(params)
