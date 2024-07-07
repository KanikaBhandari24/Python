dict={"Fruit":"Mango", "Vegetable":"Potato"}
print(dict["Fruit"])

for key in dict:
    #Only prints the key
    print(key)
    #prints the value 
    print(dict[key])

# Lists as values
capitals = {"France": ["Paris, Lille"],
            "Germany": {"cities_visited":["Berlin", "Hamburg"], "total_visits":12}}

print(capitals) 