from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, pady=20, padx=10)

        self.score_label = Label(text="Score: 0",
                                 font="Arial 20 italic", bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.q_canva = Canvas(width=300, height=250, bg='white')
        self.question_text = self.q_canva.create_text(
            150,
            125,
            width=280,
            fill="black",
            font="Times 20 italic",
            text="There will be question")
        self.q_canva.grid(row=1,column=0, columnspan=2, pady=20)

        self.true_image = PhotoImage(file=r'./images/true.png')
        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0, padx=30)

        self.false_image = PhotoImage(file=r'./images/false.png')
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1, padx=30)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.q_canva.config(bg='white')

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.q_canva.itemconfig(self.question_text, text=q_text)

        else:
            self.q_canva.itemconfig(self.question_text, text="You've reached the end of the quizz.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.q_canva.config(bg='green')
        else:
            self.q_canva.config(bg='red')

        self.window.after(1000, self.get_next_question)