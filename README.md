
## 🕉️ Rig Vedha Chatbot

An interactive AI-powered chatbot that answers questions related to **Rig Veda** using **Google Gemini (via LangChain)** for intelligent responses.
Built with a **Flask backend** and a **React frontend**, this project supports **Markdown-formatted replies**, including Sanskrit verses and translations.

---

### 📁 Project Structure

```
Rig-Vedha-Chatbot/
│
├── backend/
│   ├── app.py                 # Flask API server
│   ├── requirements.txt       # Python dependencies
│   ├── results.json           # Quiz results storage
│   ├── venv/                  # Virtual environment
│   └── ...                    # Other backend files
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── Chatbot.js     # Main chat interface
│   │   └── App.js
│   ├── package.json           # Frontend dependencies
│   └── ...                    # React setup files
│
└── README.md
```

---

### 🚀 Features

✅ Ask questions about the Rig Veda (e.g. mantras, deities, meanings)
✅ Backend powered by **LangChain + Gemini 2.5 Pro**
✅ Markdown rendering for beautiful Sanskrit + translation display
✅ Flask REST API to serve LLM responses and quiz submissions
✅ JSON-based result storage for quiz answers
✅ Responsive React frontend UI

---

### ⚙️ Tech Stack

#### **Frontend**

* React 18
* React Markdown (`react-markdown`)
* Axios (for API calls)

#### **Backend**

* Flask (Python)
* LangChain
* Google Generative AI (`gemini-2.5-pro`)
* JSON for result persistence

---

### 🧩 Installation Steps

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/rig-vedha-chatbot.git
cd rig-vedha-chatbot
```

---

#### 2️⃣ Setup Backend (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)
# source venv/bin/activate  # (Mac/Linux)

pip install -r requirements.txt
```

Create a `.env` file in the backend directory:

```
GEMINI_KEY=your_google_generative_ai_api_key
```

Run the backend:

```bash
python app.py
```

Backend runs on:
👉 `http://localhost:5000`

---

#### 3️⃣ Setup Frontend (React)

```bash
cd frontend
npm install
npm install react-markdown
npm start
```

Frontend runs on:
👉 `http://localhost:3000`

---

### 💬 Example Usage

**User:**

> What is the famous mantra in the Rig Veda?

**Bot (Markdown formatted):**

```
🌞 **Famous Mantra in the Rig Veda**

The most revered mantra is the **Gāyatrī Mantra** (Rig Veda 3.62.10)

> **तत् सवितुर्वरेण्यं**
> **भर्गो देवस्य धीमहि**
> **धियो यो नः प्रचोदयात् ॥**

_Translation_: “We meditate upon the divine radiance of Savitṛ.  
May He enlighten our intellect.”
```

---

### 🧠 Example Prompt Template (LangChain)

```python
prompt = PromptTemplate.from_template("""
You are an expert on Rig Veda.
Answer beautifully using Markdown with:
- Headings
- Bold keywords
- Sanskrit verses in block quotes
- English translation in italics

User question: {question}
""")
```

---

### 🧾 License

This project is open-source under the **MIT License**.
Feel free to use, modify, and share it for educational purposes.

---

### 🌟 Acknowledgments

* **LangChain** for LLM workflow management
* **Google Gemini API** for powerful Sanskrit + philosophy understanding
* **React + Flask** for the simple and elegant tech stack

