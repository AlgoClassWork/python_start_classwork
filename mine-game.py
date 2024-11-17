#game.py

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
class Map():
    def __init__(self):
        self.land = render.attachNewNode('Land')
        self.addBlock( (0,10,0) )

    def addBlock(self,position):
        self.block = loader.loadModel('block')
        self.block.setTexture(loader.loadTexture('block.png'))
        self.block.setPos(0,10,0)
        self.block.setColor(position)
        self.block.reparenTo(self.land)

