# 📈 NEPSE Stock Price Alert System (Python + Twilio)

A lightweight Python-based automation system that tracks live stock prices and sends instant SMS alerts when predefined price conditions are met.

Built for traders who cannot continuously monitor the market—especially useful during study/work hours.

## 🚀 Features

- 📡 Live stock price tracking using web scraping (BeautifulSoup)
- 🎯 Custom price target alerts (buy/sell zones)
- 📱 Instant SMS notifications via Twilio API
- ⚡ Automated monitoring with minimal human involvement
- 📊 Percentage change calculation for better decision making
- 🔁 Prevents duplicate alerts for the same condition
- 🧠 Supports multiple stocks in a single script

## 🛠️ Tech Stack

- Python 3
- BeautifulSoup (Web Scraping)
- Requests
- Twilio API (SMS alerts)
- Dotenv (.env for secure credentials)

## ⚙️ How It Works

1. Fetches live stock price from a financial data website (e.g., Merolagani)
2. Compares current price with predefined target price
3. If condition is met:
   - Sends SMS alert via Twilio
   - Includes LTP, target price, and price change details
4. Prevents repeated alerts until condition resets
