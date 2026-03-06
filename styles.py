# =================================================================
# Project: The Brain Budget (Digital Habit Calculator)
# Core Engine: NeuroTwin™ Technology
# Author: Saurav R. Phadnis
# Affiliation: MIT World Peace University (WPU), Pune, India
# License: MIT Open-Source Template
# Date: 2026
# =================================================================

import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* Main Background */
        .stApp {
            background-color: #0e1117;
            background-image: linear-gradient(315deg, #0e1117 0%, #1a1c23 74%);
        }
        
        /* Glassmorphism Cards */
        .stMetric, .stDataFrame, .stChart {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #00e5ff !important;
            font-family: 'Segoe UI', sans-serif;
            font-weight: 700;
        }
        
        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
            color: black;
            font-weight: bold;
            border: none;
            border-radius: 20px;
            height: 50px;
            width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)