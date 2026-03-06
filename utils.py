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

# Safe Import for LangChain Community Tools
try:
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_community.vectorstores.faiss import FAISS
    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False

def load_knowledge_base(pdf_path):
    """
    Loads the research PDF if available.
    """
    if not LANGCHAIN_AVAILABLE:
        return "⚠️ LangChain libraries missing. Running in basic mode."
        
    if not os.path.exists(pdf_path):
        return None # No file found
    
    try:
        loader = PyPDFLoader(pdf_path)
        pages = loader.load_and_split()
        return f"✅ Loaded {len(pages)} pages of research."
    except Exception as e:
        return f"❌ Error loading PDF: {str(e)}"