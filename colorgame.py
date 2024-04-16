from tkinter import *
import random

win = Tk()
win.title("Color Game")
win.geometry("400x200")

colors = ['white', 'red', 'blue', 'green', 'orange', 'pink', 'purple', 'black']
score = 0
timeleft = 30

def start(event):
    scorelbl.configure(text="Score: 0")
    if timeleft == 30:
        countdown()
    nextcolor()

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timelbl.configure(text=f"Time Left: {str(timeleft)}")
        timelbl.after(1000, countdown)
    else:
        timelbl.configure(text="You lost!", fg="red")
        win.unbind('<Return>')
        colorentry.configure(state="disabled")

def nextcolor():
    global score

    print(colors)

    if colorentry.get().lower() == colors[1].lower():
        score += 1
        scorelbl.configure(text=f"Score:{score}")
        print(score)

    colorentry.delete(0, END)

    random.shuffle(colors)

    colorfg = colors[1]
    textcolor = colors[0]

    colortext.configure(text=textcolor, fg=colorfg)

gamelbl = Label(win, text="Type in the color of the words, and not the word text!")
gamelbl.pack()

scorelbl = Label(win, text="Press enter to start!")
scorelbl.pack()

timelbl = Label(win, text="Time Left:30")
timelbl.pack()

colortext = Label(win, text="Start!", font=("Tahoma", 50))
colortext.pack()

colorentry = Entry(win)
colorentry.pack()

win.bind("<Return>", start)

win.mainloop()
