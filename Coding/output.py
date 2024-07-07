def calc():
    result = 3*2
    return result
calculate = calc()
print(calculate)

def name(fname, lname):
    f = fname.title()  #title changes the first alphabet into uppercase
    l = lname.title()
    print(f"{f} {l}")
name("kanika","bhandari")
