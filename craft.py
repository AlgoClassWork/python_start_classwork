from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        base.camLens.setFov(90)

game = Game()
game.run()



class Mapmanager():
    def __init__(self):
        self.startNew()
        self.addBlock((0, 10, 0))
        self.addBlock((1, 10, 0))

    def startNew(self):
        self.land = render.attachNewNode('Land')

    def addBlock(self, position):
        self.block = loader.loadModel('block.egg')
        self.block.setTexture(loader.loadTexture('block.png'))
        self.block.setPos(position)
        self.block.reparentTo(self.land)
