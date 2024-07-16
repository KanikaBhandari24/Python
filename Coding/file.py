# READ A FILE

with open("C:/Users/Kanika Bhandari/OneDrive/Desktop/text.txt") as file:
    content=file.read()
    print(content)
    #NO NEED TO CLOSE THE FILE IN THIS
#OR 
# file=open("text.txt")
# contents=file.read()
# print(contents) 
# file.close()

# #WRITE IN A FILE - IF FILE DOESN'T EXIST THEN IT IS CREATED
# with open("text.txt", "w") as file:
#     file.write("This is the new text.")

# #APPEND METHOD DOESN'T ERASE THE PREVIOUS DATA 
# with open("text.txt", "a") as file:
#     file.write("\nnew line text.")