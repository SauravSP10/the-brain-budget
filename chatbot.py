# =================================================================
# Project: The Brain Budget (Digital Habit Calculator)
# Core Engine: NeuroTwin™ Technology
# Author: Saurav R. Phadnis
# Affiliation: MIT World Peace University (WPU), Pune, India
# License: MIT Open-Source Template
# Date: 2026
# =================================================================

import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def render_chatbot():
    st.markdown("### 💬 Chat with your Advisor")
    
    # Initialize Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input Field
    if prompt := st.chat_input("Ask me about dopamine detox..."):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate AI Response
        with st.chat_message("assistant"):
            try:
                llm = OllamaLLM(model="llama3.2")
                # Simple chat chain
                response = llm.invoke(prompt)
                st.markdown(response)
                # Add AI message to history
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"AI Error: {e}")