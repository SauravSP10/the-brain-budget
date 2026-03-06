# =================================================================
# Project: The Brain Budget (Digital Habit Calculator)
# Core Engine: NeuroTwin™ Technology
# Author: Saurav R. Phadnis
# Affiliation: MIT World Peace University (WPU), Pune, India
# License: MIT Open-Source Template
# Date: 2026
# =================================================================

import os
import streamlit as st
import numpy as np

# --- 🚨 PYTHON 3.13 COMPATIBILITY PATCH 🚨 ---
try:
    if not hasattr(np, 'byte'): np.byte = np.int8
    if not hasattr(np, 'bool'): np.bool = bool
    if not hasattr(np, 'int'): np.int = int
    if not hasattr(np, 'float'): np.float = float
except:
    pass
# ---------------------------------------------

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="The Brain Budget", layout="wide", page_icon="🧠")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .stProgress > div > div > div > div { background-color: #00e5ff; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2043/2043217.png", width=80)
    st.title("💰 The Brain Budget")
    st.caption("Calculate Your Cognitive Currency")
    st.markdown("---")
    st.sidebar.markdown("---")
    st.sidebar.write("🚀 **Developed at MIT WPU, Pune**")
    st.sidebar.caption("Powered by NeuroTwin™ Engine")
    st.sidebar.write("© 2026 Saurav R. Phadnis")

    # 1. BIOLOGY
    st.header("🧬 1. Biology")
    age = st.slider("Age", 10, 80, 24)
    sleep = st.slider("Sleep (Hrs)", 3, 12, 6, help="Deep sleep cleanses 'Amyloid Plaques'.")
    sunlight = st.select_slider("Morning Sunlight", options=["None", "5 mins", "15+ mins"], help="Sets Circadian Rhythm.")
    
    # 2. DIGITAL LOAD
    st.header("📱 2. Digital Load")
    work_hours = st.slider("Work Screen Time", 0, 12, 8, help="Forced usage (Excel, Coding).")
    leisure_hours = st.slider("Leisure Scrolling", 0, 8, 3, help="TikTok, Reels, Games. High Dopamine spike.")
    
    # 3. LIFESTYLE
    st.header("🛡️ 3. Buffs & Debuffs")
    exercise = st.selectbox("Movement", ["Sedentary", "Walking", "Gym/Athlete"], help="Increases BDNF.")
    social = st.radio("Real Human Contact", ["Low (Digital Only)", "High (In-Person)"], help="Oxytocin protects neurons.")
    multitasking = st.checkbox("Chronic Multitasking?", help="Watching TV + Scrolling Phone.")

    if st.button("RUN ANALYSIS", type="primary"):
        st.session_state['run'] = True

# --- LOGIC ENGINE ---
def calculate_brain_health(w_hours, l_hours, sleep, sun, move, social, multi):
    health = 100
    health -= (l_hours * 8)
    health -= (w_hours * 2)
    if sleep < 7: health -= ((7 - sleep) * 10)
    if multi: health -= 15
    if social == "Low (Digital Only)": health -= 10
    
    if move == "Gym/Athlete": health += 15
    elif move == "Walking": health += 5
    if sun == "15+ mins": health += 10
    
    return max(0, min(health, 100))

# --- MAIN PAGE ---
st.title("⚖️ The Brain Budget: A Digital Habit Calculator")
st.markdown("Are you spending more focus than you're earning?")

# ➤ ADDED THE 4TH TAB HERE
tab1, tab2, tab3, tab4 = st.tabs(["📉 Expense Report", "🔮 Budget Planner", "👨‍⚕️ Audit Report", "💬 Help Desk"])

# --- SHARED CALCULATIONS ---
brain_score = calculate_brain_health(work_hours, leisure_hours, sleep, sunlight, exercise, social, multitasking)
dopamine_level = (leisure_hours * 10) + (20 if multitasking else 0)
burnout_level = (work_hours * 8) + ((8-sleep) * 5)

if st.session_state.get('run'):
    
    # --- TAB 1: VISUALS ---
    with tab1:
        c1, c2, c3 = st.columns(3)
        with c1:
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number", value = brain_score, title = {'text': "Brain Battery %"},
                gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#00e5ff"},
                         'steps': [{'range': [0, 50], 'color': "#330000"}],
                         'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}}))
            st.plotly_chart(fig_gauge, use_container_width=True)
        
        with c2:
            st.subheader("🧪 Dopamine Bucket")
            st.progress(min(dopamine_level, 100) / 100)
            st.caption(f"{dopamine_level}% Full (High = Numbness)")
            
        with c3:
            st.subheader("🔥 Burnout Meter")
            st.progress(min(burnout_level, 100) / 100)
            st.caption(f"{burnout_level}% Risk (High = Fatigue)")

        st.markdown("---")
        st.subheader("📉 What is draining you?")
        impact_data = pd.DataFrame({
            'Factor': ['Leisure Scrolling', 'Work Fatigue', 'Sleep Deprivation', 'Multitasking', 'Exercise (Recovery)'],
            'Impact': [- (leisure_hours * 8), - (work_hours * 2), - ((7-sleep)*10 if sleep < 7 else 0), -15 if multitasking else 0, 15 if exercise == "Gym/Athlete" else 0]
        })
        fig_bar = px.bar(impact_data, x='Factor', y='Impact', color='Impact', color_continuous_scale='RdYlGn')
        st.plotly_chart(fig_bar, use_container_width=True)

    # --- TAB 2: SIMULATOR ---
    with tab2:
        st.header("🔮 The Prediction Engine")
        c1, c2 = st.columns(2)
        with c1:
            new_leisure = st.slider("👇 Reduce Scrolling to:", 0, 8, leisure_hours)
            new_sleep = st.slider("👇 Increase Sleep to:", 3, 12, sleep)
            new_exercise = st.selectbox("👇 Start Exercising:", ["Sedentary", "Walking", "Gym/Athlete"], index=0)
        
        with c2:
            new_score = calculate_brain_health(work_hours, new_leisure, new_sleep, sunlight, new_exercise, social, multitasking)
            diff = new_score - brain_score
            st.metric("Projected Brain Health", f"{new_score}/100", f"{'+' if diff > 0 else ''}{diff} pts")
            if new_score > 80: st.success("🎉 HEALTHY ZONE REACHED!")

    # --- TAB 3: AI ANALYSIS ---
    with tab3:
        st.header("Dr. Neuro Analysis")
        if st.button("Generate Detailed Report"):
            try:
                from doctor_brain import get_medical_advice
                with st.spinner("Analyzing..."):
                    advice = get_medical_advice(work_hours, leisure_hours, sleep, exercise, dopamine_level, brain_score)
                    st.markdown(advice)
            except Exception as e:
                st.error(f"AI Error: {e}")

# --- TAB 4: CHATBOT (RESTORED!) ---
with tab4:
    try:
        from chatbot import render_chatbot
        render_chatbot()
    except Exception as e:
        st.warning("Chatbot is offline. Make sure 'chatbot.py' is in the folder.")
        st.error(e)