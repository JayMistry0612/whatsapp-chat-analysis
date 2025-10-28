import streamlit as st
import pandas as pd
import re
import emoji
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud
from datetime import datetime

# ---------------------------------------------
# ⚙️ Helper Functions
# ---------------------------------------------
def preprocess_chat(uploaded_file):
    read = uploaded_file.readlines()
    data = []
    for x in read:
        x = x.decode("utf-8").strip()
        match = re.match(r'(\d+/\d+/\d+)', x)
        if match:
            splitLine = x.split(' - ')
            if len(splitLine) < 2:
                continue
            dateTime = splitLine[0]
            k = dateTime.split(', ')
            if len(k) < 2:
                continue
            date, time = k[0], k[1]
            message = ' '.join(splitLine[1:])
            chck = re.findall(':', message)
            if chck:
                author, comments = message.split(":", 1)
                data.append([date, time, author.strip(), comments.strip()])
        else:
            if x != "":
                data.append([date, time, author, x])
    df = pd.DataFrame(data, columns=['Date', 'Time', 'Author', 'Message'])
    return df


def get_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'


def extract_emojis(s):
    return [c for c in str(s) if c in emoji.EMOJI_DATA]


def clean_messages(df):
    """Remove deleted and media messages"""
    df = df[~df['Message'].str.contains("Media omitted", case=False, na=False)]
    df = df[df['Message'] != ' This message was deleted']
    return df


def generate_wordcloud(text_series):
    """Generate safe WordCloud (no crash even if empty)"""
    text = " ".join(str(msg) for msg in text_series)
    text = re.sub(r"<Media omitted>|Media omitted", "", text, flags=re.IGNORECASE).strip()

    if not text or len(text.split()) == 0:
        return None

    wc = WordCloud(width=800, height=400, background_color="white", colormap="viridis").generate(text)
    return wc


# ---------------------------------------------
# 🧠 Streamlit UI
# ---------------------------------------------
st.set_page_config(page_title="WhatsApp Chat Analyzer", page_icon="💬", layout="wide")
st.title("💬 WhatsApp Chat Analyzer ")
st.caption("Developed by **Jay Mistry** 🚀 | Enhanced with Sentiment, Emojis & WordCloud Insights")

uploaded_file = st.file_uploader("📁 Upload your exported WhatsApp chat (.txt)", type="txt")

if uploaded_file is not None:
    with st.spinner("Processing your chat file..."):
        df = preprocess_chat(uploaded_file)
        df = clean_messages(df)
        df['Sentiment'] = df['Message'].apply(get_sentiment)
        df['Emojis'] = df['Message'].apply(extract_emojis)

        # Convert Date safely
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
        df = df.dropna(subset=['Date'])

        st.success("✅ Chat processed successfully!")

        # ---------------------------------------------
        # 🎛️ Filters
        # ---------------------------------------------
        st.sidebar.header("🔍 Filters")
        users = df['Author'].dropna().unique().tolist()
        users.insert(0, "All")
        selected_user = st.sidebar.selectbox("Select User", users)

        min_date, max_date = df['Date'].min(), df['Date'].max()
        start_date, end_date = st.sidebar.date_input("Select Date Range", [min_date, max_date])

        filtered_df = df.copy()
        if selected_user != "All":
            filtered_df = filtered_df[filtered_df['Author'] == selected_user]
        if start_date and end_date:
            filtered_df = filtered_df[
                (filtered_df['Date'] >= pd.to_datetime(start_date)) &
                (filtered_df['Date'] <= pd.to_datetime(end_date))
            ]

        st.sidebar.success("✅ Filters applied successfully")

        # ---------------------------------------------
        # 📊 Overview Metrics
        # ---------------------------------------------
        st.header("📊 Overview")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Messages", len(filtered_df))
        with col2:
            st.metric("Unique Participants", df['Author'].nunique())
        with col3:
            st.metric("Total Emojis", sum(filtered_df['Emojis'].apply(len)))
        with col4:
            avg_sent = filtered_df['Sentiment'].value_counts(normalize=True).get('Positive', 0) * 100
            st.metric("Avg. Positivity %", f"{avg_sent:.1f}%")

        # ---------------------------------------------
        # 👥 Messages per User
        # ---------------------------------------------
        st.header("👥 Messages per User")
        msg_count = df['Author'].value_counts()
        st.bar_chart(msg_count)

        # ---------------------------------------------
        # 🖼️ Media per User
        # ---------------------------------------------
        st.header("🖼️ Media Messages per User")
        media_df = df[df['Message'].str.contains("<Media omitted>", na=False)]
        if not media_df.empty:
            media_count = media_df['Author'].value_counts()
            st.bar_chart(media_count)
        else:
            st.info("No media messages found in this chat.")

        # ---------------------------------------------
        # 💬 Sentiment Analysis
        # ---------------------------------------------
        st.header("💬 Sentiment Analysis")
        sentiment_counts = filtered_df['Sentiment'].value_counts()
        st.bar_chart(sentiment_counts)

        sentiment_user = filtered_df.groupby(['Author', 'Sentiment']).size().unstack(fill_value=0)
        st.dataframe(sentiment_user.style.highlight_max(axis=1, color='lightgreen'))

        # ---------------------------------------------
        # 😂 Emoji Analysis
        # ---------------------------------------------
        st.header("😂 Emoji Analysis")
        all_emojis = [e for sublist in filtered_df['Emojis'] for e in sublist]
        if all_emojis:
            emo_series = pd.Series(all_emojis).value_counts().head(10)
            st.subheader("Top 10 Emojis Used")
            st.bar_chart(emo_series)
        else:
            st.info("No emojis detected in selected range/user.")

        # ---------------------------------------------
        # ☁️ Word Cloud (Messages only)
        # ---------------------------------------------
        st.header("☁️ Word Cloud ")
        wc = generate_wordcloud(filtered_df['Message'])
        if wc:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wc, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.info("No valid messages for WordCloud.")

        # ---------------------------------------------
        # 🕒 Activity Over Time
        # ---------------------------------------------
        st.header("🕒 Activity Over Time")
        if not filtered_df['Date'].empty:
            date_count = filtered_df['Date'].value_counts().sort_index()
            st.line_chart(date_count)
        else:
            st.info("No data for this date range.")

        # ---------------------------------------------
        # 🔍 Raw Data
        # ---------------------------------------------
        st.header("🔍 Raw Chat Data")
        st.dataframe(filtered_df.head(100))

else:
    st.info("👆 Upload your WhatsApp exported chat file to start analysis.")
