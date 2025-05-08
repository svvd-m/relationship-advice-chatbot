# 💬 Relationship Advice Chatbot

An AI-powered conversational assistant that provides psychology-informed relationship advice using OpenAI’s GPT-3.5, with integrated sentiment analysis and user interaction logging.

## 🔍 Overview

This project simulates an intelligent relationship counselor, designed to:
- Provide tailored advice on love, communication, and conflict.
- Analyze user sentiment to understand emotional context.
- Log conversations securely for analysis and model improvement.

Deployed as a web-based chatbot interface using Gradio.

## 🧠 Features

- ✅ GPT-3.5 powered conversational logic
- ✅ Sentiment analysis using TextBlob
- ✅ Chat logging to CSV for user insights
- ✅ Clean, SMS-style Gradio interface
- ✅ Input sanitization and error handling

## 📊 Tools & Technologies

| Purpose                  | Tech Stack                         |
|--------------------------|------------------------------------|
| AI/LLM                   | OpenAI GPT-3.5                     |
| Sentiment Analysis       | TextBlob                           |
| UI Interface             | Gradio                             |
| Programming Language     | Python                             |
| Visualization (Optional) | Matplotlib                         |
| Hosting Option           | Hugging Face Spaces (optional)     |

## 📁 File Structure
├── app.py # Chatbot logic + Gradio interface
├── chatbot_notebook.ipynb # Colab development version
├── requirements.txt # Dependencies for reproducibility
├── README.md # Project documentation
└── logs/
└── chat_log.csv # Logged interactions



## 🧪 Sample Questions to Try

- "How do I move on after a breakup?"
- "Is holding hands a sign of love?"
- "How do I build trust in a relationship?"
- "What should I do if we keep arguing?"

## 📝 How It Works

1. The user inputs a relationship question.
2. The chatbot analyzes emotional tone using TextBlob.
3. A prompt is sent to GPT-3.5 with full conversation history.
4. The response is logged and shown in the UI.
5. All chats are saved to `logs/chat_log.csv`.

## 🔧 Setup & Run Locally

```bash
git clone https://github.com/yourusername/relationship-advice-chatbot.git
cd relationship-advice-chatbot
pip install -r requirements.txt
python app.py
```

🔒 Security Note
This app logs user queries and responses. Please ensure compliance with privacy requirements when deployed.

🧠 Future Enhancements
RAG integration using psychology self-help books

Analytics dashboard for emotional trends

Hugging Face deployment with persistent memory

🙋‍♂️ Author
Saad Mohamad
🎓 M.Sc. Business Analytics (AI Specialization)
🔗 LinkedIn
💼 Portfolio Projects

