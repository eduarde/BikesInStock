import json
import warnings
import requests
from bs4 import BeautifulSoup
from discord import Webhook, RequestsWebhookAdapter
from app.variables import (
    DISCORD_USER, DISCORD_WEBHOOK_URL, MY_SIZE_OPTIONS, 
    NEW_BIKES_TO_CHECK, NEW_BIKES_TO_IGNORE,
    OUTLET_PAGE_LIST, OUTLET_BIKES, OUTLET_BIKES_TO_IGNORE
)

warnings.filterwarnings('ignore')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

TYPE_NEW_BIKE = 'NEW BIKE'
TYPE_OUTLET = 'OUTLET'

def notify(bike, url_type, webhook=None):
    if not webhook:
        webhook = Webhook.from_url(DISCORD_WEBHOOK_URL, adapter=RequestsWebhookAdapter())
    print(bike)
    webhook.send(f'Howdy {DISCORD_USER}! [{url_type}] I found your size in stock. Check the following page: {bike}')

def find_bike(url, size, status='Sold out'):
    html = requests.get(url, headers=headers, timeout=10, verify=False)
    soup = BeautifulSoup(html.content, 'html.parser')
    all_bike_size = soup.findAll('div', {'class': 'productConfiguration__availabilityMessage'})
    my_size_status = all_bike_size[size].text.strip()
    return my_size_status != status


def find_bike_outlet(url, bikes):
    html = requests.get(url, headers=headers, timeout=10, verify=False)
    soup = BeautifulSoup(html.content, 'html.parser')
    all_bikes = soup.findAll('div', {'class': 'productTile__productName'})
    for bike in all_bikes:
        bike_name = bike.text.strip()
        if bike_name in OUTLET_BIKES_TO_IGNORE:
            continue
        if any(map(bike_name.__contains__, bikes)):
            return True
    return False

def collect_available_bikes(size):
    bikes_in_stock = set()

    for bike in NEW_BIKES_TO_CHECK:
        bike_available = find_bike(bike, size=size)
        if bike_available:
            bikes_in_stock.add(bike)
    bikes_in_stock = bikes_in_stock - NEW_BIKES_TO_IGNORE
    
    return bikes_in_stock


def lambda_handler(event, context):

    available_bikes = set()
    # check brand new bikes from collection
    for size in MY_SIZE_OPTIONS:
        available_bikes.update(collect_available_bikes(size=size))
    for bike in available_bikes:
        notify(bike, TYPE_NEW_BIKE)

    # check outlet bikes
    for url in OUTLET_PAGE_LIST:
        is_available = find_bike_outlet(url, OUTLET_BIKES)
        if is_available:
            notify(url, TYPE_OUTLET)

    return {
        'statusCode': 200,
        'body': json.dumps('URLS CHECKED SUCCESFULLY!')
    }
