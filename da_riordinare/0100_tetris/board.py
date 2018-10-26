import random
from shapes import I_Shape, J_Shape, L_Shape, O_Shape, S_Shape, T_Shape, Z_Shape

class Board:
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 20

    def __init__(self):
        self.createNewShape()

    def createNewShape(self):
        shapes = [I_Shape((4, 1)),J_Shape((4, 1)),L_Shape((4, 1)),O_Shape((4, 1)),S_Shape((4, 1)),T_Shape((4, 1)),Z_Shape((4, 1))]
        self.currentShape = random.choice(shapes)

    def canMoveCurrentShape(self, delta):
        canMove = self.currentShape.canMove(delta, Board.BOARD_WIDTH, Board.BOARD_HEIGHT)
        dx, dy = delta
        if not canMove and dy == 1:
            self.addShapeBlocks()
        return canMove

    def moveCurrentShape(self, delta):
        self.currentShape.move(delta)


    def addShapeBlocks(self):
        print "arrivato"

    def draw(self, screen):
        self.currentShape.draw(screen)
