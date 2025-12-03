# Relationship Advice Chatbot

An AI-powered relationship support tool that uses **Google Gemini 2.0 Flash**, simple **Retrieval-Augmented Generation (RAG)**, **sentiment analysis**, and **chat logging**, all inside a clean SMS-style **Gradio** interface.

This chatbot gives basic guidance on communication, breakups, trust, and emotional awareness using context from three public self-help books.

---

## Overview

This project simulates a small relationship advice assistant. It is designed to:

- give simple psychology-based advice  
- use context from three books stored on GitHub  
- detect user sentiment (Positive / Neutral / Negative)  
- log every conversation for analytics  
- run inside a Gradio chat UI  

You can run it in **Google Colab** or **locally** using `app.py`.

---

## Features

- **Google Gemini 2.0 Flash** for conversation  
- **RAG** using text from these three books:
  - *Men Are from Mars, Women Are from Venus*  
  - *Nonviolent Communication*  
  - *The Art of Loving*  
- **Sentiment analysis** using TextBlob  
- **Chat logging** saved to `logs/chat_log.csv`  
- **Analytics dashboard** for sentiment counts and word clouds  
- **SMS-style UI** using Gradio (`type="messages"`)  
- **Works in Colab or locally**  
- **Optional deployment** to Hugging Face Spaces  

---

## Tools & Technologies

| Purpose | Technology |
|--------|-------------|
| Language Model | Google Gemini 2.0 Flash (`google-genai`) |
| Retrieval / RAG | Simple chunk-based lookup from GitHub |
| Sentiment Analysis | TextBlob |
| UI | Gradio (messages layout) |
| Logging & Analytics | Pandas, Matplotlib, WordCloud |
| Notebook | Google Colab |
| Deployment (Optional) | Hugging Face Spaces |
| Language | Python 3 |

---

## File Structure

relationship-advice-chatbot/

├── app.py # Local Gradio script

├── chatbot_notebook.ipynb # Full Colab notebook

├── requirements.txt # Python dependencies

├── README.md # This documentation

└── logs/

└── chat_log.csv # Auto-generated logs


---

## How It Works

### 1. User Input  
User types a message in the Gradio chat box.

### 2. Retrieval (RAG)  
The notebook fetches the three book texts from GitHub, splits them into chunks, and selects the top 3 chunks.

### 3. Gemini API Call  
A combined prompt is sent to **gemini-2.0-flash** with:
- system instruction  
- selected book chunks  
- user message  

### 4. Sentiment Analysis  
TextBlob labels the user’s message as:
- Positive  
- Neutral  
- Negative  

### 5. Logging  
The chatbot saves:
- user message  
- sentiment  
- bot reply  

to `logs/chat_log.csv`.

### 6. Chat Display  
The Gradio UI shows the conversation in a text-message style layout.

### 7. Analytics Dashboard  
After stopping the UI, a code cell reads the chat log and shows:
- a bar chart of sentiment  
- a word cloud of common user phrases  

---

## Sample Questions

Try these:

- "How do I move on after a breakup?"  
- "What should I do if we keep arguing?"  
- "How do I stop overthinking in a relationship?"  
- "How can I communicate better with my partner?"  
- "Is holding hands a sign of love or attention?"  

---

## Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/svvd-m/relationship-advice-chatbot.git
cd relationship-advice-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key
```bash
export GEMINI="<your-gemini-api-key>"
```

### 4. Run the chatbot
```bash
python app.py
```

Then open:
http://localhost:7860

### Run in Google Colab
Open the notebook:
```bash
https://colab.research.google.com/github/svvd-m/relationship-advice-chatbot/blob/main/chatbot_notebook.ipynb
```

### Steps in Colab:
- Add Gemini key in Runtime → Manage Secrets (Gemini)
- Run all cells
- Gradio UI will open
- After stopping the UI, run the analytics cell
- Analytics Dashboard Code
- Below is the code used in the analytics section:
```bash
# 1. Load chat_log.csv
import os, pandas as pd, matplotlib.pyplot as plt
from wordcloud import WordCloud

log_path = "logs/chat_log.csv"
if not os.path.exists(log_path):
    print("No chat_log.csv found. Chat first, then stop the UI.")
else:
    logs = pd.read_csv(log_path)

    # 2. Plot sentiment distribution
    plt.figure(figsize=(6,4))
    counts = logs["Sentiment"].value_counts().reindex(
        ["Positive","Neutral","Negative"], fill_value=0
    )
    counts.plot(kind="bar", color=["#4CAF50","#FFC107","#F44336"])
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.show()

    # 3. Word cloud of user messages
    text = " ".join(logs["User Message"].dropna().tolist())
    if text:
        wc = WordCloud(width=800, height=400, background_color="white").generate(text)
        plt.figure(figsize=(10,5))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.title("Common Words in User Queries")
        plt.show()
    else:
        print("Not enough data for a word cloud.")
```

## Future Enhancements

- Replace simple chunk lookup with semantic search (FAISS / embeddings)
- Store user session history
- Multi-language support
- Deploy on Hugging Face Spaces

## License & Privacy
- Conversations may contain personal information. Avoid sharing logs publicly.
- Project is released under the MIT License.
