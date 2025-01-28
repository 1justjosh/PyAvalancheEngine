from ...settings import *
from .base_component import BaseComponent
from ...engine import Engine

VERTEX_SHADER = """
#version 330 core

layout (location = 0) in vec3 in_position;

void main() {
    gl_Position = projection * vec4(in_position, 1.0);
}

"""

FRAGMENT_SHADER = """
#version 330 core

layout (location = 0) out vec4 fragColour;

void main() {
    fragColour = vec4(1.0, 0.0, 0.0, 1.0);
}
"""


class Mesh(BaseComponent):
    def __init__(self, vertices: list[tuple[float, float, float]], indices, vertex_shader_code=VERTEX_SHADER,
                 fragment_shader_code=FRAGMENT_SHADER):
        super().__init__()

        self.vertex_shader_code = vertex_shader_code
        self.fragment_shader_code = fragment_shader_code

        self.vertices = vertices
        self.indices = indices

        self.vbo = self.__get_vbo()
        self.shader_program = self.__get_shader_program()
        self.vao = self.__get_vao()

    def render(self):
        self.vao.render()

    def destroy(self):
        self.vao.release()
        self.vbo.release()
        self.shader_program.release()

    def __get_vao(self):
        vao = self.context.vertex_array(self.shader_program, [(self.vbo, "3f", "in_position")])
        return vao

    def __get_vertex_data(self):
        return np.array(self.vertices, dtype="f4")

    def __get_vbo(self):
        vertex_data = self.__get_vertex_data()
        vbo = self.context.buffer(vertex_data)
        return vbo

    def __get_shader_program(self):
        program = self.context.program(vertex_shader=self.vertex_shader_code, fragment_shader=self.fragment_shader_code)
        return program
