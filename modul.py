from time import time

rest = 20
begining = time() 
move = ''
while rest > 0 and move != 'off':
    move = input('Ваш ход (off - сдаться):') 
    end = time()
    rest = 20 - (end - begining)
    print('Осталось', int(rest), 'секунд из 20')




from time import time

while True:
    otvet = input('1 - начать 0 - завершить')
    if otvet == '1':
        start = time()
    if otvet == '0':
        end = time()
        itog = round(end - start,2)
        print('Прошло',itog,'с')
        break


    
from random import randint

number = str(randint(1,8))
letter = 'ABCDEFGH'[randint(0,7)]
print('Ход фигурой на клетке', letter + number)
