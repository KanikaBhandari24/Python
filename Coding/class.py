# class student:
#    def __init__(self, id, name):
#       print("new object is created")

# s1 = student() 
# s1.id = "001"  #id is the attribute 
# s1.name = "Kanika" #name is the attribute
# print(s1.name) 

# s2 = student()
# s2.id = "002"
# s2.name = "Aditya"
# print(s2.name)


# #ANOTHER WAY OF GETTING THE VALUES
# class student:
#    def __init__(self, id, name):
#       self.id = id
#       self.name = name
#       self.follower = 0

# s1 = student("001", "Kanika")
# print(s1.id, s1.name)
# s2 = student("002", "Aditya")
# print(s2.id, s2.name) 


#ADDING METHODS TO A CLASS
class student:
   def __init__(self, id, name):
      self.id = id
      self.name = name
      self.follower = 0
      self.following = 0

   def follow(self):
      student.follower += 1
      student.following += 1

s1 = student("001", "Kanika")
s2 = student("002", "Aditya")

s1.follow(s2)
print(s1.follower)
print(s1.following)
print(s2.follower)
print(s2.following)
