from ...settings import *

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scenes = None

    def add_scene(self,name,scene):
        if scene not in self.scenes:
            if len(self.scenes) == 0:
                self.current_scenes = name

            self.scenes[name] = scene

    def swap_scenes(self,name):
        self.current_scenes = name

    def render(self):
        if self.current_scenes:
            self.scenes[self.current_scenes].render()

    def update(self):
        if self.current_scenes:
            self.scenes[self.current_scenes].update()
