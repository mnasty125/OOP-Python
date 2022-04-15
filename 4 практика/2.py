from tkinter import *
 
class Colors(Tk): 
    def __init__(self):
        super().__init__()
        self.label = Label(text="", width=1)
        self.entry = Entry(width=1, justify=CENTER)
        self.label.grid(row=0, column=0, columnspan=10, sticky='nwse')
        self.entry.grid(row=1, column=0, columnspan=10, sticky='nwse')
 
        colors = {'#ff0000': 'Красный',
               '#ff7d00': 'Оранжевый',
               '#ffff00': 'Желтый',
               '#00ff00': 'Зеленый',
               '#007dff': 'Голубой',
               '#0000ff': 'Синий',
               '#7d00ff': 'Фиолетовый'}
 
        for i, temp in enumerate(colors.keys()):
            func = lambda col=temp, color_name=colors[temp]: self.click(col, color_name)
            btn = Button(text='', command=func, bg=temp, width=2, height=1)
            btn.grid(row=2, column=i, padx=2, pady=0, sticky='nwse')
 
    def click(self, colour, color_name):
        self.entry.delete(0, END)
        self.entry.insert(0, colour)
        self.label['text'] = color_name 
 
window = Colors()
window.mainloop()