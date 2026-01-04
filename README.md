# OLX Price Hunter

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A Python-based Telegram bot that automates price monitoring on OLX.ua. It tracks a specific product URL and sends instant notifications when the price drops.

## Features
* **Real-time Monitoring:** Checks prices automatically in the background (24/7).
* **Smart Parsing:** Extracts price data directly from JSON (resilient to HTML layout changes).
* **Telegram Alerts:** Sends detailed reports with old/new price comparison and discount amount.
* **User-Agent Rotation:** Uses fake user-agents to mimic real browser behavior.

## Tech Stack
* **Python 3**
* **BeautifulSoup4** & **LXML** (Web Scraping)
* **Requests** (HTTP Client)
* **Telegram Bot API**

## Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/talisman-ep/olx-price-tracker.git
    cd olx-price-tracker
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration**
    * Rename `config_example.py` to `config.py`.
    * Open `config.py` and add your credentials:
        ```python
        TELEGRAM_TOKEN = "your_bot_token_here"
        CHAT_ID = "your_chat_id_here"
        ```

4.  **Run the bot**
    ```bash
    python main.py
    ```

<img width="1232" height="327" alt="image" src="https://github.com/user-attachments/assets/841fe7bb-c39e-494c-976a-aa51b8b48817" />


## Disclaimer
This project is for educational purposes only. Please respect OLX's terms of service and `robots.txt`.
