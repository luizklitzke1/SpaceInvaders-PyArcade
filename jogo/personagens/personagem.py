import arcade


class Personagem(arcade.Sprite):

    def __init__(self, tipo, escala, center_x=0, center_y=0,**kwargs):
        imagem = ('jogo/personagens/sprites/' + str(tipo) + '.png')
        super().__init__(imagem, escala)
        self.set_escala(escala)
        self.set_center_x(center_x)
        self.set_center_y(center_y)

    def set_center_x(self, center_x):
        self.center_x = center_x

    def get_center_x(self):
        return self.center_x

    def set_center_y(self, center_y):
        self.center_y = center_y

    def get_center_y(self):
        return self.center_y

    def set_escala(self, escala):
        self.escala = escala

    def get_escala(self):
        return self.escala

    #Manter na tela caso passe dos limites
    def manter_na_tela(self, width, height, bottom, top, left, right):
        if bottom < 50:
            self.center_y += 5
        elif top > height -50:
            self.center_y += -5
        elif right > width-10:
            self.center_x += -5
        elif left < 10:
            self.center_x += 5
