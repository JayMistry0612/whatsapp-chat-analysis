git clone https://github.com/JayMistry0612/whatsapp-chat-analysis.git
# WhatsApp Chat Analysis

Analyze your exported WhatsApp chats with an interactive Streamlit dashboard. The app provides sentiment breakdowns, emoji analytics, activity timelines, and a dynamic word cloud to help you gain insights into conversations.

Live demo: https://whatsapp-chat-analysis-projecttt.streamlit.app/

## Features
- Parse and clean WhatsApp exported .txt files (handles multi-line messages and common placeholders)
- Sentiment analysis (TextBlob): Positive / Neutral / Negative
- Emoji extraction and top-10 emoji stats
- Per-user message counts and activity timeline
- WordCloud generation from messages (safe for empty input)
- Interactive filters (user & date range)

## Quick start (Windows PowerShell)
1. Create and activate your virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Usage
1. In WhatsApp: Chat > More > Export chat (Without Media) and save the .txt file.
2. Upload the exported `.txt` file using the app's file uploader.
3. Use the sidebar to pick a participant (or "All") and select a date range.
4. Explore Overview metrics, Sentiment, Emoji stats, WordCloud, Activity timeline, and raw data table.

## Project structure
```
whatsapp-chat-analysis/
├── app.py              # Streamlit application (entrypoint)
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── sample_chat.txt     # Example WhatsApp export (optional)
└── assets/             # Optional preview images used in README
```

## Requirements
Key packages are pinned in `requirements.txt` (Streamlit, pandas, textblob, emoji, wordcloud, matplotlib, numpy).

## Notes & tips
- Date parsing uses day-first parsing and will drop rows with unparseable dates.
- WordCloud is skipped if there are no valid words.
- TextBlob provides a lightweight heuristic sentiment; for more accurate results consider transformer-based models.

## Development & Contributing
Feel free to open issues or PRs. Small improvements:
- Add tests for parsing edge cases
- Add optional deployment scripts (Docker / Streamlit sharing)

## License
This project is provided "as-is". Add an appropriate open-source license (e.g., MIT) if you plan to share it publicly.

## Author
Jay Mistry

Happy analyzing! 💬

	
	
	
