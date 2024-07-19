# try:
#     file=open("f.txt")
# except:
#     print("File does not exist.") 

# try:
#     file=open("f.txt")
# except:
#     file=open("f.txt","w")
#     file.write("this is file.")

# try:
#     file=open("f.txt")
#     dict={"key":"value"}
#     print(dict["key"]) #doesn't exist
# except FileNotFoundError:
#     file=open("f.txt","w")
#     file.write("this is file.") 
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist.")
# else:
#     content=file.read()
#     print(content)
# finally: #occurs no matter what
#     file.close()
#     print("File was closed")
#     raise TypeError("This is an error that I made.")

h=float(input("Height: "))
w=int(input("Weight: "))
if h>3:
    raise ValueError("Height should not be over 3 meters.")
bmi=w/h**2
print(bmi) 