from tkinter import *

class Calck(Tk): 
    def __init__(self):
        super().__init__()
        # Создание элементов
        self.entry1 = Entry(width=20, justify=CENTER)
        self.entry2 = Entry(width=20, justify=CENTER)
        self.label = Label(text="", width=15, height=4, background="#F08080")
        # Размещение элементов в окне
        self.entry1.grid(row=1, column=0, columnspan=2, pady=2)
        self.entry2.grid(row=2, column=0, columnspan=2, pady=2)
        self.label.grid(row=3, column=0, columnspan=3)
        # Начальные значения
        self.num_1 = ""
        self.num_2 = ""

        # Массив со значениями кнопок и их номерами
        btns = {"+":"0", 
                    "-":"1",
                        "*":"2",
                            "/":"3"}
        # Создание кнопок, назначение им функции при клике и размещение кнопок в окне
        for count in btns.keys():
            func = lambda temp = count: self.click(temp)
            btn = Button(text = count, command=func, width=10, height=4)
            if (int(btns[count])<=1):
                btn.grid(row=4, column=int(btns[count]), padx=2, pady=2)
            else:
                btn.grid(row=5, column=int(btns[count]) - 2, padx=2, pady=2)
            
    # Получение значений из текстовых полей ввода
    def entry_get (self):
        self.num_1 = self.entry1.get()
        self.num_2 = self.entry2.get()

    # При клике выполняется операция +, -, *, / с цифрами, полученными из полей
    def click(self, operation):
        self.entry_get()
        num1 = int(self.num_1)
        num2 = int(self.num_2)
        if (operation == "+"):
            result = num1 + num2
        elif (operation == "-"):
            result = num1 - num2
        elif (operation == "*"):
            result = num1 * num2
        elif (operation == "/"):
            if (num2 != 0):
                result = num1 / num2
            else:
                result = "NaN"
        self.label['text'] = result
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)

window = Calck()
window.mainloop()