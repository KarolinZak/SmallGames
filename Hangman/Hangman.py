import random
from tkinter import Canvas
import tkinter as tk

words = ['travel', 'person', 'strong', 'street', 'turtle', 'purple', 'orange',
         'potato', 'august', 'better', 'breath', 'market', 'repair', 'school',
         'colony', 'online', 'carrot', 'rabbit', 'doctor']

hangman_lines = [(220, 185, 220, 250), (220, 200, 240, 240), (220, 200, 200, 240),
                 (220, 245, 240, 280), (220, 245, 200, 280)]


class Hangman:
    def __init__(self):
        self.master = tk.Tk()
        self.canvas = Canvas(self.master, width=500, height=500)
        self.guess = ['_' for _ in range(6)]
        self.guess_id = None
        self.word = random.choice(words)
        self.count = 0
        self.buttons = {}  # Dictionary to hold button references
        self.initialize_game()

    def create_circle(self, x, y, r):
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, width=5)

    def change_status(self, letter):
        indexes = [i for i in range(len(self.word)) if self.word[i] == letter]
        for i in indexes:
            self.guess[i] = letter
        self.canvas.itemconfig(self.guess_id, text=' '.join(self.guess))

    def add_line_to_hangman(self):
        if self.count != 0:
            self.canvas.create_line(hangman_lines[self.count - 1], width=5)
        else:
            self.create_circle(220, 170, 15)
        self.count += 1

    def check_guess(self, letter):
        if self.count < 6:
            if letter in self.word:
                self.change_status(letter)
                self.buttons[letter.upper()].config(bg='green')
                if ''.join(self.guess) == self.word:
                    self.canvas.create_text(250, 100, text="You guessed the word!", fill="Green", font=("Purisa", 25))
            else:
                self.buttons[letter.upper()].config(bg='red')
                self.add_line_to_hangman()
                if self.count == 6:
                    self.canvas.create_text(250, 100, text="Game Over", fill="Red", font=("Purisa", 25))

    def initialize_letter_buttons(self):
        buttons_per_row = 13
        button_width = 30
        button_height = 30
        button_y = 450
        # Create buttons for A-Z
        for index, letter in enumerate(range(65, 91)):  # ASCII values for A-Z
            letter_char = chr(letter)
            btn = tk.Button(self.master, text=letter_char, width=button_width // 6, height=button_height // 15,
                            command=lambda l=letter_char: self.check_guess(l.lower()))
            self.buttons[letter_char] = btn  # Store the button reference
            # Calculate row and column for positioning
            row = index // buttons_per_row
            column = index % buttons_per_row
            self.canvas.create_window(15 + column * (button_width + 10), button_y + row * (button_height + 5),
                                      window=btn)

    def initialize_game(self):
        self.master.title("Hangman")
        self.master.geometry("550x550")
        self.canvas.pack()
        self.canvas.create_line(200, 300, 300, 300, width=5)
        self.canvas.create_line(270, 130, 270, 300, width=5)
        self.canvas.create_line(220, 130, 270, 130, width=5)
        self.canvas.create_line(220, 130, 220, 160, width=5)
        self.canvas.create_text(250, 400, text="Please guess your next letter:", fill="black", font=50)
        self.guess_id = self.canvas.create_text(250, 350, text=' '.join(self.guess), fill="black", font=("Purisa", 25))

        self.initialize_letter_buttons()  # Call to create buttons


if __name__ == "__main__":
    p1 = Hangman()
    p1.master.mainloop()
