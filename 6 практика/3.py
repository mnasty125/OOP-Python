from tkinter import *

root = Tk()

c1 = Canvas(root, width=500, height=500, bg= "white")
c1.pack()

c1.create_polygon(100, 200, 300, 400, 170, 400, fill="blue")
c1.create_polygon(400, 200, 330, 400, 200, 400, fill="green")
c1.create_polygon(250, 200, 320, 400, 180, 400, fill="red")

c1.create_oval(80, 180, 120, 220, fill="blue")
c1.create_oval(230, 180, 270, 220, fill="red")
c1.create_oval(380, 180, 420, 220, fill="green")

c1.create_polygon(250, 300, 260, 330, 290, 340, 260, 350, 250, 380, 240, 350, 210, 340, 240, 330, fill="yellow")

root.mainloop()