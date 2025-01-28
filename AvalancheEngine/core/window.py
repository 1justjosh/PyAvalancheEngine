from ..settings import *

class Window:
    def __init__(self,size,title,flags):
        self.screen = pg.display.set_mode(size,flags=pg.OPENGL | pg.DOUBLEBUF | flags)

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_COMPATIBILITY,pg.GL_CONTEXT_PROFILE_CORE)

        self.context = mgl.create_context()

        pg.display.set_caption(title)

    def set_icon(self,icon):
        if icon:
            pg.display.set_icon(icon)


    def event_handler(self,event):
        if event.type == pg.VIDEORESIZE:
            print(self.screen.get_size())

    def render(self):
        self.context.clear(0.2,0.6,0.8,1.0)
        pg.display.flip()
