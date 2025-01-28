from ..settings import *

def load_image(path:str,*args,**kwargs):
    if "convert" in args:
        image = pg.image.load(path).convert()
    else:
        image = pg.image.load(path).convert_alpha()

    if "size" in kwargs:
        image = pg.transform.scale(image,kwargs["size"])

    return image
