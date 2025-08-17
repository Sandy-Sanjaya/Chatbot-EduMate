import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables from .env file 
load_dotenv()

st.set_page_config(
    page_title="EduMate 🎓",
    page_icon="🎓",
    layout="wide"
)

# Load API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

gen_ai.configure(api_key=GOOGLE_API_KEY)
model=gen_ai.GenerativeModel("gemini-2.5-flash")

# Init session state
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# ===== SIDEBAR =====
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=120)
    st.markdown("## 🎓 EduMate")
    st.write("Teman akademik cerdas yang siap mendampingimu belajar kapan saja.")
    st.markdown("---")
    st.markdown("### 📌 Tips Penggunaan")
    st.write("- Gunakan **Bahasa Indonesia** atau **English**")
    st.write("- Bisa tanya teori, rangkuman, atau latihan soal")
    st.write("- Cocok untuk persiapan ujian 🎯")

# ===== HEADER =====
st.markdown(
    """
    <div style="text-align:center; padding: 10px 0;">
        <h1 style="color:#1E40AF; margin-bottom:0;">📘 EduMate</h1>
        <p style="color:#475569; font-size:18px; margin-top:0;">
            Mentor digital yang membantumu memahami konsep, merangkum materi, dan berlatih soal.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ===== CHAT AREA =====
chat_container = st.container()

with chat_container:
    for message in st.session_state.chat_session.history:
        if message.role == "user":
            st.chat_message("user", avatar="🧑‍🎓").markdown(message.parts[0].text)
        else:
            st.chat_message("assistant", avatar="🎓").markdown(message.parts[0].text)

# ===== INPUT BOX =====
st.markdown("#### 💬 Tanyakan sesuatu pada EduMate")
user_input = st.chat_input("Ketik pertanyaanmu di sini...")

if user_input:
    # tampilkan pesan user
    st.chat_message("user", avatar="🧑‍🎓").markdown(user_input)

    # dapatkan respon dari model
    response = st.session_state.chat_session.send_message(user_input)

    # tampilkan respon bot
    st.chat_message("assistant", avatar="🎓").markdown(response.text)