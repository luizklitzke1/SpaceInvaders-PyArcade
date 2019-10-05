import arcade
from .objeto import Objeto

class Bloco_cover(Objeto):

    def __init__(self, center_x, center_y, escala):
        super().__init__('jogo/objetos/sprites/coverp.png', escala, center_x, center_y)




