from tkinter import Canvas
import tkinter as tk
from GameOfLife import main

colors = [
            ('Red', 'red', 85),
            ('Orange', 'orange', 120),
            ('Yellow', 'yellow', 180),
            ('Green', 'green', 230),
            ('Blue', 'blue', 280),
            ('Pink', 'pink', 375),
            ('Purple', 'purple', 320),
        ]

class MenuGameOfLife:
    def __init__(self):
        self.master = tk.Tk()
        self.canvas = Canvas(self.master, width=500, height=500)
        self.selected_color =  ""

    def start_game(self, width, height):
        if self.selected_color == "":
            tk.Label(self.master, text="You didn't choose color!", font=("Arial", 16, "bold"), fg='Red').place(x=150, y=250)
        elif not width.isnumeric() or not height.isnumeric():
            tk.Label(self.master, text="Bad Width or height", font=("Arial", 16, "bold"), fg='Red').place(x=150, y=250)
        else:
            main(int(width), int(height),  self.selected_color)
    def set_color(self, color):
        self.selected_color = color.title()
    def initialize_game(self):
        self.master.title("Template Game Of Life")
        self.master.geometry("500x300")
        tk.Label(self.master,text="Please choose color for life:" ,font=("Arial", 16, "bold")).pack(pady=20)

        for text, bg_color, x in colors:
            button = tk.Button(self.master, text=text, bg=bg_color, command=lambda c=bg_color: self.set_color(c))
            button.place(x=x, y=50)

        tk.Label(self.master,text="Screen width:" ,font=("Arial", 16, "bold")).place(x=175, y=90)
        width = tk.Entry(self.master,font=("Arial", 14, "bold"))
        width.place(x=140, y=120)
        tk.Label(self.master, text="Screen height:", font=("Arial", 16, "bold")).place(x=170, y=150)
        height = tk.Entry(self.master, font=("Arial", 14, "bold"))
        height.place(x=140, y=180)
        tk.Button(self.master, text='Start', bg='Grey',
                  command=lambda: self.start_game(width.get(), height.get())).place(x=220, y=220)
        self.master.mainloop()

menu = MenuGameOfLife()
menu.initialize_game()