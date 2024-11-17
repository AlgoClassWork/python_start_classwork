#game.py

# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from map import Map

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Map()
        base.camLens.setFov(90)

game = Game()
game.run()

#map.py

# напиши здесь код создания и управления картой
class Map():
    def __init__(self):
        self.land = render.attachNewNode('Land')
        self.addBlock( (0,10,0) )

    def addBlock(self,position):
        self.block = loader.loadModel('block')
        self.block.setTexture(loader.loadTexture('block.png'))
        self.block.setPos(position)
        self.block.setColor((0.2 , 0.2 , 0.2 , 1))
        self.block.reparentTo(self.land)

