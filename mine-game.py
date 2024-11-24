Файл game.py


from direct.showbase.ShowBase import ShowBase

from hero import Hero
from mapmanager import Mapmanager

    
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.hero = Hero( (1,1,1), self.land )
        self.land.loadLand('land.txt')

game = Game()
game.run()

Файл mapmanager.py

class Mapmanager():
    """ Управление картой """
    def __init__(self):
        self.model = 'block' # модель кубика лежит в файле block.egg
        # # используются следующие текстуры: 
        self.texture = 'block.png'
        # создаём строительные блоки   
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))           
        self.color = (0.2, 0.2, 0.35, 1) #rgba

        # создаём основной узел карты:
        self.startNew() 

    def startNew(self):
        """создаёт основу для новой карты""" 
        self.land = render.attachNewNode("Land") # узел, к которому привязаны все блоки карты
    
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture)) 
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    # обнуление карты
    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        # загружаем данные из текстового файла
        self.clear()
        land = open(filename)
        # алгоритм загрузки карты из числовой модели
        y = 0
        for block_line in land:
            x = 0
            block_line = block_line.split()
            for block_count in block_line:
                for z in range( int(block_count) + 1 ):
                    block = self.addBlock((x,y,z))
                x += 1
            y += 1


Файл hero.py

class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(pos[0], pos[1], pos[2])
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def accept_events(self):
        base.accept('z', self.changeView)

