# 🤖 AI/ML Interview Assistant

An AI-powered interview preparation chatbot built using **Streamlit, LangChain, RAG, and Groq LLM**.

This project helps users learn AI/ML concepts, practice technical interview questions, and improve their answers through AI-powered feedback.

## 🚀 Features

### 1. Learning Mode
- Ask questions related to Machine Learning, Deep Learning, NLP, and other technical topics.
- Get context-aware answers using Retrieval-Augmented Generation (RAG).
- Uses a knowledge base to provide relevant responses.

### 2. Interview Mode
- Generate technical interview questions based on selected topics.
- Write your own answers to interview questions.
- Get AI-powered evaluation and feedback on your answers.
- Generate follow-up questions to simulate a real interview experience.

### 3. RAG-Based Architecture
- Retrieves relevant information from a vector database.
- Uses retrieved context to generate more relevant answers.
- Connects retrieval with an LLM for question answering.

### 4. User Interface
- Built with Streamlit.
- Simple, clean, and interactive interface.
- Separate Learning Mode and Interview Mode.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | User interface |
| LangChain | LLM and RAG orchestration |
| Groq | LLM inference |
| FAISS | Vector database |
| Sentence Transformers | Text embeddings |
| PyPDF | PDF document processing |

## 📂 Project Structure

```text
AI-ML-Interview-Chatbot/
│
├── app.py                  # Main Streamlit application
├── connect.py              # LLM connection and question answering
├── retriever.py            # Vector store and retriever
├── interview_mode.py       # Interview question generation and evaluation
│
├── requirements.txt        # Project dependencies
├── .env                    # API keys (not uploaded to GitHub)
├── .gitignore              # Ignored files
└── README.md               # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-ML-Interview-Chatbot.git
```

### 2. Navigate to the project directory

```bash
cd AI-ML-Interview-Chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and add your Groq API key.

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

Make sure the environment variable name matches the one used in `connect.py`.

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 How It Works

The application provides two different modes:

**Learning Mode:**

User Question → Retriever → Relevant Context → Groq LLM → Generated Answer

**Interview Mode:**

Select Topic → Generate Interview Question → Candidate Answer → AI Evaluation → Follow-up Question

## 🎯 Project Objective

The main objective of this project is to build an AI-powered learning and interview preparation assistant that combines RAG and LLM capabilities to provide an interactive technical interview experience.

## 🔮 Future Improvements

- Add difficulty levels (Easy, Medium, Hard).
- Store interview history and previous evaluations.
- Add performance tracking and interview scores.
- Support additional technical subjects.
- Improve conversational memory.
- Deploy the application for public access.

## 👨‍💻 Author

**Your Name**

GitHub: [Your GitHub Profile](https://github.com/Rahul-bhardwaj05)

---

⭐ If you find this project interesting, consider giving it a star!
