# Chatbot-EduMate
EduMate adalah chatbot akademik berbasis Google Gemini API dan Streamlit yang dirancang untuk menjadi teman belajar cerdas bagi mahasiswa maupun pelajar. Dengan EduMate, kamu bisa bertanya apa saja terkait materi kuliah, meminta rangkuman, hingga berlatih soal secara interaktif.

# 🚀 Cara Menjalankan EduMate Chatbot

Berikut adalah langkah-langkah untuk menjalankan chatbot **EduMate** di lokal komputer kamu.

---

## 1️⃣ Clone Repository
Pertama, clone repository ini ke komputer kamu:

```bash
git clone https://github.com/Sandy-Sanjaya/Chatbot-EduMate.git
cd edumate-chatbot
```

## 2️⃣ Buat Virtual Environment (Opsional tapi Disarankan)
Untuk menjaga dependencies tetap rapih, buat virtual environment:
```bash
python -m venv venv
```

## 3️⃣ Install Dependencies
Install semua library yang dibutuhkan dari requirements.txt:
```bash
pip install -r requirements.txt
```

## 4️⃣ Atur API Key
Aplikasi ini menggunakan Gemini API.
Buat file .env di root folder project, lalu tambahkan:
```bash
GOOGLE_API_KEY=your_google_api_key
```

## 5️⃣ Jalankan Aplikasi
Setelah semua siap, jalankan dengan perintah:
```bash
streamlit run main.py
```
