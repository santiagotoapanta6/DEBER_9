from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack(expand=YES, fill=BOTH)
canvas.create_polygon(30, 10, 10, 60, 50, 60,width=2, fill='orange')
def movetriang(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
canvas.bind_all('<KeyPress-Up>', movetriang)
canvas.bind_all('<KeyPress-Down>', movetriang)
canvas.bind_all('<KeyPress-Left>', movetriang)
canvas.bind_all('<KeyPress-Right>', movetriang)
tk.mainloop()