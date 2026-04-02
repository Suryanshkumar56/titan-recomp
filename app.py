import streamlit as st
import google.generativeai as genai

# Setup
st.set_page_config(page_title="Titan Recomp", page_icon="💪")
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

st.title("🦾 Titan Recomp: All-In-One")
menu = st.sidebar.radio("Menu", ["Workout Plan", "AI Diet Plan", "Progress Photo"])

if menu == "Workout Plan":
    st.header("🏋️ Home Jugad Plan")
    st.write("Target: Muscle Gain (Bar + Mat + School Bag)")
    ex = st.selectbox("Exercise", ["Backpack Squats", "Pull-ups", "Push-ups", "Bucket Carries"])
    if st.button("Log Workout"):
        st.success(f"Logged {ex}!")

elif menu == "AI Diet Plan":
    st.header("🥗 High-Protein Builder")
    st.write("NO Curd, Green Moong, or Kala Chana.")
    food = st.selectbox("Protein Source", ["Soya Chunks", "Paneer", "Tofu", "Yellow Dal"])
    if st.button("Generate Recipe"):
        prompt = f"Create a high-protein recipe with {food}. NO CURD, NO GREEN MOONG, NO KALA CHANA."
        response = model.generate_content(prompt)
        st.write(response.text)

elif menu == "Progress Photo":
    st.header("📸 Photo Tracker")
    pic = st.camera_input("Take a snap")
    if pic: st.image(pic)
