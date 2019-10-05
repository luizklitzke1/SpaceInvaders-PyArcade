import arcade
from personagens.personagem import Personagem
from objetos.projeteis import Laser_jogador

class Jogador(Personagem):

    def __init__(self, tipo, vidas, escala, velocidade, center_x, center_y, mov_left, mov_right, laser, pont):
        super().__init__('player'+tipo+'1', escala, center_x, center_y)
        self.append_texture(arcade.load_texture("jogo/personagens/sprites/player"+tipo+'2.png'))
        self.append_texture(arcade.load_texture("jogo/personagens/sprites/player"+tipo+'3.png'))
        self.numero = tipo
        self.vidas = vidas
        self.speed = velocidade
        self.pontos = pont
        self.mov_left = mov_left
        self.mov_right = mov_right
        self.botao_laser = laser
        self.lista_lasers = arcade.SpriteList()
        self.som_laser = arcade.load_sound('jogo/sons/shoot.wav')
        self.estado = 'vivo'


    def adicionar_pontos(self, pontos):
        self.pontos += pontos

    def on_key_press(self, key, modifiers):

        if self.get_estado() == 'vivo':
            # Movimentação  (Esqueda - Direita)
            if key == self.mov_left:
                self.change_x = -self.speed
            elif key == self.mov_right:
                self.change_x = self.speed

            # Criar laser e adiciona na sua própria lista
            if key == self.botao_laser:
                if len(self.lista_lasers) == 0:
                        novo_laser = Laser_jogador(self.numero, self.center_x, self.top+5, 18)
                        arcade.play_sound(self.get_som_laser())
                        self.lista_lasers.append(novo_laser)
    
    def on_key_release(self, key, modifiers):
        # Movimentação  (Esqueda - Direita)
        if key == self.mov_left or key == self.mov_right:
            self.change_x = 0
            

    # morto = primeiro estado da animacao  morto2 = segundo estado e volta a vida  mortofull = acabaram todas as vidas
    def mudar_textura(self, loops, resets, update_time):
        if loops == update_time:
            if self.get_estado() == 'morto':
                arcade.play_sound(arcade.load_sound('jogo/sons/shipexplosion.wav'))
                if resets % 2 == 0:
                    self.set_texture(1)
                    self.set_estado('morto2')
            elif self.get_estado() == 'morto2':
                self.set_texture(2)
                self.set_estado('vivo')
                self.set_estado('mudar')
            elif self.get_estado() == 'mudar':
                self.set_texture(0)
                self.set_estado('vivo')

    def get_pontos(self):
        return self.pontos

    def set_vidas(self, vidas):
        self.vidas = vidas

    def get_vidas(self):
        return self.vidas

    def remover_vidas(self, vida):
        self.vidas -= vida

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado
        
    def get_botao_laser(self):
        return self.botao_laser

    def get_som_laser(self):
        return self.som_laser

    def get_velocidade(self):
        return self.velocidade

    def get_numero(self):
        return self.numero
