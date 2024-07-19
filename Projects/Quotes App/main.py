from tkinter import *
import requests

#API CALLING
def get_quote():
    response=requests.get(url="https://dummyjson.com/quotes/random")
    response.raise_for_status()
    data=response.json()
    quote=data["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("Quote Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Quotes App project/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Quote Goes HERE", width=250, font=("Courier", 20, "bold"), fill="white") 
canvas.grid(row=0, column=0)

img = PhotoImage(file="Quotes App project/quote6.png")
button = Button(image=img, highlightthickness=0, command=get_quote)
button.grid(row=1, column=0)


window.mainloop() 