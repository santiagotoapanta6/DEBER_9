from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack(expand=YES, fill=BOTH)
canvas.create_oval(10, 10, 80, 80, width=2, fill='red')
def movecirculo(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
canvas.bind_all('<KeyPress-Up>', movecirculo)
canvas.bind_all('<KeyPress-Down>', movecirculo)
canvas.bind_all('<KeyPress-Left>', movecirculo)
canvas.bind_all('<KeyPress-Right>', movecirculo)
tk.mainloop()