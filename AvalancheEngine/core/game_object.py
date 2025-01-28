from ..settings import *

class GameObject:
    def __init__(self):
        self.components = []

    def render(self):
        for component in self.components:
            component.render()

    def update(self):
        for component in self.components:
            component.update()

