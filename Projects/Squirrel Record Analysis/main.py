import pandas
data = pandas.read_csv("/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Squirrel data analysis/file.csv")
gray=len(data[data["Primary Fur Color"] == "Gray"])
red=len(data[data["Primary Fur Color"] == "Cinnamon"])
black=len(data[data["Primary Fur Color"] == "Black"]) 
print(gray)
print(red)
print(black)

dict = {
    "Fur":["Gray","Cinnamon","Black"] ,
    "count": [{gray},{red},{black}]
}
df = pandas.DataFrame(dict)
df.to_csv("Squirrel data analysis count.csv")