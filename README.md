# 🌦️ Weather Desktop Application

A modern and lightweight **desktop weather application** built with **Python** and **CustomTkinter**.  
The app fetches real-time weather data using the **OpenWeather API** and presents it in a clean UI.

---

## ✨ Features
- 🌍 Real-time weather updates by city name
- 🖥️ Clean & modern desktop UI
- 🔐 Secure API key handling using `.env`
- ⚡ Fast and lightweight
- 📦 Windows EXE available

---

## 🛠 Tech Stack
- **Python 3**
- **CustomTkinter**
- **Requests**
- **python-dotenv**
- **OpenWeather API**
- **PyInstaller**

---

## 📂 Project Structure
weather-app/
├── app/
│ ├── ui/
│ ├── controllers/
│ ├── services/
│ ├── models/
│ ├── utils/
│ └── main.py
├── assets/
│ └── screenshot.png
├── .env.example
├── requirements.txt
└── README.md

---

## ▶️ How to Run (From Source)

1️⃣ Clone the repository
```bash
git clone https://github.com/mahbubstu20182-del/weather-app.git
cd weather-app
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Setup environment variables
Create a .env file in the root directory:
OPENWEATHER_API_KEY=0c27137c2422a9da5e27b83a1fea6a60
📦 Download (Windows EXE)

👉 Go to the Releases section and download the latest main.exe.

🧑‍💻 Developer

Mahbub Alam

📄 License

MIT