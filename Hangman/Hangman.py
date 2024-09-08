import random
from tkinter import Canvas
import tkinter as tk

words = ['travel', 'person', 'strong', 'street', 'turtle', 'purple', 'orange',
     'potato', 'august', 'better', 'breath', 'market', 'repair', 'school',
     'colony', 'online', 'carrot', 'rabbit', 'doctor']

hangman_lines = [(220, 185, 220, 250), (220, 200, 240, 240),(220, 200, 200, 240),(220, 245, 240, 280), (220, 245, 200, 280)]

def list_to_print(ls):
    return ' '.join(str(x) for x in ls)



class Hangman:
    def __init__(self):
        self.master = tk.Tk()
        self.canvas = Canvas(self.master, width=500, height=500)
        self.guess = ['_' for c in range(6)]
        self.guess_id = None
        self.letter = None
        self.word = random.choice(words)
        self.count = 0

    def create_circle(self, x, y, r):
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, width=5)


    def change_status(self, letter):
        indexes = [i for i in range(len(self.word)) if self.word[i] == letter]
        for i in indexes:
            self.guess[i] = letter
        self.canvas.itemconfig(self.guess_id, text=self.guess)

    def add_line_to_hangman(self):
        if self.count != 0:
            self.canvas.create_line(hangman_lines[self.count-1], width=5)
        else:
            self.create_circle(220, 170, 15)
        self.count+=1

    def check_guess(self):
        letter = self.letter.get()
        if self.count == 6:
            self.canvas.create_text(230, 100, text="Game Over", fill="Red", font=100)
        elif letter in self.word:
            self.change_status(letter)
            if ''.join(self.guess) == self.word:
                print("You guessed the word!")
        elif self.count < 6:
            self.add_line_to_hangman()


    def initialize_game(self):
        self.master.title("Hangman")
        self.master.geometry("500x500")
        self.canvas.pack()
        self.canvas.create_line(200, 300, 300, 300, width=5)
        self.canvas.create_line(270, 130, 270, 300, width=5)
        self.canvas.create_line(220, 130, 270, 130, width=5)
        self.canvas.create_line(220, 130, 220, 160, width=5)
        self.canvas.create_text(250, 400, text="Please guess your next letter:", fill="black", font=50)
        self.guess_id = self.canvas.create_text(250,350, text=' '.join(self.guess), fill="black", font=("Purisa", 25))
        self.letter = tk.Entry(self.master)
        self.canvas.create_window(220, 450, window=self.letter, height=30)
        button_widget = tk.Button(text='guess', command=self.check_guess)
        self.canvas.create_window(310, 450, window=button_widget)
        self.master.mainloop()







p1 = Hangman()
p1.initialize_game()


