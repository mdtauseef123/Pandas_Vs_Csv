# with open("weather_data.csv", mode="r") as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv", mode="r") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
#To store temperature, we can do it in a single line
print(data["temp"])

