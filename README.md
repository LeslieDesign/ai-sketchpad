# NeuroGuideAI 🧠✨  
*Your AI-powered companion for traumatic-brain-injury recovery*

[![API Status](https://img.shields.io/badge/API-local--dev-green?style=flat-square&logo=fastapi)](http://127.0.0.1:8000/docs)

NeuroGuideAI turns wearable vitals, voice-stress samples, and caregiver check-ins into real-time guidance for survivors, families, and clinicians.

---

## Quick start

```bash
git clone https://github.com/LeslieDesign/ai-sketchpad.git
cd ai-sketchpad
python -m venv venv && venv\Scripts\activate    # mac/Linux: source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
