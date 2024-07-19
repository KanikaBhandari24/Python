#FileNotFound error
with open("file.txt") as f: #file.txt doesn't exist
    f.read()

#KeyError
dict={"key":"value"}
value=dict["non-existent-key"]

#IndexError
list=["Apple","Banana","Mango"]
fruit=list[3] #3 index doesn't exist in the list
print(fruit)

#TypeError
text="abc"
print(text + 5) #str + int?? doesn't happen! 