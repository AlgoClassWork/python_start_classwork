class Price_list():
    def __init__(self,name):
        self.name = name
        self.uslugi = dict()

    def add_price(self, **data):
        for usluga in data:
            self.uslugi[usluga] = data[usluga]

    def order(self, **data):
        total = 0
        for usluga in data:
            total += self.uslugi[usluga] * data[usluga]
        return total

my_offer = Price_list('Инстаграм')
my_offer.add_price(management = 1000, content_plan = 850, style = 500, stories = 100, post = 300)

otvet = input('Хотите сделать заказ? (1 - да, 0 - нет)')
if otvet == '1':
    otvet = input('Хотите заказать управление аккаунтами (1) или публикации (2)?')
    if otvet == '1':
        account = int(input('Сколько новых аккаунтов хотите добавить?'))
        content = int(input('Для скольких из них будем делать контент-план?'))
        styl = int(input('Для скольких из них будем разрабатывать стиль?'))
        print('Стоимость услуг:',my_offer.order(management = account, content_plan = content, style = styl),'руб.')





