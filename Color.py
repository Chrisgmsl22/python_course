

class Color:
    def __init__(self, color):
        self._color = color

    #toString()
    def __str__(self):
        return f'de color: {self._color}'

    #Getters y Setters
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color