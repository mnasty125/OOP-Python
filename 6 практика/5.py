from tkinter import *
 
root = Tk()
c = Canvas(root, width=500, height=500, bg="gray")
c.pack()

ball = c.create_oval(400, 0, 500, 100, fill='purple', outline="purple")
ball2 = c.create_oval(0, 0, 100, 100, fill='yellow', outline="yellow")
ball3 = c.create_oval(0, 400, 100, 500, fill='green', outline="green")
ball4 = c.create_oval(400, 400, 500, 500, fill='blue', outline="blue")
 
def moveing():
    c.move(ball, -1, 1)
    if c.coords(ball)[0] < 500:
        root.after(10, moveing)
def moveing2():
    c.move(ball2, 1, 1)
    if c.coords(ball2)[0] < 500:
        root.after(10, moveing2)
def moveing3():
    c.move(ball3, 1, -1)
    if c.coords(ball2)[0] < 500:
        root.after(10, moveing3)
def moveing4():
    c.move(ball4, -1, -1)
    if c.coords(ball2)[0] < 500:
        root.after(10, moveing4)

moveing()
moveing2()
moveing3()
moveing4()

root.mainloop()