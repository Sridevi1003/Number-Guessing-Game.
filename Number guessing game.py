
from tkinter import *
import random

window = Tk()
window.title("NUMBER GUESSING GAME")
window.geometry("540x450")
window.configure(bg='PaleTurquoise2')

chance_var = IntVar()


def new_game():
    global num, chance
    chance = 0
    guessInput.delete(0, "end")
    comment.delete(0, "end")
    chanceentry.delete(0, "end")
    guessButton.config(state='normal')
    num = random.randint(1, 100)


def play_game():
    global chance
    numGuess = int(guessInput.get())
    chance += 1
    if numGuess < num:
        comment.delete(0, "end")
        comment.insert(0, "Hint: Try higher number!!")
    elif numGuess > num:
        comment.delete(0, "end")
        comment.insert(0, " Hint: Try smaller number!!")
    else:
        comment.delete(0, "end")
        comment.insert(0, " CONGRATULATIONS!! Successfully You Won the game ")
    chance_var.set(chance)


label = Label(text="Guess a number between 1 to 100", font=("Arial", 15, "bold"), bg='PaleTurquoise2')
label.grid(row=0, column=0)
guessInput = Entry(font=("bold", 14), width=8)
guessInput.grid(row=2, column=0, padx=10, pady=10)
comment = Entry(font=("bold", 14), bg='PaleTurquoise2', fg='navy', bd=0)
comment.grid(row=4, column=0, padx=20, pady=20)
chanceLabel = Label(text=" Number of guesses you have made :", font=("bold", 14), bg='PaleTurquoise2')
chanceLabel.grid(row=5, column=0)
chanceentry = Entry(font=("bold", 14), width=4, textvariable=chance_var, bd=0, bg= 'PaleTurquoise')
chanceentry.grid(row=5, column=0, sticky='e')
chanceentry.delete(0, "end")

startButton = Button(text="start/restart  game", bg="green", fg="white", font=("bold", 14), command=new_game)
startButton.grid(row=1, column=0, padx=10, pady=20)
guessButton = Button(text="Guess", bg="brown", fg="white", font=("bold", 14), state='disabled', command=play_game)
guessButton.grid(row=3, column=0, padx=10, pady=10)
exitButton = Button(text="EXIT GAME", bg="green", fg="white", font=("bold", 14), command=window.destroy)
exitButton.grid(row=6, column=0, pady=20)

window.mainloop()

