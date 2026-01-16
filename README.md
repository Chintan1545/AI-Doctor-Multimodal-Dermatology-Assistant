# AI-Doctor-Multimodal-Dermatology-Assistant

An AI-powered doctor-style dermatology assistant built using Groq LLMs and Streamlit, capable of analyzing face images + text queries to provide safe, educational skin insights.

 ⚠️ Disclaimer: This project is for educational and research purposes only and does not   provide medical diagnosis or treatment.

---

## 🚀 Features

* 🖼️ Image + Text Multimodal Analysis
* 🧑‍⚕️ Doctor-style prompt tuning (Dermatologist AI)
* 🛡️ Medical-safe responses (no diagnosis / no prescriptions)
* 📋 Structured clinical-style output:
  * Observation
  * Possible explanation
  * General care tips
  * When to see a doctor
  * Medical disclaimer
* ⚡ Powered by Groq LLaMA Vision Models
* 🎨 Clean Streamlit UI
* 🔐 Secure API key handling via .env

---

## 🧠 Tech Stack

* Python
* Streamlit
* Groq API
* Meta LLaMA 4 Vision Model
* dotenv
* Base64 image encoding

---

## 📂 Project Structure
```bash
ai-doctor-dermatology/
│
├── app.py                # Streamlit application
├── .env                  # API keys (not committed)
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── sample_images/        # (Optional) Test images
```
---

## 📦 Installation

1️⃣ Clone Repository
```bash
git clone https://github.com/Chintan1545/ai-doctor-dermatology.git
cd ai-doctor-dermatology
```
2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---
## 🔐 Environment Setup

Create a .env file in the root directory:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
❗ Never commit your .env file to GitHub.

---

## ▶️ Run the Application
```bash
streamlit run app.py
```
Open browser at:
```bash
http://localhost:8501
```

---

## 🧪 Example Use Case

User Input:
  * Upload a face image
  * Ask: “Is there something wrong with my skin?”
AI Output:
  * Observes visible skin features
  * Explains possible non-diagnostic causes
  * Suggests general skincare habits
  * Recommends professional consultation
  * Includes medical disclaimer

---

## 🛡️ Medical Safety Design

This project strictly follows responsible AI principles:
  * ❌ No medical diagnosis
  * ❌ No prescriptions
  * ✅ Clear disclaimers
  * ✅ Supportive, non-alarming tone
  * ✅ Encourages professional consultation

---

## 📈 Future Enhancements

  * 🎙️ Voice-based doctor responses
  * 📊 Skin severity scoring
  * 🧠 Multi-specialist AI (Dermatology, Dental, Eye)
  * 🗂️ Patient interaction memory
  * ☁️ Deployment on AWS / Hugging Face Spaces

---

## 👨‍💻 Author

Chintan Dabhi
AI Engineer | AI Agents | Multimodal Systems

  * 🔗 GitHub: https://github.com/Chintan1545

--- 

## ⭐ Support

If you find this project useful, give it a star ⭐ and feel free to fork or contribute.
