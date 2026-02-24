# Stock News Alert 📈

This project monitors stock price changes and sends SMS alerts with related news.

## 🚀 Features
- Fetches stock price data
- Detects significant price changes
- Retrieves related news articles
- Sends SMS notifications using Twilio

## 🛠 Technologies Used
- Python
- Requests
- Twilio API
- NewsAPI
- python-dotenv

## 🔐 Environment Variables

Create a `.env` file and add:

NEWS_API_KEY=your_news_api_key  
TWILIO_ACCOUNT_SID=your_twilio_sid  
TWILIO_AUTH_TOKEN=your_auth_token  
TWILIO_PHONE_NUMBER=your_twilio_number  

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the project:
python main.py

---

This project was built for learning API integration and automation.