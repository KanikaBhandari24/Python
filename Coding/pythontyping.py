# age:int
# name:str
# height:float

def check(age: int): 
    if age>18:
        drive=True
    else:
        drive=False
    return drive

print(check(19))