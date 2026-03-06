# =================================================================
# Project: The Brain Budget (Digital Habit Calculator)
# Core Engine: NeuroTwin™ Technology
# Author: Saurav R. Phadnis
# Affiliation: MIT World Peace University (WPU), Pune, India
# License: MIT Open-Source Template
# Date: 2026
# =================================================================

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def get_medical_advice(work_hours, leisure_hours, sleep, exercise, dopamine_level, brain_score):
    try:
        llm = OllamaLLM(model="llama3.2")
        
        template = """
You are the 'Brain Budget Auditor'. 
Your job is to look at a user's mental 'spending' (screens) and 'income' (sleep/exercise).

User Audit Data:
- Fixed Expenses (Work): {work_hours} hrs
- Luxury Spending (Leisure): {leisure_hours} hrs
- Savings/Recovery (Sleep): {sleep} hrs
- Investment (Exercise): {exercise}

Task:
1. **The Audit**: Tell them if they are in 'Cognitive Debt' (Negative balance).
2. **The Interest Rate**: Explain how scrolling is like 'High-Interest Debt'—it feels good now but costs double later in brain fog.
3. **The Savings Plan**: Give 3 steps to increase their 'Mental Net Worth'.
   
Tone: Professional, direct, and uses financial metaphors (Debt, Savings, Investment). 📈
"""
        
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | llm
        response = chain.invoke({
            "work_hours": work_hours, 
            "leisure_hours": leisure_hours, 
            "sleep": sleep, 
            "exercise": exercise, 
            "dopamine_level": dopamine_level,
            "brain_score": brain_score
        })
        return response

    except Exception as e:
        return f"⚠️ Error: {str(e)}"