class Car():
    def __init__(self,marka='лада',color='малиновый',speed=10,gas=0,km=0):
        self.marka = marka
        self.color = color
        self.speed = speed
        self.gas = gas 
        self.km = km

    def info(self):
        print('Марка машины:',self.marka)
        print('Цвет машины:',self.color)
        print('Скорость машины:',self.speed)
        print('Количество топлива:',self.gas,'\n')

    def move(self):
        print('Газ в пол')
        self.gas -= 50
        print('За час вы проехали', self.speed)
        self.km += self.speed
        print('Ваш текущий путь составил', self.km)
        print('У вас осталось',self.gas,'л')

car1 = Car(marka='мерс',speed=200, gas = 150, color='черный')
car1.move()
car1.move()
car1.move()
