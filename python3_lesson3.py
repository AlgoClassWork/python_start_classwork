class Converter:
    def __init__(self, kurs):
        self.kurs = kurs

    def change_dollar(self, summa):
        print(   round(self.kurs * summa,2)   )

    def change_rub(self, summa):
        print(   round(summa / self.kurs,2)    )

kurs = float(input('Введите курс доллара'))
summa = int(input('Введите сумму обмена'))

change_money = Converter(kurs)

otvet = int(input('Введите 1 поменять доллары 2 поменять рубли'))
if otvet == 1:
    change_money.change_dollar(summa)
if otvet == 2:
    change_money.change_rub(summa)
