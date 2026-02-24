# 📄 AI Contract & Document Review Bot

## 🚀 Overview

The AI Contract & Document Review Bot is a lightweight MVP designed to automate the initial review of business contracts. The system extracts key contractual clauses and highlights potential risk areas, helping businesses reduce manual review effort and identify critical terms quickly. This project was built as part of an AI Engineer hiring task.

## 🎯 Problem Statement

Businesses frequently review contracts such as NDAs, vendor agreements, service contracts, and employment agreements. Manual review is time-consuming, error-prone, and risky if important clauses are overlooked. This project demonstrates how AI-based structured analysis can assist in contract review by identifying key clauses and highlighting potential risks.

## 🛠 Features

- Upload PDF contracts  
- Paste raw contract text  
- Extract key clauses:
  - Parties involved  
  - Duration  
  - Payment terms  
  - Termination clause  
  - Renewal clause  

- Risk Flag Detection:
  - Auto-renewal traps  
  - Liability exposure  
  - Missing exit clause  

- Plain English Summary  
- Clean, structured UI using Streamlit  

## 🧠 Architecture

The application follows a modular design:

1. Input Layer  
   Accepts PDF uploads or raw contract text.

2. Text Extraction Layer  
   Uses PyMuPDF for extracting text from PDF documents.

3. Analysis Layer  
   Designed as an LLM-ready structured analysis module. For stable MVP execution and to avoid API quota limitations during submission, the inference logic is currently mocked. The architecture supports seamless integration with Claude, OpenAI, or Gemini APIs.

4. Output Layer  
   Displays structured clause extraction results with color-coded risk flags and a plain English summary.

## 💻 Tech Stack

- Python  
- Streamlit  
- PyMuPDF  
- Modular LLM-ready architecture  

## ▶ How to Run Locally

Clone the repository:

git clone YOUR_REPOSITORY_LINK  
cd ai-contract-review-bot  

Install dependencies:

pip install -r requirements.txt  

Run the application:

streamlit run app.py  

The app will open in your browser at:

http://localhost:8501  

## 📌 Future Improvements

- Integrate Claude / OpenAI / Gemini API for semantic clause understanding  
- Add clause confidence scoring  
- Enable downloadable analysis report (PDF export)  
- Improve clause extraction using semantic parsing  
- Add multi-language contract support  

## 👨‍💻 Author

Srikanth Gudla  
AI Engineer Hiring Task Submission
