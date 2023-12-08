class Fractal:
    def __init__(self):
        if type(self) == Fractal:
            raise NotImplementedError("You must inherit from Fractal class")

    def count(self):
        raise NotImplementedError("You must override count method in subclass")
