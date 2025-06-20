# NeuroNest AI Micro-service 🧠⚡

[![API Status](https://img.shields.io/badge/API-local--dev-green?style=flat-square&logo=fastapi)](http://127.0.0.1:8000/docs)

A tiny FastAPI wrapper around OpenAI’s Chat Completion endpoint, built for rapid prototyping of post-TBI caregiver tools.

---

## Quick start

```bash
git clone https://github.com/LeslieDesign/ai-sketchpad.git
cd ai-sketchpad
python -m venv venv && venv\Scripts\activate   # mac/Linux: source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
