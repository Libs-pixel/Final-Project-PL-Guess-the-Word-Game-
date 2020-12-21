import tkinter
from tkinter import *
import random
from tkinter import messagebox


root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Guess the word")
root.configure(background="#9daab8")

words = [
    "pteacher",
    "java",
    "flask",
    "bishkek",
    "final",
    "exam",
    "console",
    "javascript",
    "html",
    "css3",
    "meme",
    "sorry",
    "pycharm",
    "alatoo",
]

qwords = [
    "erhteacp",
    "avja",
    "lfaks",
    "bkekish",
    "inalf",
    "xame",
    "solenco",
    "iscjavptia",
    "tmhl",
    "s3cs",
    "emme",
    "armchapy",
    "toolaa",
]


num = random.randrange(0, len(qwords), 1)


def default():
    global qwords, words, num
    lbls.config(text=qwords[num])


def res():
    global words, qwords, num
    num = random.randrange(0, len(qwords), 1)
    lbls.config(text=qwords[num])
    entr.delete(0, END)


def checkans():
    global qwords, words, num
    var = entr.get()
    if var == words[num]:
        messagebox.showinfo("Success", "This is a correct answer!")
        res()
    else:
        messagebox.showerror("Error", "Try again :(")
        e1.delete(0, END)


AddWindow = Frame(root, width=600, height=100, bd=1, relief=SOLID)
AddWindow.pack(side=TOP, pady=20)

lbl_text = Label(AddWindow, text="Guess the next word",
                 font=('Helvetica', 18), width=600)
lbl_text.pack(fill=X)

lbls = Label(
    root,
    text="Your here",
    font=("Helvetica", 18),
    bg="#8cabca",
    fg="#af00db",

)
lbls.pack(pady=30, ipady=10, ipadx=10)


ans = StringVar()
entr = Entry(
    root,
    font=("Helvetica", 16),
    textvariable=ans,
)
entr.pack(ipady=5, ipadx=5)

btncheck = Button(
    root,
    text="Check",
    font=("Helvetica", 16),
    width=16,
    bg="#5757ff",
    fg="#57a2ff",
    relief=GROOVE,
    command=checkans,
)
btncheck.pack(pady=40)

btnreset = Button(
    root,
    text="Reset",
    font=("Helvetica", 16),
    width=16,
    bg="#6905f5",
    fg="#be93c2",
    relief=GROOVE,
    command=res,
)
btnreset.pack()

default()
root.mainloop()
