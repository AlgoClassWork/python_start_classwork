def amount_five():
    mark = int(input('Оценка (0-завершить):'))
    five = 0
    while mark != 0:
        if mark == 5:
            five += 1
        mark = int(input('Оценка (0-завершить):'))
    return five

def skidka(kolvo_5):
    if kolvo_5 > 5:
        print('Скидка на билеты в театр (%):',15)
    elif kolvo_5 >= 4 and kolvo_5 <= 5:
        print('Скидка на билеты в театр (%):',10)
    else:
        print('Скидка на билеты в театр (%):',0)

skidka(amount_five())
