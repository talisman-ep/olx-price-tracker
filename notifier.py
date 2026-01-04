import requests
import sys
import os
from config import TELEGRAM_TOKEN, CHAT_ID

# Лікуємо консоль Windows
if sys.platform == 'win32':
    os.system('chcp 65001 >nul')
sys.stdout.reconfigure(encoding='utf-8')

def send_telegram_message(text):
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    
    try:
        response = requests.post(url, data=payload)
        
        # Перевірка на помилки
        if response.status_code == 200:
            print("✅ Повідомлення успішно відправлено!")
        else:
            print(f"⚠️ Помилка Telegram: {response.text}")
            
    except Exception as e:
        print(f"❌ Не вдалося відправити: {e}")
        
if __name__ == "__main__":
    send_telegram_message("Привіт! Це перевірка зв'язку 🚀")