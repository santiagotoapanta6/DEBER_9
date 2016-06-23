import turtle
a = int(input("ingrese un numero impar de puntas para una estrella : "))
t = turtle.Pen()

t.reset()
for x in range(1,a+1):
	t.forward(300)
	an = 180/a
	ang = 180 - an
	t.left(ang)
	
turtle.getscreen()._root.mainloop()