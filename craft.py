from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        base.camLens.setFov(90)

game = Game()
game.run()




class Mapmanager():
    def __init__(self):
        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode('Land')

    def addBlock(self, position):
        self.block = loader.loadModel('block.egg')
        self.block.setTexture(loader.loadTexture('block.png'))
        self.block.setPos(position)
        self.block.reparentTo(self.land)

    def loadLand(self, filename):
        map = open(filename)
        y = 0
        for line in map:
            block_line = line.split()
            x = 0
            for block in block_line:
                for z in range(int(block) + 1):
                    one_block = self.addBlock((x, y, z))
                x += 1
            y += 1
