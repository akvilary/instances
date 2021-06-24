import pandas

# data = pandas.read_csv("./weather_data.csv")
# monday = data[data.day == 'Monday'].condition
#
# print(monday)

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == 'Gray'])
print(gray)