from tkinter import *
 
class Colors(Tk): 
    def __init__(self):
        super().__init__()
        self.label = Label(text="", width=20)
        self.entry = Entry(width=20, justify=CENTER)
 
        colors = {'#ff0000': 'Красный',
               '#ff7d00': 'Оранжевый',
               '#ffff00': 'Желтый',
               '#00ff00': 'Зеленый',
               '#007dff': 'Голубой',
               '#0000ff': 'Синий',
               '#7d00ff': 'Фиолетовый'}
 
        for temp in colors.keys():
            func = lambda col=temp, color_name=colors[temp]: self.click(col, color_name)
            btn = Button(text='', command=func, bg=temp, width=20, height=1)
            self.label.pack()
            self.entry.pack()
            btn.pack()
 
    def click(self, colour, color_name):
        self.entry.delete(0, END)
        self.entry.insert(0, colour)
        self.label['text'] = color_name
 
 
window = Colors()
window.mainloop()