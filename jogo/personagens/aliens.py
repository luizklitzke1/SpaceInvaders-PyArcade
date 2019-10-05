import arcade
from personagens.personagem import Personagem


class Alien(Personagem):

    def __init__(self,  tipo , escala, center_x=0, center_y=0, coluna = 0):
        super().__init__('alien'+tipo+'1', escala, center_x, center_y)
        self.append_texture(arcade.load_texture("jogo/personagens/sprites/alien"+tipo+'2.png'))
        self.append_texture(arcade.load_texture("jogo/personagens/sprites/explosao"+tipo+'.png'))
        self.tipo = tipo
        self.coluna = coluna
        self.estado = 'vivo'
        self.mudado = 0

        # Define a pontuação que dara ao ser morto, baseado no seu tipo
        if self.tipo  == '1':
            self.pontuacao = 30
            self.som_morte = arcade.load_sound('jogo/sons/invaderkilled.wav')
        elif self.tipo  == '2':
            self.pontuacao = 20
            self.som_morte = arcade.load_sound('jogo/sons/invaderkilled.wav')
        elif self.tipo == '3':
            self.pontuacao = 10
            self.som_morte = arcade.load_sound('jogo/sons/invaderkilled.wav')
            

    #Muda sua textura na movimentação, cada "mudado" corresponde há uma textura
    def mudar_textura_andar(self):
        if self.get_mudado() == 0:
            self.set_texture(1)
            self.set_mudado(1)
        else:
            self.set_texture(0)
            self.set_mudado(0)
    
    def get_pontuacao(self):
        return self.pontuacao

    def get_som_morte(self):
        return self.som_morte

    def get_coluna(self):
        return self.coluna

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_mudado(self, mudado):
        self.mudado = mudado

    def get_mudado(self):
        return self.mudado


class Misterio(Personagem):

    def __init__(self, center_x, center_y, tipo):
        super().__init__('nave1', 1, center_x, center_y)
        self.pontos = 500
        self.vida = 3
        self.tipo = tipo       

    def remover_vida(self, dano):
        self.vida -= dano
        
    def get_vida(self):
        return self.vida

    def get_pontos(self):
        return self.pontos