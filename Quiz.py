from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина")
root.geometry("300x300")


def question_one():
    question = Label(root, text="Висит груша, и её нельзя скушать")
    answer = Entry()
    btn = Button(root, text="Ответить", command=lambda: game1(question_two))
    question.grid()
    answer.grid()
    btn.grid()

    def game1(question_two):
        if answer.get().lower() == "лампочка":
            question_two()
        else:
            messagebox.showerror("Ошибка!", "Попробуй еще раз!")


def question_two():
    question_2 = Label(root, text="Зимой и летом одним цветом")
    answer_2 = Entry()
    btn_2 = Button(root, text="Ответить", command=lambda: game2(question_two))
    question_2.grid()
    answer_2.grid()
    btn_2.grid()

    def game2(question_two):
        if answer_2.get().lower() == "ёлка":
            messagebox.showinfo("Победа", "Ты молодец!")
        else:
            messagebox.showerror("Ошибка", "Попрообуй еще раз!")


question_one()

root.mainloop()
