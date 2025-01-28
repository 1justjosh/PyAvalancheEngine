import sys

from .settings import *
from .core.window import Window
from .core.scenes.scene_manager import SceneManager

class Engine:
    _instance = None  # Class-level attribute to store the singleton instance

    def __new__(cls, *args, **kwargs):
        # Check if an instance already exists
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self,size:tuple[int,int]=(1080,720),title:str="Avalanche Engine",flags=0,fps=120):

        self.window = Window(size,title,flags)
        self.context = self.window.context

        self.initialized = True

        self.clock = pg.time.Clock()
        self.fps = fps
        self.dt = 0

        self.scene_manager = SceneManager()

        self.running = True

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            self.window.event_handler(event)

    def render(self):
        self.window.render()
        self.scene_manager.render()

    def update(self):
        self.dt = self.clock.tick(self.fps) / 1000

        self.scene_manager.update()

    def quit(self):
        pg.quit()
        sys.exit()

    def run(self):
        while self.running:
            self.event_handler()
            self.update()
            self.render()
        self.quit()
