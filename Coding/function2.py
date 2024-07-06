def greet():
    print("Kanika's hobby is swimming")
    print("She is going to take classes for the same")
    print("She will excel in this too!")
greet()

#FUNCTION WITH INPUT
def greetings(name):
    print(f"{name} is going to take classes for the same")
    print(f"{name} will excel in this too!")

greetings("Kanika") 

#FUNCTION WITH MULTIPLE INPUTS
def greet(name, location):
    print(f"My name is {name}")
    print(f"I live in {location}")
#POSITIONAL ARGUMENT - position of argument affects the output
greet("Kanika", "Delhi")

#KEYWORD ARGUMENT - position doesn't affect the output
greet(name="Kanika", location="Delhi")