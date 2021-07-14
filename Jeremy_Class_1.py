from tkinter import *

window = Tk()
window.title("A House")
canvas = Canvas(window)
canvas.pack()
canvas.config(bg = "lightblue")

canvas.create_polygon(40, 100, 215, 100, 129, 30, fill = 'white' )
canvas.create_rectangle(50, 100, 200, 200, fill = 'white')

canvas.create_rectangle(370, 100, 250, 200, fill = 'white')
canvas.create_rectangle(360, 130, 259.5, 200, fill = 'gray')

canvas.create_rectangle(70, 130, 120, 200, fill = "gray")
canvas.create_rectangle(140, 150, 175, 130, fill = "blue")
canvas.create_line(72, 200, 107, 290, fill = "black")
canvas.create_line(120, 200, 1800, 5000, fill = "black")

window.mainloop()


