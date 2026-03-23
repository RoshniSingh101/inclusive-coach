# Gemini Inclusivity Coach
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## Overview
The **Gemini Inclusivity Coach** is a full-stack AI application designed to foster more inclusive workplace environments through **Gemini 2.5 Flash's multimodal audio reasoning** to analyze for bias and gendered language and provides actionable, real-time feedback.

---

## Tech Stack & Architecture

* **Frontend:** [Streamlit](https://streamlit.io/)
* **AI Engine:** [Google Gemini 2.5 Flash](https://ai.google.dev/)
* **Database:** [SQLite](https://www.sqlite.org/) - MVP1 (goal to migrate to PostgreSQL)
* **Infrastructure:** [Streamlit Community Cloud](https://streamlit.io/cloud) - ephemeral containerization using DevContainers
* **CI/CD:** [GitHub Integrated Deployment](https://github.com/features/actions) – Automated build-and-deploy pipeline triggered on every commit from remote and local enviornments

---

## Key Features
* **Direct Audio Reasoning:** Speech-to-Text (STT) audio capture analyzes tone, inflection, and context directly via Gemini's multimodal window
* **Session History:** Tracks history previous coaching sessions through SQL backend
* **Real-time Analytics:** Provides instant feedback on each audio-recording session (e.g., meeting facilitation, peer feedback).

---

## Deployment & Installation

### Cloud Access
The live MVP1 is available here: **https://inclusive-workplace-coach.streamlit.app**

### Local Setup
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/gemini-inclusivity-coach.git]
    cd gemini-inclusivity-coach
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run Application:**
    ```bash
    streamlit run app.py
    ```

---
