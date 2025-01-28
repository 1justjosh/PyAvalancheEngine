from ...settings import *
from ...engine import Engine

class BaseComponent:
    def __init__(self):
        self.engine = Engine()
        self.context = self.engine.context

        print(self.engine.window.screen.size)

    def render(self):
        pass

    def update(self):
        pass

    def destroy(self):
        pass