import requests
import data_manager
from datetime import datetime, timedelta

TEQUILLA_ENDPOINT = 'https://tequila-api.kiwi.com'
TEQUILLA_API_KEY = 'SUPERSECRET'
DEFAULT_CITYCODE = 'MOW'
DEFAULT_CURRENCY = 'RUB'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.xheader = {
            'apikey': TEQUILLA_API_KEY,
        }

        self.today = datetime.now().strftime("%d/%m/%Y")
        self.endday = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")

    def get_destination_code(self, cityname):
        paramset = {
            'term': cityname,
            'locale': 'en-US',
            'location_types': 'city',
            'limit': 1,
        }
        response = requests.get(url=f"{TEQUILLA_ENDPOINT}/locations/query", params=paramset, headers=self.xheader)
        code = response.json()['locations'][0]['code']
        return code

    def search_for_flights(self, citycode, maxprice):
        paramset = {
            'fly_from': DEFAULT_CITYCODE,
            'fly_to': citycode,
            'date_from': self.today,
            'date_to': self.endday,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr': DEFAULT_CURRENCY,
            'price_to': maxprice,
            'max_stopovers': 0,
        }
        response = requests.get(url=f"{TEQUILLA_ENDPOINT}/v2/search", params=paramset, headers=self.xheader)
        flights_data = response.json()
        fs_data = f"from {flights_data['data'][0]['cityFrom']} to {flights_data['data'][0]['cityTo']} for "
              f"{flights_data['data'][0]['price']}")
        return fs_data
