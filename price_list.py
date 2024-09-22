class Price_list():
    def __init__(self,name):
        self.name = name
        self.price_list = dict()

    def add_price(self,**uslugi):
        for usluga in uslugi:
            self.price_list[usluga] = uslugi[usluga]

my_offer = Price_list('Инстаграм')
my_offer.add_price(management = 1000, content_plan = 850, style = 500, stories = 100, post = 300)

otvet = input('Хотите сделать заказ? (1 - да, 0 - нет)')
if otvet == '1':
    pass
if otvet == '0':
    print('Спасибо за сотрудничество! Хорошего дня!')
