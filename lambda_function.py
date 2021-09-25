import json
import warnings
import requests
from bs4 import BeautifulSoup
from discord import Webhook, RequestsWebhookAdapter


warnings.filterwarnings('ignore')


class Size:
    XXS = 0
    XS = 1
    S = 2
    M = 3
    L = 4
    XL = 5
    XXL = 6


TYPE_NEW_BIKE = 'NEW BIKE'
TYPE_OUTLET = 'OUTLET'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}


# list here all the url for all bikes you want to check
bikes_factory = [
    # endurance
    'https://www.canyon.com/en-ro/road-bikes/endurance-bikes/endurace/cf-sl/endurace-cf-sl-8-disc/2948.html?dwvar_2948_pv_rahmenfarbe=BU%2FBK',
]

# if there is any bike that you want to ignore
bikes_to_ignore = {
    'https://www.canyon.com/en-de/gravel-bikes/all-road/grail/al/grail-7/2370.html?dwvar_2370_pv_rahmenfarbe=SR%2FBK',
}

# list also the outlet pages in case u want a SH bike
# (make sure that you filter by your size )
outlet_urls = [
    'https://www.canyon.com/en-ro/outlet-bikes/?hideSelectedFilters=true&prefn1=pc_outlet&prefn2=pc_rahmengroesse&prefv1=true&prefv2=M',
    'https://www.canyon.com/en-ro/new-outlet-bikes/?cgid=new-outlet-bikes&prefn1=pc_rahmengroesse&prefv1=M&srule=sort_last_added',
    'https://www.canyon.com/en-ro/factory-seconds-outlet-bikes/?cgid=factory-seconds-outlet-bikes&prefn1=pc_rahmengroesse&prefv1=M&srule=sort_last_added'
]

# bikes name (substring) that u want to search in outlet
outlet_bikes = ['Endurace']
outlet_bikes_to_ignore = ['Endurace CF SL 8 DISC Di2', ]


discord_webhook_url = '***'
discord_user = '<@ *** >'


def find_bike(url, size, text_to_check='Sold out'):
    html = requests.get(url, headers=headers, timeout=10, verify=False)
    soup = BeautifulSoup(html.content, 'html.parser')
    all_bike_size = soup.findAll(
        'div', {'class': 'productConfiguration__availabilityMessage'})
    my_size = all_bike_size[size].text.strip()
    return my_size != text_to_check


def find_bike_outlet(url, bikes):
    html = requests.get(url, headers=headers, timeout=10, verify=False)
    soup = BeautifulSoup(html.content, 'html.parser')
    all_bikes = soup.findAll(
        'div', {'class': 'productTile__productName'})
    for bike in all_bikes:
        bike_name = bike.text.strip()
        if bike_name in outlet_bikes_to_ignore:
            continue
        if any(map(bike_name.__contains__, bikes)):
            return True
    return False


def notify(bike, url_type, webhook=None):
    if not webhook:
        webhook = Webhook.from_url(
            discord_webhook_url, adapter=RequestsWebhookAdapter())
    print(bike)
    webhook.send(
        f'Hurry-up {discord_user}! [{url_type}] Please check the following page: {bike}')


def collect_available_bikes():
    bikes_in_stock = set()

    for bike in bikes_factory:
        bike_available = find_bike(bike, size=Size.M)
        if bike_available:
            bikes_in_stock.add(bike)

    bikes_in_stock = bikes_in_stock - bikes_to_ignore
    return bikes_in_stock


def lambda_handler(event, context):

    # check brand new bikes from collection
    available_bikes = collect_available_bikes()
    for bike in available_bikes:
        notify(bike, TYPE_NEW_BIKE)

    # check outlet bikes
    for url in outlet_urls:
        is_available = find_bike_outlet(url, outlet_bikes)
        if is_available:
            notify(url, TYPE_OUTLET)

    return {
        'statusCode': 200,
        'body': json.dumps('Checker finished succesfully!')
    }
