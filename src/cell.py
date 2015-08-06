

class Cell:
    
    def __init__(self, x, y, reachable):
        self.reachable = reachable
        self.x         = x
        self.y         = y
        self.parent    = None
        self.g         = 0
        self.h         = 0
        self.f         = 0
