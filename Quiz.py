from tkinter import *

root = Tk()
root.title("Викторина")
root.geometry("300x400")


def question_one():
    question = Label(root, text="Висит груша, и её нельзя скушать")
    answer = Entry()
    btn = Button(root, text= "Ответить")
    question.grid(row=0)
    answer.grid(row=1)
    btn.grid(row=2)

def question_two():
    question = Label(root, text="")
    answer = Entry()
    btn = Button(root, text="")


question_one()

root.mainloop()

