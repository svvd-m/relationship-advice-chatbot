# Relationship Advice Chatbot

An AI-powered relationship counselor that uses **Google Gemini-2.0-Flash** with **Retrieval-Augmented Generation (RAG)**, integrated **sentiment analysis**, and **chat logging**, all presented via a clean SMS-style Gradio interface.

---

## Overview

This project simulates an intelligent relationship counselor designed to:  
- Provide psychology-informed advice on love, communication, conflict, and getting over breakups  
- Enhance responses with context from three self-help books (RAG) hosted on GitHub  
- Analyze user sentiment (Positive/Neutral/Negative) using TextBlob  
- Log every conversation for later analytics and model improvement

The chatbot runs in a Colab notebook (or locally via `app.py`) and launches a Gradio UI for interaction.

---

## Features

- **Google Gemini-2.0-Flash** powered conversational logic  
- **Retrieval-Augmented Generation** (RAG) using book excerpts from:  
  - *Men Are from Mars, Women Are from Venus*  
  - *Nonviolent Communication*  
  - *The Art of Loving*  
  (all fetched automatically from GitHub)   
- **Sentiment Analysis** via TextBlob to detect user tone  
- **Chat Logging**: all messages, sentiments, and bot replies saved to `logs/chat_log.csv`  
- **Analytics Dashboard**: visualize sentiment distribution and word clouds of user queries  
- **Clean SMS-Style UI** built with Gradio (`type="messages"`, Enter-to-send, Send/Clear buttons)  
- **Colab-Friendly**: works in Google Colab or locally as a Python script  
- **Optional Hosting**: easily deploy to Hugging Face Spaces for a public demo  

---

## Tools & Technologies

| Purpose                   | Technology / Library                         |
|---------------------------|----------------------------------------------|
| Language Model (LLM)      | Google Gemini-2.0-Flash via `google-genai`    |
| Retrieval / RAG           | Simple chunk lookup of GitHub-hosted texts   |
| Sentiment Analysis        | TextBlob                                     |
| UI Framework              | Gradio (`type="messages"`)                   |
| Data Logging & Analytics  | Pandas, Matplotlib, WordCloud                |
| Notebook Environment       | Google Colab                                |
| Optional Deployment       | Hugging Face Spaces                          |
| Programming Language      | Python 3                                    |

---

## File Structure

```

relationship-advice-chatbot/
├── app.py                       # Flask/Gradio script for local run (same logic as notebook)
├── chatbot\_notebook.ipynb       # Colab notebook with full code, comments, and analytics
├── requirements.txt             # Python dependencies
├── README.md                    # This documentation
└── logs/
└── chat\_log.csv             # Auto-generated chat logs with sentiments

````

---

## How It Works

1. **User Input**  
   - User types a question (e.g., “How do I get over someone I know is incompatible?”) in the Gradio UI.

2. **Retrieval-Augmented Prompt**  
   - The notebook fetches three self-help texts from GitHub, splits them into ~400-character chunks, and picks the top 3 chunks to provide context.  

3. **Gemini API Call**  
   - A combined prompt (“You are a psychologist… [book excerpts] …User: [message] Assistant:”) is sent to `gemini-2.0-flash` via the `google-genai` client.  

4. **Sentiment Analysis & Logging**  
   - TextBlob analyzes the user’s message and labels it Positive/Neutral/Negative.  
   - User message, sentiment label, and bot response are appended to `logs/chat_log.csv`.  

5. **Display Response**  
   - The bot’s reply appears in the chat history. Enter key or “Send” button triggers new messages; “Clear Chat” resets history.  

6. **Analytics Dashboard** (run after stopping Gradio)  
   - A separate code cell reads `logs/chat_log.csv`, plots sentiment distribution, and (optionally) generates a word cloud of user queries.

---

## Sample Questions to Try

- “How do I move on after a breakup?”  
- “Is holding hands a sign of love?”  
- “How do I build trust in a relationship?”  
- “What should I do if we keep arguing?”  
- “How can I improve communication with my partner?”  

---

## Setup & Run Locally

1. **Clone the repository**  
   ```bash
   git clone https://github.com/svvd-m/relationship-advice-chatbot.git
   cd relationship-advice-chatbot
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Gemini API key**

   * Create an environment variable:

     ```bash
     export GEMINI="<your-gemini-api-key>"
     ```
   * Or, if running in Colab, add a secret named `Gemini` with your key.

4. **Run locally**

   ```bash
   python app.py
   ```

   * Opens a Gradio interface at `http://localhost:7860`.
   * Type your question, press Enter or click “Send,” and view advice.

---

## Run in Google Colab

1. **Open the Colab notebook**

   * Click this link or paste it into a browser:

     ```
     https://colab.research.google.com/github/svvd-m/relationship-advice-chatbot/blob/main/chatbot_notebook.ipynb
     ```

2. **Add your Gemini key**

   * In Colab, go to `Runtime → Manage Secrets` and create a secret named `Gemini` with your API key.

3. **Run all cells**

   * Sections will install dependencies, fetch RAG texts, define helper functions, launch the Gradio UI, and—after you stop the UI—run the analytics dashboard.

---

## Analytics Dashboard

Once you’ve finished chatting (and you interrupt the Gradio cell), run the following section to visualize your conversation data:

```python
# 1. Load chat_log.csv
import os, pandas as pd, matplotlib.pyplot as plt
from wordcloud import WordCloud

log_path = "logs/chat_log.csv"
if not os.path.exists(log_path):
    print("No chat_log.csv found. Run Gradio cell and chat, then stop it before running analytics.")
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

---

## Future Enhancements

* **Semantic RAG**: Replace the simple “first 3 chunks” retrieval with TF-IDF or embedding-based similarity search (FAISS).
* **Persistent User State**: Allow the chatbot to recall prior sessions (e.g., via cookies or database).
* **Multi-Language Support**: Add additional language backends to help more users.
* **Hugging Face Spaces Deployment**: Follow the “Gradio CLI → `gradio deploy`” flow to host permanently on Hugging Face with GPU acceleration and versioning.

---

## License & Privacy

* Logged conversations may contain sensitive information. Remove or anonymize logs before sharing publicly.
* This project is released under the MIT License. 
```
```
