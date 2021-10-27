# Check if you bike url has the following size options: xxs, xs etc.
# Otherwise you need to update the size enum acordingly. 
class SIZE:
    XXS = 0
    XS = 1
    S = 2
    M = 3
    L = 4
    XL = 5
    XXL = 6

# Contact the owner of the server to provide you the user_id and webhook_url information.
DISCORD_USER = '<@123456789>'
DISCORD_WEBHOOK_URL = 'https://discordapp.com/api/webhooks/###'

MY_SIZE_OPTIONS = [SIZE.S, SIZE.M]

# List here all the url for all bikes you want to checkl
NEW_BIKES_TO_CHECK = [
    # grail
    'https://www.canyon.com/en-ro/gravel-bikes/all-road/grail/al/grail-7/2370.html?dwvar_2370_pv_rahmenfarbe=GN%2FBK',
    'https://www.canyon.com/en-ro/gravel-bikes/all-road/grail/al/grail-7/2370.html?dwvar_2370_pv_rahmenfarbe=SR%2FBK', 
    'https://www.canyon.com/en-ro/gravel-bikes/all-road/grail/al/grail-6/2369.html?dwvar_2369_pv_rahmenfarbe=SR%2FBK',
    # grail cf
    'https://www.canyon.com/en-ro/gravel-bikes/all-road/grail/cf-sl/grail-cf-sl-7/2374.html?dwvar_2374_pv_rahmenfarbe=GY%2FBK',
    'https://www.canyon.com/en-ro/gravel-bikes/all-road/grail/cf-sl/grail-cf-sl-7/2374.html?dwvar_2374_pv_rahmenfarbe=BU%2FBK',
    'https://www.canyon.com/en-ro/gravel-bikes/all-road/grail/cf-sl/grail-cf-sl-8/2717.html?dwvar_2717_pv_rahmenfarbe=BU%2FBK',
    'https://www.canyon.com/en-ro/gravel-bikes/all-road/grail/cf-sl/grail-cf-sl-8/2717.html?dwvar_2717_pv_rahmenfarbe=GY%2FBK'

    #test
    # 'https://www.canyon.com/en-de/gravel-bikes/bike-packing/grizl/cf-slx/grizl-cf-slx-8-di2/2968.html?dwvar_2968_pv_rahmenfarbe=GN%2FBK'
]

# If there is any bike that you want to ignore so you don't receive notifications about it.
NEW_BIKES_TO_IGNORE = {''}

# List also the outlet pages in case you want a second-hand bike.
# Make sure that you filter the pages by your size.
OUTLET_PAGE = [
    'https://www.canyon.com/en-ro/outlet-bikes/?cgid=outlet&prefn1=pc_rahmengroesse&prefv1=S%7CM&searchType=outlet',
    'https://www.canyon.com/en-ro/new-outlet-bikes/?cgid=new-outlet-bikes&prefn1=pc_rahmengroesse&prefv1=S%7CM&srule=sort_last_added', 
    'https://www.canyon.com/en-ro/factory-seconds-outlet-bikes/?cgid=factory-seconds-outlet-bikes&prefn1=pc_rahmengroesse&prefv1=S%7CM&srule=sort_last_added'
]

# Bikes name (substring) that u want to search in outlet.
OUTLET_BIKES = ['Grail']
# Full name of the bike you wish to ignore.
OUTLET_BIKES_TO_IGNORE = []
