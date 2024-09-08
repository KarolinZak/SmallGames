import tkinter as tk

root = tk.Tk(); canvas = tk.Canvas(root, width=400, height=200); canvas.pack(); [canvas.create_window(x * 15 + 20, 50, window=tk.Button(root, text=chr(i), command=lambda l=chr(i): print(l))) for i, x in zip(range(65, 91), range(26))]; root.mainloop()
