from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer1=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer1)
    canvas.itemconfig(timer, text="00:00")
    timer.config(text="Timer")
    tick.config(text="")
    global reps
    reps=0 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def time():
    global reps
    reps +=1
    work_sec= WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60 
    if reps % 8 == 0:
        count(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 ==0:
        count(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count(work_sec)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count(down):
    down_min = math.floor(down/60)
    down_sec = down % 60
    #DYNAMIC TYPING
    if down_sec<10:
        down_sec=f"0{down_sec}"

    canvas.itemconfig(timer, text=f"{down_min}:{down_sec}")
    if down>0:
        global timer1
        timer1=window.after(1000, count, down-1)  
    else:
        time()
        mark =""
        for i in range(math.floor(reps/2)):
            mark += "✔"
        tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)  

timer=Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
timer.grid(column=1, row=0)

#Image setup
canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img=PhotoImage(file="/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Pomodoro Project/tomato.png")
canvas.create_image(100, 110, image=img)
timer=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start=Button(text="Start", highlightthickness=0, command=time)
start.grid(column=0, row=2)

reset=Button(text="Reset", highlightthickness=0, command=reset)
reset.grid(column=2, row=2)

tick=Label(fg=GREEN, bg=YELLOW, font=20)
tick.grid(column=1, row=3)


window.mainloop()