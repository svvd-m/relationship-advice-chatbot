# -*- coding: utf-8 -*-
"""Relationship_Advice_Chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cykRge6WHwPGiil6geKla5lsNMwRH3-N
"""

!pip install openai==1.10.0
!pip install gradio==4.24.0

# Required imports
from google.colab import userdata
import openai
import gradio as gr

# Fetch the OpenAI API key securely from the Colab Secrets menu
openai.api_key = userdata.get('openai')

# Define a function to handle chatbot responses
def chatbot_response(prompt, chat_history):
    try:
        # Start with a system message to set the context for the AI
        messages = [{"role": "system", "content": "You are a psychologist specializing in relationships. Help users with their relationship concerns."}]

        # Convert Gradio chat history (tuples) into OpenAI message format
        for user_input, bot_response in chat_history:
            messages.append({"role": "user", "content": user_input})
            messages.append({"role": "assistant", "content": bot_response})

        # Add the current user input
        messages.append({"role": "user", "content": prompt})

        # Call the OpenAI ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Extract the assistant's response
        bot_response = response['choices'][0]['message']['content']

        # Update chat history in Gradio format (list of tuples)
        chat_history.append((prompt, bot_response))

        return chat_history, ""  # Return updated history and clear input box
    except Exception as e:
        return chat_history, f"API Error: {str(e)}"

# Function to clear chat history
def clear_chat():
    return [], []  # Reset both the chat display and the chat history state

# Create the Gradio app
with gr.Blocks() as app:
    gr.Markdown("# **Relationship Advice Chatbot**")
    gr.Markdown("💬 Ask any relationship-related questions and receive expert advice!")

    # Components for chatbot UI
    chatbot = gr.Chatbot(label="Your Relationship Advisor")
    msg = gr.Textbox(placeholder="Type your message here...", label="Your Message")
    send_button = gr.Button("Send")
    clear_button = gr.Button("Clear Chat")

    # Initialize chat history
    chat_history = gr.State([])

    # Send button functionality
    send_button.click(
        chatbot_response, inputs=[msg, chat_history], outputs=[chatbot, msg]
    )

    # Clear button functionality (reset chat and history)
    clear_button.click(
        clear_chat, inputs=None, outputs=[chatbot, chat_history]
    )

app.launch()
