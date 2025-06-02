# Voicemail Urgency Detection

This is a work-in-progress project for detecting urgency levels in voicemail transcriptions using Google Vertex AI. The goal is to build a backend service that classifies voicemails as **urgent** or **non-urgent**, helping streamline response prioritization in IT support.

---

## 🚀 Objectives

- Convert voicemails to text using Google Speech-to-Text (or existing transcripts).
- Analyze transcriptions using NLP to detect urgency.
- Train a custom model with Google Vertex AI.
- Build an API endpoint using Flask or FastAPI to serve predictions.

---

## 🧠 Why I am building this?

This project was inspired by the need to triage customer voicemails quickly and efficiently in IT service environments especially **after work hours**.

---

## ✅ Current Status

- [x] Initial research
- [x] Google NLP tried (results not useful)
- [x] Decided to train a custom model on Vertex AI
- [x] Dataset preparation with real-world voicemail samples
- [x] Model training 
- [ ] API development (in progress)
- [ ] Deployment

---

## 📂 Tech Stack

- Python
- Google Cloud Vertex AI
- Google Cloud NLP (initially)
- Flask / FastAPI (TBD)

---

## 📝 Future Improvements

- Integrate frontend dashboard for message review.
- Use more advanced NLP (e.g., transformers like BERT).
- Improve dataset with more dataset

---


## 📌 Note

This project is **not complete yet**. It is being built step by step to improve my skills in backend development, cloud services, and applied AI.
