import pandas
import csv
data=pandas.read_csv("/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/CSV files/weather_data.csv")
# print(type[data])         #DATAFRAME DS
# print(type(data["temp"])) #SERIES DS 
dic=data.to_dict()
print(dic) 
list=data["temp"].to_list()
print(list) 

#BOTH WILL GIVE AVERAGE OF TEMPERATURE
print(data["temp"].mean())
#OR
avg = sum(list)/len(list)
print(avg)

"""TO COUNT MAXIMUM"""
print(data["temp"].max())

#GET DATA IN COLUMNS
print(data["condition"]) 
#OR
print(data.condition)

#GET DATA IN ROW
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

#create a DATAFRAME
data={
    "student":["Kanika","Adi","Jam"],
    "score":[90, 92, 56]
}
d=pandas.DataFrame(data)
#print(d)
d.to_csv("new.csv") 