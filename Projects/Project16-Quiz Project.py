question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

# THE QUESTION CLASS
class question:
    def __init__(self, text, ans):
        self.text = text
        self.answer = ans

#LIST OF QUESTION OBJECTS
question_bank = []
for i in question_data:
    question_text = i["text"]
    question_ans = i["answer"]
    new_q = question(text=question_text, ans=question_ans)
    #OR POSITIONAL PARAMETERS CAN BE USED 👇
    #new_q = question(question_text, question_ans)
    question_bank.append(new_q)
print(question_bank[0].answer)

#TO ASK THE USER TO ANSWER THE QUESTION
class quizbrain:
    def __init__(self, q_list):
        self.q_no = 0
        self.score=0
        self.question_list = q_list

    #NEW METHOD
    def still_has_question(self):
        # if self.q_no < len(self.question_list):
        #     return True
        # else:
        #     return False
        return self.q_no < len(self.question_list) #insted of if-else

    def nextq(self):
        currentq = self.question_list[self.q_no]
        self.q_no += 1
        user_answer = input(f"Q.{self.q_no}: {currentq.text} (True/False): ")
        self.check(user_answer, currentq.answer) #correct answer =currentq.ans
 
    def check(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong answer.") 
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.q_no}")


quiz = quizbrain(question_bank)
while quiz.still_has_question():
    quiz.nextq()
print("Hurray! You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.q_no}") 