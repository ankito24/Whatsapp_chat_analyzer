WhatsApp Chat Analyzer

A powerful and interactive web app to analyse your WhatsApp chats — built with Python and Streamlit.

🔗 Live App: https://whatsappchatanalyzer-ankit29.streamlit.app/
[https://whatsappchatanalyzer-ankit29.streamlit.app/](https://whatsappchatanalyzer-ankit29.streamlit.app/)

**Features**


Top Statistics — Total messages, words, media shared, and links
Monthly Timeline — Message frequency over months
Daily Timeline — Day-by-day activity graph
Activity Map — Busiest days and months
Most Busy Users — Who chats the most (group chats)
WordCloud — Most used words visualised
Most Common Words — Bar chart of frequent words
Emoji Analysis — Emoji usage stats with pie chart

**How to Use**


Open the app: (https://whatsappchatanalyzer-ankit29.streamlit.app/)
Export your WhatsApp chat:

Open any chat in WhatsApp
Tap ⋮ Menu → More → Export Chat → Without Media
Save the .txt file



Upload the .txt file in the sidebar
Select a specific user or Overall
Click "Show Analysis" 



**Tech Stack**

TechnologyPurposePythonCore languageStreamlitWeb app frameworkPandasData processingMatplotlibCharts and graphsWordCloudWord cloud generationEmojiEmoji extractionURLExtractLink detectionSeabornStyling


**Project Structure**

Whatsapp_Chat_Analyser/
│
├── App.py              # Main Streamlit app
├── helper.py           # All analysis functions
├── preprocessor.py     # Chat data parsing
├── requirements.txt    # Dependencies
├── stop_hinglish.txt   # Stop words (Hindi + English)
└── README.md

**Run Locally**

bash# Clone the repo
git clone https://github.com/ankito24/Whatsapp_chat_analyzer.git
cd Whatsapp_chat_analyzer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run App.py

Developer
: Ankit 
