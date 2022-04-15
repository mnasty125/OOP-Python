from tkinter import *

class Numbers(Tk): 
    def __init__(self):
        super().__init__()
        #Создание элементов окна
        self.label1 = Label(text="Римские в арабские:", width=20, height=2, background="#CD5C5C")
        self.label2 = Label(text="Арабские в римские:", width=20, height=2, background="#CD5C5C")
        self.label3 = Label(text="", width=20, height=2, background="#F08080")
        self.label4 = Label(text="", width=20, height=2, background="#F08080")
        self.entry1 = Entry(width=25, justify=CENTER)
        self.entry2 = Entry(width=25, justify=CENTER)
        # Функции, выполняемые при клике на кнопки
        func1 = lambda : self.click_btn1()
        func2 = lambda : self.click_btn2()
        self.btn1 = Button(text="Перевести", command=func1, width=10, height=2)
        self.btn2 = Button(text="Перевести", command=func2, width=10, height=2)
        # Размещение элементов в окне
        self.label1.grid(row=0, rowspan=2, column=0, pady=3)
        self.label2.grid(row=2, rowspan=2, column=0, pady=3)
        self.entry1.grid(row=0, column=1, padx=3)
        self.entry2.grid(row=2, column=1, padx=3)
        self.label3.grid(row=1, column=1, padx=3, pady=3)
        self.label4.grid(row=3, column=1, padx=3, pady=3)
        self.btn1.grid(row=0, rowspan=2, column=2, padx=3, pady=3)
        self.btn2.grid(row=2, rowspan=2, column=2, padx=3, pady=3)

        # Кортеж соответствий арабских и римских цифр
        self.table = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

    # Выполняется при клике на кнопку1, перевод из арабских в римские
    def click_btn1(self):
        self.arab = int(self.entry1.get())
        if self.arab <= 0: 
            return ''
        result = ''
        for arab, roman in self.table:
            while self.arab >= arab:
                result += roman
                self.arab -= arab
        self.label3['text'] = result
    
    # Выполняется при клике на кнопку2, перевод из римских в арабские
    def click_btn2(self):
        self.roman = self.entry2.get()
        self.roman = self.roman.upper()
        result = 0
        for arab, roman in self.table:
            while self.roman.startswith( roman ):
                result += arab
                self.roman = self.roman[ len( roman ): ]
        self.label4['text'] = result


window = Numbers()
window.mainloop()