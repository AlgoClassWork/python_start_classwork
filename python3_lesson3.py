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



data = dict()
while input('Желаете посетить урок программирования (да/нет)?').lower() == 'да':
    topic = input('Введите тему урока')
    if topic in data:
        data[topic] += 1
    else:
        data[topic] = 1


total_lessons = 0
for lesson in list(data.values()):
    total_lessons += lesson
total_topics = len(data)


print('Общее количество уроков:', total_lessons)
print('Рассмотрено тем:', total_topics)

