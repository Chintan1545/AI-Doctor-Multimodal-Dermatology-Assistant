import os
import base64
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# ===============================
# Load Environment Variables
# ===============================
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in .env file")
    st.stop()

# ===============================
# Initialize Groq Client
# ===============================
client = Groq(api_key=GROQ_API_KEY)

# ===============================
# Doctor-Style System Prompt
# ===============================
DOCTOR_SYSTEM_PROMPT = """
You are a licensed dermatologist AI assistant.

IMPORTANT RULES:
- You must NOT give a confirmed medical diagnosis.
- You must NOT prescribe medicines.
- You must clearly say this is NOT medical advice.
- Be calm, supportive, and professional.
- Do not alarm the user.

YOUR TASK:
1. Observe visible skin features from the image (acne, redness, scars, dryness, pigmentation).
2. Explain what these signs *might* indicate in simple, non-technical language.
3. Suggest general skincare and lifestyle care (hydration, hygiene, sunscreen).
4. Recommend consulting a certified dermatologist if needed.

RESPONSE FORMAT:
- Observation:
- Possible Explanation:
- General Care Tips:
- When to See a Doctor:
- Medical Disclaimer:
"""

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="AI Dermatologist", layout="centered")

st.title("🧑‍⚕️ AI Dermatologist (Groq Vision)")
st.write("Upload a face image and ask a skin-related question.")

st.warning(
    "⚠️ This tool is for educational purposes only and does NOT provide medical diagnosis."
)

# ===============================
# User Inputs
# ===============================
uploaded_file = st.file_uploader(
    "📷 Upload Face Image",
    type=["jpg", "jpeg", "png"]
)

query = st.text_input(
    "💬 Ask your question",
    value="Is there something wrong with my face?"
)

# ===============================
# Process Image + Query
# ===============================
if uploaded_file and query:

    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Convert image to Base64
    image_bytes = uploaded_file.read()
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    messages = [
        {
            "role": "system",
            "content": DOCTOR_SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]

    if st.button("🧠 Analyze Skin"):
        with st.spinner("Analyzing image..."):
            try:
                response = client.chat.completions.create(
                    model="meta-llama/llama-4-scout-17b-16e-instruct",
                    messages=messages
                )

                st.subheader("📋 AI Dermatologist Report")
                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"❌ Error: {e}")

else:
    st.info("👆 Upload an image and ask a question to begin.")

# ===============================
# Footer
# ===============================
st.markdown("---")
st.caption("🔬 Powered by Groq | ⚕️ Educational Use Only")
