import streamlit as st
import google.generativeai as genai
import os 
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

st.title("🌟 Daily Motivation Generator")
st.write("Select your mood or situation, and get a personalized motivational message .")

moods = [
    "Feeling anxious",
    "Need focus",   
    "Feeling low",
    "Need confidence",
    "Excited but nervous",
    "Overwhelmed",
    "Procrastinating",
    "Need inspiration",
    "Feeling grateful",
    "Other"
]

selected_mood = st.selectbox("How are you feeling today?", moods)

custom_mood = ""
if selected_mood == "Other":
    custom_mood = st.text_input("Describe your current mood or situation:")

if st.button("Generate Motivation"):
    prompt = (
        f"Give me a short, encouraging motivational message for someone who is "
        f"{custom_mood if selected_mood == 'Other' else selected_mood.lower()}. "
        "Keep it uplifting, positive, and original."
    )
    with st.spinner("Generating your motivation..."):
        try:
            model = genai.GenerativeModel("gemini-2.5-flash")

            response = model.generate_content(prompt)
            motivation = response.text.strip()
            st.success(motivation)
        except Exception as e:
            st.error(f"Error generating motivation: {e}")
