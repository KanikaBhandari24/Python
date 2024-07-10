#DEBUG PROBLEM 1
def fun():
    for i in range(1, 21):   #debugged issue -> range(1, 20)
        if i == 20:
            print("You reached 20.")
fun()


#DEBUG PROBLEM 2
from random import randint
img = ["1","2","3","4","5","6"]
num = randint(0, 5)    #debugges issue -> randint(1,6), list starts from 0 index
print(img[num])


#DEBUG PROBLEM 3
year = int(input("What is your age?"))
if year>1980 and year<1994:
    print("You are millenial")
elif year>=1994:
    print("You are Gen Z")