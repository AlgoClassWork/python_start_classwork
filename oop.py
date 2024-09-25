class Converter:
    def __init__(self,kurs):
        self.kurs = kurs

    def convert_rub(self,money):
        print(round(self.kurs * money,2))

    def convert_usd(self,money):
        print(round(money / self.kurs,2))

kurs = int(input('Введите курс:'))
money = int(input('Сколько у вас деняк'))

converter = Converter(kurs)

otvet = int(input('1 конвертация рублей 2 конвертация долларов'))
if otvet == 1:
    converter.convert_rub(money)
else:
    converter.convert_usd(money)
