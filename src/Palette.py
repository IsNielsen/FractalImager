class Palette:
    def __init__(self, iterations):
        if type(self) == Palette:
            raise NotImplementedError("you must inherit from Palette")
        self._iterations = iterations

    def getColor(self):
        raise NotImplementedError("You must override getColor method in subclass :(")
