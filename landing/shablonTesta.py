import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Тест по физике")
window.geometry('600x300')

def otveti():
   correct_answers = 0
   answer1 = str(q1_an.get())
   answer2 = str(q2_an.get())
   answer3 = str(q3_an.get())
   answer4 = str(q4_an.get())
   answer5 = str(q5_an.get())
   if answer1 == 'физика':
      correct_answers = correct_answers + 1
   if answer2 == 'телескоп':
      correct_answers = correct_answers + 1
   if answer3 == '100':
      correct_answers = correct_answers + 1
   if answer4 == 'мензурка':
      correct_answers = correct_answers + 1
   if answer5 == 'килограмм':
      correct_answers = correct_answers + 1
   messagebox.showinfo('Кольичество правильных ответов', f'У вас правильных ответов: {correct_answers} из 5, ваша оценка: {correct_answers}' )

frame = Frame(
   window, 
   padx = 10, 
   pady = 10 
)

frame.pack(expand=True)
q1 = Label(
   frame,
   text="Первый вопрос: Наука, изучающая разнообразные явления природы?"
)
q1.grid(row=3, column=1)

q2 = Label(
   frame,
   text="Второй вопрос: Прибор для изучения небесных тел?",
)
q2.grid(row=4, column=1)

q3 = Label(
   frame,
   text="Третий вопрос: Сколько сантиметров в одном метре?",
)
q3.grid(row=5, column=1)

q4 = Label(
   frame,
   text="Четвёртый вопрос: Каким прибором измеряют объем жидкости?",
)
q4.grid(row=6, column=1)

q5 = Label(
   frame,
   text="Пятый вопрос: Основная единица массы в Международной системе единиц (СИ)",
)
q5.grid(row=7, column=1)

q1_an = Entry(
   frame, 
)
q1_an.grid(row=3, column=2, pady=5)

q2_an = Entry(
   frame,
)
q2_an.grid(row=4, column=2, pady=5)

q3_an = Entry(
   frame, 
)
q3_an.grid(row=5, column=2, pady=5)

q4_an = Entry(
   frame, 
)
q4_an.grid(row=6, column=2, pady=5)

q5_an = Entry(
   frame, 
)
q5_an.grid(row=7, column=2, pady=5)

button = Button(
   frame, 
   text='Ответить', 
   command=otveti
)
button.grid(row=8, column=2)

window.mainloop()