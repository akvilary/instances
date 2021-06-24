import requests
import data_manager
import flight_search
import notification_manager

manage_data = data_manager.DataManager()
sheet_data = manage_data.get_destination_data()

if manage_data.is_there_empty_destination_code():
    manage_data.update_destination_data()

f_search = flight_search.FlightSearch()
f_data = {}

for destination in sheet_data:
    f_data.append(f_search.search_for_flights(destination['iataCode'], destination['lowestPrice']))

notificator = notification_manager.NotificationManager()
notificator.send_me_email(f_data)


