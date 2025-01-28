from AvalancheEngine import *

import pygame as pg
import os

class Scene(AvalancheScene):
    def __init__(self):
        super().__init__()
        vertices = [
            (-0.5, -0.5, 0.0),  # Vertex 1
            (0.5, -0.5, 0.0),  # Vertex 2
            (0.0, 0.5, 0.0)  # Vertex 3
        ]

        with open(os.path.join("AvalancheEditor","default.vert")) as file:
            vert = file.read()
        with open(os.path.join("AvalancheEditor","default.frag")) as file:
            frag = file.read()

        mesh = Mesh(
            vertices=vertices,
            indices=None,
            vertex_shader_code=vert,
            fragment_shader_code=frag
        )
        self.game_objects.append(mesh)

    def render(self):
        for game_object in self.game_objects:
            game_object.render()


if __name__ == '__main__':
    engine = Engine(flags=pg.RESIZABLE)
    scene = Scene()
    engine.scene_manager.add_scene("test_scene", scene)
    engine.run()
