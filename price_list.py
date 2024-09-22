class Price_list():
    def __init__(self,name):
        self.name = name
        self.price_list = dict()

    def add_price(self,**uslugi):
        for usluga in uslugi:
            self.price_list[usluga] = uslugi[usluga]

    def order(self,**uslugi):
        total = 0
        for usluga in uslugi:
            total += self.price_list[usluga] * uslugi[usluga]
        print('Стоимость услуг равна',total,'руб')

my_offer = Price_list('Инстаграм')
my_offer.add_price(management = 1000, content_plan = 850, style = 500, stories = 100, post = 300)

otvet = input('Хотите сделать заказ? (1 - да, 0 - нет)')
if otvet == '1':
    otvet = input('Хотите заказать управление аккаунтами (1) или публикации (2)?')
    if otvet == '1':
        ans1 = int(input('Сколько новых аккаунтов хотите добавить?'))
        ans2 = int(input('Для скольких из них будем делать контент-план?'))
        ans3 = int(input('Для скольких из них будем разрабатывать стиль?'))
        my_offer.order(management=ans1, content_plan=ans2, style=ans3)
    if otvet == '2':
        pass
if otvet == '0':
    print('Спасибо за сотрудничество! Хорошего дня!')
