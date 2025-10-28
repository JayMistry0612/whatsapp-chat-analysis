📘 WhatsApp Chat Analysis
🔗 Live App

👉 Click here to try the app

📖 Overview

The WhatsApp Chat Analysis App is a powerful, Streamlit-based analytics tool that helps you visualize and understand your WhatsApp conversations.
It uncovers chat trends, user behavior, emotions, and content patterns using modern NLP and data visualization techniques.

✨ Features
📊 Core Analytics

Total messages, words, media shared, and links

Activity heatmap: hourly, daily, and monthly

Top users, most active days, and busiest times

🧠 Sentiment Analysis

Uses TextBlob to classify chats into Positive, Negative, and Neutral

Displays sentiment ratio with clean visual insights

🌈 WordCloud & Emoji Analysis

Generates a WordCloud of most used words

Automatically removes “<Media omitted>” and empty entries

Emoji leaderboard showing top used emojis

📈 Interactive Dashboard

User-based filters for group chats

Visual charts powered by Matplotlib and Streamlit

Engaging layout with real-time updates

🧰 Tech Stack
Component	Technology
UI / Frontend	Streamlit
Data Processing	Pandas, NumPy
Visualization	Matplotlib, WordCloud
Sentiment Analysis	TextBlob
Emoji Handling	Emoji
🗂️ Folder Structure
whatsapp-chat-analysis/
│
├── app.py
├── requirements.txt
├── README.md
├── sample_chat.txt
└── assets/
    ├── wordcloud_example.png
    ├── emoji_chart.png
    ├── sentiment_chart.png
    └── dashboard_preview.png

⚙️ Installation

Clone the repository

git clone https://github.com/<your-username>/whatsapp-chat-analysis.git
cd whatsapp-chat-analysis


Create and activate virtual environment (optional)

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py

📁 How to Use

Export your WhatsApp chat (without media).

Upload the .txt file using the Streamlit UI.

Choose a specific user (or overall).

Explore analytics, WordClouds, and sentiment trends.

📊 Example Insights

Top Active User: Identifies the most chatty participant

Most Used Words: Highlights common conversation words

Emoji Usage: Shows emoji frequency per user

Sentiment Breakdown: Pie chart of positive vs. negative messages

Timeline: Visual pattern of chat frequency across days and months

🧩 Future Enhancements

🧠 Transformer-based sentiment model for deeper tone detection

🔍 Topic modeling (e.g., clustering conversations by theme)

📅 Time period comparisons

💬 AI chat summarizer using LLMs

🧑‍💻 Author

Jay Mistry
📧 [Add your email or GitHub link here]
💼 GitHub

🖼️ Preview

Here’s what your dashboard looks like 👇

WordCloud	Emoji Analysis	Sentiment Overview	Dashboard

	
	
	
🚀 Deployment

Deployed via Streamlit Cloud
🔗 https://whatsapp-chat-analysis-projecttt.streamlit.app/
