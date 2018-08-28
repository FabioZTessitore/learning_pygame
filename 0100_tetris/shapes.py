from block import Block
from colors import BLUE, ORANGE, CYAN, RED, GREEN, YELLOW, PURPLE

class Shape:
    def __init__(self, coords):
        self.coords = coords

    def canMove(self, delta, boardWidth, boardHeight):
        for point in self.coords:
            b = Block()
            if not b.canMove(point, delta, boardWidth, boardHeight):
                return False

        return True

    def move(self, delta):
        dx, dy = delta
        newcoords = []
        for coord in self.coords:
            x, y = coord
            newcoords.append( (x+dx, y+dy) )
        self.coords = newcoords

    def draw(self, screen):
        for point in self.coords:
            b = Block()
            b.draw(screen, point, self.color)

class I_Shape(Shape):
    def __init__(self, center):
        x, y = center
        coords = [ (x-2, y), (x-1, y), (x, y), (x+1, y) ]
        self.color = BLUE
        Shape.__init__(self, coords)

class J_Shape(Shape):
    def __init__(self, center):
        x, y = center
        coords = [ (x-1, y), (x, y), (x+1, y), (x+1, y+1) ]
        self.color = ORANGE
        Shape.__init__(self, coords)

class L_Shape(Shape):
    def __init__(self, center):
        x, y = center
        coords = [ (x-1, y), (x, y), (x+1, y), (x-1, y+1) ]
        self.color = CYAN
        Shape.__init__(self, coords)

class O_Shape(Shape):
    def __init__(self, center):
        x, y = center
        coords = [ (x-1, y), (x, y), (x, y+1), (x-1, y+1) ]
        self.color = RED
        Shape.__init__(self, coords)

class S_Shape(Shape):
    def __init__(self, center):
        x, y = center
        coords = [ (x-1, y+1), (x, y), (x, y+1), (x+1, y) ]
        self.color = GREEN
        Shape.__init__(self, coords)

class T_Shape(Shape):
    def __init__(self, center):
        x, y = center
        coords = [ (x-1, y), (x, y), (x, y+1), (x+1, y) ]
        self.color = YELLOW
        Shape.__init__(self, coords)

class Z_Shape(Shape):
    def __init__(self, center):
        x, y = center
        coords = [ (x-1, y), (x, y), (x, y+1), (x+1, y+1) ]
        self.color = PURPLE
        Shape.__init__(self, coords)
