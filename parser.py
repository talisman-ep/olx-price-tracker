import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_olx_price(url):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            script_tag = soup.find("script", {"type": "application/ld+json"})
            
            if script_tag:
                data = json.loads(script_tag.text)
                return data['offers']['price']
    except Exception as e:
        print(f"Error parsing: {e}")
    
    return None