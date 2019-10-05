import arcade
from .objeto import Objeto

class Laser_jogador(Objeto):

    def __init__(self, tipo, center_x=0, center_y=0, speed = 10, escala = 1 ):
        super().__init__('jogo/objetos/sprites/tiro' + tipo + '.png', escala, center_x, center_y)
        self.speed = speed

    def get_speed(self):
        return self.speed

class Laser_alien(Objeto):

    def __init__(self, center_x=0, center_y=0, speed = -10, escala = 1 ):
        super().__init__('jogo/objetos/sprites/tiroalien1.png', escala,  center_x, center_y)
        self.append_texture(arcade.load_texture('jogo/objetos/sprites/tiroalien2.png'))
        self.append_texture(arcade.load_texture('jogo/objetos/sprites/tiroalien3.png'))
        self.append_texture(arcade.load_texture('jogo/objetos/sprites/tiroalien4.png'))
        self.speed = speed

    def get_speed(self):
        return self.speed