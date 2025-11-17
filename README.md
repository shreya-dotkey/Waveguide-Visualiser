# Waveguide-Visualiser
A lightweight, interactive Streamlit app for visualizing electromagnetic field patterns inside TEM, Rectangular (TE/TM), and Circular (TE/TM) waveguides.
It’s designed to be simple, clean, and fast: no animations, no heavy UI, just real-time field plots based on the modes you choose.

✨ Features
📡 Waveguide Types

TEM Mode
Simple visual representation of E and H fields in a coaxial-like geometry.

Rectangular Waveguide (TE/TM)
Visualizes field patterns for any (m, n) mode using streamplots.

Circular Waveguide (TE/TM)
Computes patterns using Bessel function roots and displays the corresponding E/H fields.

⚡ Real-time Visualization

Adjust mode indices and geometry in the sidebar and see the fields update instantly.

🎯 Minimal, student-friendly UI

No distractions — just sliders and clean plots.

🖼️ Preview

(Add screenshots or GIFs here)

/screenshots
    ├── rectangular.png
    ├── circular.png
    └── tem.png

🛠️ Tech Stack

Python 3.10+

Streamlit — UI framework

NumPy — numerical math

SciPy — Bessel functions (circular waveguide modes)

Matplotlib — plotting engine

📦 Installation

Clone the repo:

git clone https://github.com/yourusername/waveguide-visualizer
cd waveguide-visualizer


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run waveguide_app.py

📄 requirements.txt
streamlit
numpy
scipy
matplotlib
pandas

🚀 Deployment Options
1️⃣ Streamlit Cloud (easiest)

Push your code to GitHub

Go to https://share.streamlit.io

Deploy the repo

Choose waveguide_app.py as the entry point

Your app is instantly live.

2️⃣ Render.com

Supports long-running Python web apps.
Start command:

streamlit run waveguide_app.py --server.port $PORT --server.address 0.0.0.0

3️⃣ HuggingFace Spaces

Select Streamlit as the space template and upload your code.

📘 About This Project

I built this tool because plotting waveguide modes manually is tedious and the existing online visualizers are often too slow or too complicated.
This app aims to be:

simple enough for students,

accurate enough for assignments, and

clean enough for quick conceptual visualization.

If you find it useful or want more modes/features, feel free to open an issue or PR!
