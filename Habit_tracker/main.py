import requests
from datetime import datetime

NOW = datetime.now()
DATE = NOW
# If you need another date, then comment out code below
# DATE = datetime(year=2021, month=5, day=24)
DATE = DATE.strftime('%Y%m%d')

TOKEN = 'SUPERSECRET'
USERNAME = 'akvilary'
GRAPH_ID = 'graph1'

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
PIXELA_GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
PIXELA_PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'
PIXELA_EXACT_PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',

}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

header_info = {
    'X-USER-TOKEN': TOKEN,

}

graph_config = {
    'id': GRAPH_ID,
    'name': 'Coding graph',
    'unit': 'min',
    'type': 'int',
    'color': 'ajisai',

}

pixel_config = {
    'date': DATE,
    'quantity': input("How many minutes did you code? "),

}

update_pixel = {
    'quantity': '120',
}

# create_graph = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_config, headers=header_info)
# print(create_graph.text)

create_pixel = requests.post(url=PIXELA_PIXEL_ENDPOINT, json=pixel_config, headers=header_info)
print(create_pixel.text)

# update_exact_pixel = requests.put(url=PIXELA_EXACT_PIXEL_ENDPOINT, json=update_pixel, headers=header_info)
# print(update_exact_pixel.text)

# delete_pixel = requests.delete(url=PIXELA_EXACT_PIXEL_ENDPOINT, headers=header_info)
# print(delete_pixel.text)