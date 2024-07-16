# with open("/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/CSV files/weather_data.csv") as file:
#     data = file.readlines()
#     print(data) 

import csv
with open("/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/CSV files/weather_data.csv") as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

"""Instead of the above 8 lines, a specific col can be printed using the below 3 lines using pandas"""

import pandas 
data = pandas.read_csv("/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/CSV files/weather_data.csv")
print(type[data]) 
print(type(data["day"]))