import arcade
import time
from .objeto import Objeto

class Interface():

    def __init__(self, fonte):
        self.set_fonte(fonte)

    def mostrar_menu_pause(self):
        arcade.draw_text('PAUSE', 279, 499, (0,255,255), font_size=40, font_name=self.fonte, bold=True)
        arcade.draw_text('PAUSE', 280, 500, arcade.color.RED, font_size=40, font_name=self.fonte, bold=True)
        arcade.draw_rectangle_filled(359, 469, 10, 40, (0,255,255))
        arcade.draw_rectangle_filled(360, 470, 10, 40, arcade.color.RED)
        arcade.draw_rectangle_filled(379, 469, 10, 40, (0,255,255))
        arcade.draw_rectangle_filled(380, 470, 10, 40, arcade.color.RED)

    def mostrar_nivel(self, nivel):
        output = f"Level:  {nivel}"
        arcade.draw_text(output, 300, 10, arcade.color.YELLOW, 19, font_name= self.fonte)

    def mostrar_vidas(self, lista_jogadores):
        output = f"Lives: {lista_jogadores[0].get_vidas()}"
        arcade.draw_text(output, 40, 15, (0,255,255), 14, font_name=self.fonte)
        output = f"Lives: {lista_jogadores[1].get_vidas()}"
        arcade.draw_text(output, 580, 15, (255,0,255), 14, font_name=self.fonte)

    def mostrar_texto_topo(self):
        arcade.draw_text( 'SCORE - 1', 60, 750, (0,255,255), 20, font_name=self.fonte)
        arcade.draw_text( 'HIGH - SCORE', 250, 750, (255,0,0), 20, font_name=self.fonte)
        arcade.draw_text( 'SCORE - 2', 500, 750, (255,0,255), 20, font_name=self.fonte)

    def mostrar_pontuacao(self, lista_jogadores):
        arcade.draw_text(str(lista_jogadores[0].get_pontos()), 110, 715, arcade.color.WHITE, 14, font_name=self.fonte)
        highscore = 0
        highscore_player = '0'
        for jogador in lista_jogadores:
            if jogador.get_pontos() > highscore:
                highscore_player = jogador.get_numero()
                highscore = jogador.get_pontos()

        output = 'Player ' + highscore_player
        arcade.draw_text(output, 300, 715, arcade.color.WHITE, 14, font_name=self.fonte, align='center')
        arcade.draw_text(str(lista_jogadores[1].get_pontos()), 560, 715, arcade.color.WHITE, 14, font_name=self.fonte)

    def mostrar_avancar_nivel(self, nivel):
        output = 'Level ' + str(nivel)
        arcade.draw_text(output, 260, 500, arcade.color.RED, font_size=40, font_name=self.fonte, bold=True)

    def mostrar_game_over(self, nivel, pont1, pont2):
        arcade.draw_text('GAME OVER', 209, 599, arcade.color.YELLOW, font_size=40, font_name=self.fonte, bold=True)
        arcade.draw_text('GAME OVER', 210, 600, arcade.color.RED, font_size=40, font_name=self.fonte, bold=True)
        arcade.draw_text('Level:   '+str(nivel), 250, 500, arcade.color.MAGENTA, font_size=30, font_name=self.fonte, bold=True)
        arcade.draw_text('Level:   '+str(nivel), 250, 499, arcade.color.AQUA, font_size=30, font_name=self.fonte, bold=True)
        arcade.draw_text('Player 1:    '+str(pont1), 260, 400, arcade.color.MAGENTA, font_size=20, font_name=self.fonte, bold=True)
        arcade.draw_text('Player 1:    '+str(pont1), 260, 399, arcade.color.AQUA, font_size=20, font_name=self.fonte, bold=True)
        arcade.draw_text('Player 2:    '+str(pont2), 260, 300, arcade.color.AQUA, font_size=20, font_name=self.fonte, bold=True)
        arcade.draw_text('Player 2:    '+str(pont2), 260, 299, arcade.color.MAGENTA, font_size=20, font_name=self.fonte, bold=True)
        arcade.draw_text('Press fire to restart!', 89, 199, arcade.color.YELLOW, font_size=30, font_name=self.fonte, bold=True)
        arcade.draw_text('Press fire to restart!', 90, 200, arcade.color.RED, font_size=30, font_name=self.fonte, bold=True)

    def set_fonte(self, fonte):
        self.fonte = fonte
    
    def get_fonte(self):
        return self.fonte

class Menu_inicial(Objeto):
    
    def __init__(self):
        super().__init__('jogo/objetos/menu/frame1.png', 1, 350, 400)
        self.append_texture(arcade.load_texture("jogo/objetos/menu/frame2.png"))
        self.append_texture(arcade.load_texture("jogo/objetos/menu/frame3.png"))
        self.append_texture(arcade.load_texture("jogo/objetos/menu/frame4.png"))
        self.append_texture(arcade.load_texture("jogo/objetos/menu/frame5.png"))
        self.append_texture(arcade.load_texture("jogo/objetos/menu/frame6.png"))
        self.append_texture(arcade.load_texture("jogo/objetos/menu/frame7.png"))
        self.append_texture(arcade.load_texture("jogo/objetos/menu/frame8.png"))
        self.atual = 0

    def update(self, loops):
        
        if self.atual >= 7:
            self.atual = 0
        self.atual += 1
        self.set_texture(self.atual)
        time.sleep(.5)


