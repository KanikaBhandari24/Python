from tkinter import *
def convert():
    mile=float(miles.get())
    kms=mile * 1.609
    kmresult_label.config(text=f"{kms}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

miles=Entry(width=10, font=15)
miles.grid(column=1, row=0)
miles_label=Label(text="Miles", font=15)
miles_label.grid(column=2, row=0)

equal_label=Label(text="is equal to", font=15)
equal_label.grid(column=0, row=1)

kmresult_label=Label(text=0, font=15)
kmresult_label.grid(column=1, row=1)
km_label=Label(text="Km", font=15)
km_label.grid(column=2, row=1)

calc=Button(text="Calculate", command=convert, font=10)
calc.grid(column=1, row=2)

window.mainloop()