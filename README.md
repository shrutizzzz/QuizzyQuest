# QuizzyQuest
# Scoring API and Quiz Application

This repository contains two primary components: a **Quiz Application** and a **Subjective Scoring API**.

---

## **Project Structure**
---

## **Features**

### **Quiz Application (Backend + Frontend)**
- **Frontend**: A quiz interface that allows users to answer questions and move to the next one.
- **Backend**: Handles storing answer in MongoDB and verifying their correctness against predefined answers through api.

### **Subjective Scoring API**
- Accepts user-submitted answers via a REST API.
- Uses **RAKE** for keyword extraction and **WordNet** for synonym matching.
- Generates a score based on weighted keyword matches.

---

## **Getting Started**

### Prerequisites

Ensure you have the following installed:
- **Node.js** (for the quiz application backend)
- **Python 3.8+** (for the scoring API)
- **MongoDB** (for storing quiz answers)
## **RUN on terminal**
- cd scoring_api
- pip install -r requirements.txt
- uvicorn app:app --reload
- cd backend
- node server.js
- Now open the index.html on live server

