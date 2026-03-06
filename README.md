# 💰 The Brain Budget: Digital Dementia Analyzer
**Powered by NeuroTwin™ Engine v4.1**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Model](https://img.shields.io/badge/AI-Llama_3.2-purple)
![License](https://img.shields.io/badge/License-MIT-green)

## 🧠 The Concept
Most people treat their attention like it is infinite. It is not. **The Brain Budget** is a simulator that treats your focus like currency to combat **Digital Dementia**.

* **Income:** Sleep, Sunlight, Exercise (Deep Work).
* **Expenses:** Social Media, Doomscrolling, Multitasking (Dopamine Hits).

## 🚀 Key Features
* **NeuroTwin™ Engine (Proprietary Logic):** A custom Python algorithm that calculates a user's "Cognitive Decay Rate" based on their daily habits.
* **The Dopamine Graph:** Visualizes how fast mental energy is drained during high-stimulation activities.
* **AI Doctor (The Interface):** Integrates **Meta Llama 3.2** (via Ollama) to act as a medical consultant, translating the raw NeuroTwin data into actionable health advice.

---

## ⚙️ Prerequisites (Critical)
This project uses **Local Inference** for privacy. You do not need an API key, but you **must** have Ollama installed.

1.  **Download Ollama:** [https://ollama.com](https://ollama.com)
2.  **Install the Model:** Open your terminal and run:
    ```bash
    ollama pull llama3.2
    ```
3.  **Keep it Running:** Ensure the Ollama app is running in the background before launching the simulator.

---

## 🛠️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/SauravSP10/the-brain-budget.git
    cd the-brain-budget
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

---

## 🧩 Project Structure
* `app.py` - The main dashboard interface.
* `doctor_brain.py` - Contains the **NeuroTwin™ Logic** and AI connector.
* `utils.py` - Helper functions for calculations.
* `styles.py` - Custom CSS for the UI.

## 🛡️ License & Credits
* **License:** Distributed under the **MIT License**.
* **Core Logic:** Developed by Saurav R. Phadnis, MIT World Peace University.
* **AI Model:** Llama 3.2 by Meta (Running locally via Ollama).