import requests
from bs4 import BeautifulSoup


def parse_iphone_prices(url):
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')

    iphone_prices = []
    for price_tag in soup.find_all('div', class_='product-card__price'):
        price = price_tag.get_text().replace(' ', '').replace('₽', '').replace('от', '').replace('Цена', '')
        iphone_prices.append(int(price))

    if iphone_prices:
        min_price = min(iphone_prices)
        max_price = max(iphone_prices)
        avg_price = sum(iphone_prices) / len(iphone_prices)
    else:
        min_price, max_price, avg_price = 0, 0, 0

    return min_price, max_price, avg_price

url = 'https://omsk.lstore.ru/phones?utm_source=yandex&utm_medium=cpc&utm_campaign=107507281&utm_content=15844966908&utm_term=купить%20айфон&yclid=7667458319298068479'
min_price, max_price, avg_price = parse_iphone_prices(url)

print(f"Min price: {min_price} руб.")
print(f"Max price: {max_price} руб.")
print(f"Avg price: {avg_price} руб.")