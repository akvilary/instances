import requests
import flight_search

SHEETY_ENDPOINT = 'https://api.sheety.co/7427e165a7ddef6ac6de2ca00e62e542/flightDeals/prices'


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        self.destination_data = response.json()['prices']
        return self.destination_data

    def is_there_empty_destination_code(self):
        for destination in self.destination_data:
            print(destination)
            try:
                if destination['iataCode'] == '':
                    return True
                    break
            except KeyError:
                return True

    def update_destination_data(self):
        fdb = flight_search.FlightSearch()
        for destination in self.destination_data:
            data_to_update = {
                'price': {
                'city' : destination['city'],
                'iataCode' : fdb.get_destination_code(destination['city']),
                }
            }

            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{destination['id']}",
                json=data_to_update
            )
            print(response.text)
