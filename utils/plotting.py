import matplotlib.pyplot as plt
import numpy as np

def create_streamplot(x, y, U, V, title=None):
    """
    Create a simple Matplotlib streamplot and return the figure.
    """
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.streamplot(x, y, U, V)
    ax.set_aspect('equal')

    if title:
        ax.set_title(title)

    return fig

