from tkinter import *

root = Tk()

c1 = Canvas(root, width=500, height=500, bg= "white")
c1.pack()

c1.create_rectangle(150, 200, 350, 400, fill="#5F9EA0", outline="#5F9EA0")
c1.create_polygon(250, 100, 400, 200, 100, 200, fill="#5F9EA0", outline="#5F9EA0")
c1.create_oval(350, 50, 450, 150, fill="yellow", outline="yellow")

for count in range(0, 30):
    c1.create_arc(-50+count*20, 600, 80+count*20, 400, start=90, extent=90, style="arc", outline="green", width=3)

root.mainloop()