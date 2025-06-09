import requests
from bs4 import BeautifulSoup
import time
from plyer import notification


# Replace this with your desired Amazon product URL
url = 'https://www.amazon.com/HP-962-Cartridge-Cyan-3HZ96AN/dp/B07M8PH5JS?pd_rd_w=xnkVP&content-id=amzn1.sym.545f2ac1-7392-463d-83f6-77ac6b95c5ce&pf_rd_p=545f2ac1-7392-463d-83f6-77ac6b95c5ce&pf_rd_r=9X46JT1RYNHGC8Y6CQCY&pd_rd_wg=5XwB3&pd_rd_r=f27d9110-855e-404e-9c5e-0bee5ed46ccd&pd_rd_i=B07M8PH5JS&ref_=pd_bap_d_grid_rp_0_1_ec_pd_hp_d_atf_rp_4_i&th=1'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

target_price = 28.00  # Set your target price here

def get_price():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_span = soup.find('span', class_='a-offscreen')
        if price_span:
            price_str = price_span.get_text().strip().replace('$', '').replace(',', '')
            return float(price_str)
        else:
            print("⚠️ Price not found. Amazon may have blocked this request.")
    else:
        print(f"Failed to retrieve the page. Status: {response.status_code}")
    return None

while True:
    price = get_price()
    if price:
        print(f"Current price: ${price}")
        if price <= target_price:
            notification.notify(
                title='💰 Amazon Price Drop Alert!',
                message=f'Price is now ${price}!\n{url}',
                timeout=10  # seconds
            )
            print("🚨 Price dropped! Notification sent.")
            break  # Exit after alert
    time.sleep(10)  # Wait 1 hour before checking agai
