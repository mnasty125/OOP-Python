from tkinter import *

class Money(Tk): 
    def __init__(self):
        super().__init__()
        #Создание элементов окна
        self.label1 = Label(text="Остаток:", width=20, height=2, background="#CD5C5C")
        self.label2 = Label(text="", width=20, height=2, background="#F08080")
        self.entry = Entry(width=25, justify=CENTER)
        # Размещение элементов в окне
        self.label1.grid(row=1, column=0, columnspan=3, pady=2)
        self.label2.grid(row=2, column=0, columnspan=3, pady=2)
        self.entry.grid(row=3, column=0, columnspan=3)
        # Задание начальных значений
        self.money = ""
        self.balance = 1000
        self.label2['text'] = self.balance

        # Массив значений кнопок и их номерами
        btns = {"Снять":"0", 
                    "Положить":"1",
                        "Баланс":"2"}

         # Создание кнопок, назначение им функции при клике и размещение кнопок в окне
        for count in btns.keys():
            func = lambda temp = count: self.click(temp)
            btn = Button(text = count, command=func, width=10, height=4)
            if (int(btns[count])<=1):
                btn.grid(row=4, column=int(btns[count]), padx=2, pady=2)
            else:
                btn.grid(row=5, column=int(btns[count]) - 2, columnspan=3, padx=2, pady=2)
    
    # Получение значений из текстовых полей ввода
    def entry_get (self):
        self.money = int(self.entry.get())

    # Выполнение операций по клике на кнопку
    def click(self, operation):
        self.label2['text'] = self.balance
        self.entry_get()
        if (operation == "Снять"):
            if (self.balance >= self.money):
                result = self.balance - self.money
            else:
                self.label2['text'] = "Недостаточно средств"
        elif (operation == "Положить"):
            result = self.balance + self.money
        elif (operation == "Баланс"):
            result = self.balance
        self.balance = result
        self.label2['text'] = result
        self.entry.delete(0, END)
        self.label2.delete(0, END)

window = Money()
window.mainloop()