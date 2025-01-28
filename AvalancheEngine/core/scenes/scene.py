from ...settings import *


class AvalancheScene:
    def __init__(self):
        self.game_objects = []

    def add_game_object(self,object):
        self.game_objects.append(object)

    def render(self):
        for game_object in self.game_objects:
            game_object.render()

    def update(self):
        for game_object in self.game_objects:
            game_object.update()
