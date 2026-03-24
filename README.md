# Gemini Inclusivity Coach
<p align="left">
  <a href="https://inclusive-workplace-coach.streamlit.app">
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white" height="25">
  </a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" height="25">
  <img src="https://img.shields.io/badge/python-3.11+-blue.svg?style=flat-square" height="25">
</p>

## Overview
The **Gemini Inclusivity Coach** is a full-stack AI application designed to foster more inclusive workplace environments through **Gemini 2.5 Flash's multimodal audio reasoning** to analyze for bias and gendered language and provides actionable, real-time feedback.

---

## Tech Stack & Architecture
**Cloud-Native** architecture
* **Frontend/UI:** [Streamlit](https://streamlit.io/)
* **AI Engine:** [Google Gemini 2.5 Flash](https://ai.google.dev/)
* **Database:** [SQLite](https://www.sqlite.org/) - MVP1 (goal migrate to PostgreSQL in MVP2)
* **Infrastructure:** [Streamlit Community Cloud](https://streamlit.io/cloud) - ephemeral containerization using DevContainers
* **CI/CD:** [GitHub Integrated Deployment](https://github.com/features/actions) – Automated build-and-deploy pipeline triggered on every commit from remote and local enviornments

---

## Key Features
* **Direct Audio Reasoning:** Speech-to-Text (STT) audio capture analyzes tone, inflection, and context
* **Session History:** Tracks history previous coaching sessions through SQL backend
* **Real-time Analytics:** Provides instant feedback on each audio-recording session (e.g., meeting facilitation, peer feedback).

---

## Deployment & Installation

### Cloud Access
The live MVP1 is available here: **https://inclusive-workplace-coach.streamlit.app**

### Local Setup
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/inclusive-coach.git]
    cd inclusive-coach
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
## Demo

https://github.com/user-attachments/assets/ef802871-1e1f-4cee-875f-67833a303b10

<img width="1913" height="988" alt="Screenshot 2026-03-24 at 12 19 04 PM" src="https://github.com/user-attachments/assets/34b21e0d-9322-4dbd-b634-a7fd4a8cbe23" />

<img width="1913" height="988" alt="Screenshot 2026-03-24 at 12 19 21 PM" src="https://github.com/user-attachments/assets/bcfd1328-1999-466f-9e03-7f2d26bc1a33" />

<img width="1913" height="988" alt="Screenshot 2026-03-24 at 12 19 36 PM" src="https://github.com/user-attachments/assets/ad9bd230-a664-4aa6-a2db-cecf3902acf7" />

<img width="1913" height="988" alt="Screenshot 2026-03-24 at 12 19 51 PM" src="https://github.com/user-attachments/assets/db22ee77-e845-4181-a0e3-98816132ecf7" />


