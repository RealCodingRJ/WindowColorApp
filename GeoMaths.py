class Geo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return ((self.x + 50) - 2) / 3

    def getY(self):
        return ((self.y + 50) - 50) / 2

