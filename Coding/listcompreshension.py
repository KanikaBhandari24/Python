# LIST COMPREHENSION
num=[1,2,3]
new=[n+1 for n in num]
print(new)

name="kanika"
new=[letter for letter in name]
print(new)

double=range(1,5)
new=[n+n for  n in double]
print(new)
#OR
r=[n*2 for n in range(1,5)]
print(r)

#CONDITIONAL LIST COMPREHENSION
name=['Kanika','Kan','Adi','Tarang','Shash','Adia']
new=[n.lower() for n in name if len(n) < 5]
print(new)

name=['Kanika','Kan','Adi','Tarang','Shash','Adia']
new=[n.upper() for n in name if (len(n) > 5)]
print(new)