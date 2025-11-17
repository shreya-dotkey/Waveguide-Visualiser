import numpy as np
import io
from PIL import Image
import matplotlib.pyplot as plt

def polar_to_cartesian(Er, Etheta, theta):
    Ex = Er * np.cos(theta) - Etheta * np.sin(theta)
    Ey = Er * np.sin(theta) + Etheta * np.cos(theta)
    return Ex, Ey

def fig_to_array(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return Image.open(buf)

def streamplot_on_axis(ax, X, Y, U, V, R, density=1.2, color="blue"):
    mask = (X**2 + Y**2) <= R**2
    U = np.ma.array(U, mask=~mask)
    V = np.ma.array(V, mask=~mask)
    ax.streamplot(X, Y, U, V, color=color, density=density, linewidth=1)
    circle = plt.Circle((0,0), R, color="k", fill=False, linewidth=2)
    ax.add_patch(circle)
    ax.set_aspect("equal")
    ax.set_xlim(-R, R)
    ax.set_ylim(-R, R)
    ax.axis("off")

