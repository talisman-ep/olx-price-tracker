import sys
import os
import time
import random
from parser import get_olx_price
from storage import save_price, load_price
from notifier import send_telegram_message

if sys.platform == 'win32':
    os.system('chcp 65001 >nul')
sys.stdout.reconfigure(encoding='utf-8')

URL = "https://www.olx.ua/d/uk/obyavlenie/vdeokarta-asus-tuf-rtx-4070ti-gaming-oc-12gb-IDZDawP.html"

CHECK_INTERVAL = 3600 

def run():
    print("--- THE HUNTER IS RUNNING (Press Ctrl+C to stop) ---")
    send_telegram_message("Бот запущений і почав полювання!")

    while True:
        try:
            print(f"\n[INFO] Checking price at {time.strftime('%H:%M:%S')}...")

            current_price = get_olx_price(URL)
            
            if not current_price:
                print("Error: Could not get price. Skipping...")
            else:
                print(f"Current Price: {current_price} UAH")
    
                old_price = load_price()
                
                if old_price is None:
                    print("First run. Saving price.")
                    save_price(current_price)
                
                elif current_price != old_price:
                    if current_price < old_price:
                        diff = old_price - current_price
                        msg = f"<b>ЦІНА ВПАЛА!</b>\nБуло: {old_price} грн\nСтало: {current_price} грн\nЗнижка: <b>{diff} грн</b> \n<a href='{URL}'> КУПУВАТИ ТУТ</a>"
                        send_telegram_message(msg)
                    else:
                        print("Price increased.")

                    save_price(current_price)
                else:
                    print("zzz... Price is stable.")

            sleep_time = CHECK_INTERVAL + random.randint(1, 300)
            print(f"Sleeping for {sleep_time} seconds...")
            time.sleep(sleep_time)

        except Exception as e:
            print(f"CRITICAL ERROR: {e}")
            time.sleep(60)

if __name__ == "__main__":
    run()
