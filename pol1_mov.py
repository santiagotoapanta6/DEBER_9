from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack(expand=YES, fill=BOTH)
canvas.create_rectangle(10, 10, 60, 60, width=2, fill='blue')
def moverectangulo(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
canvas.bind_all('<KeyPress-Up>', moverectangulo)
canvas.bind_all('<KeyPress-Down>', moverectangulo)
canvas.bind_all('<KeyPress-Left>', moverectangulo)
canvas.bind_all('<KeyPress-Right>', moverectangulo)
tk.mainloop()