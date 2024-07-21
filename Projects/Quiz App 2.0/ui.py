from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#7091E6" 

class QuizUI:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label=Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Courier", 15, "bold")) 
        self.score_label.grid(row=0, column=1) 

        self.canvas=Canvas(width=300, height=250, bg="white")
        self.question_text=self.canvas.create_text(150, 125, width=250, text="Some Question Text", fill=THEME_COLOR, font=("Courier", 20, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        trueimg=PhotoImage(file="Quiz App 2.0/images/true.png") 
        self.true=Button(image=trueimg, highlightthickness=0, command=self.true)
        self.true.grid(row=2, column=0)
        falseimg=PhotoImage(file="Quiz App 2.0/images/false.png")
        self.false=Button(image=falseimg, highlightthickness=0, command=self.false)
        self.false.grid(row=2, column=1) 

        self.get_next_question()

        self.window.mainloop() 

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():    
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text) 
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true(self):
        self.feedback(self.quiz.check_answer("True"))

    def false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, right):
        if right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)