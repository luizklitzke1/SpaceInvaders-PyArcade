import arcade
import random
import time
from objetos.cover import Bloco_cover
from objetos.projeteis import Laser_jogador, Laser_alien
from personagens.aliens import Alien, Misterio
from personagens.jogador import Jogador
from objetos.interface import Interface, Menu_inicial


#Constantes do jogdo
LARGURA_TELA = 700
ALTURA_TELA = 800
TITULO_TELA = "Space Invaders Part II - PyArcade Version"
FONTE = 'jogo/fonts/space_invaders.ttf'


class Jogo(arcade.Window):

    def __init__(self):

        super().__init__(LARGURA_TELA, ALTURA_TELA, TITULO_TELA, antialiasing=True)
        arcade.set_background_color((0,0,0))
        self.interface = Interface(FONTE)

    #Setup de todos os elementos do jogo
    def setup(self, nivel = 1, pont1 = 0, vida1 = 3 , pont2 = 0, vida2 = 3, estado = 4):  
        
        # Criação da tela inicial
        self.menu_inicial = Menu_inicial()

        # Criação dos inimigos, linha por linha
        self.lista_inimigos = arcade.SpriteList()
        self.inimigos_mortos = 0
        for linha in range (5):
            if linha == 0 or linha == 1:
                tipo = '1'
            elif linha == 2:
                tipo = '2'
            else:
                tipo = '3'
            for inimigo in range (10):
                coluna = inimigo + 1
                novo_alien = Alien(tipo, .8, 100 + inimigo*55 , 630 - (linha*42), coluna)
                self.lista_inimigos.append(novo_alien)
                
        #Criação da lista para os lasers dos inimigos
        self.lista_laser_inimigos = arcade.SpriteList()
        self.colunas_restantes = []
        
        #Direção da movimentação dos inimigos   (0 = Direita,  1 = Esquerda)
        self.direcao_inimigos = 0
    
        # Criação dos jogadores e das listas para guardar seus lasers
        self.lista_jogadores = arcade.SpriteList()
        jogador1 = Jogador('1', vida1, 1, 4, 125, 80, arcade.key.A, arcade.key.D, arcade.key.W, pont1)
        jogador2 = Jogador('2', vida2, 1, 4, 575, 80, arcade.key.LEFT, arcade.key.RIGHT, arcade.key.UP, pont2)
        self.lista_jogadores.append(jogador1)
        self.lista_jogadores.append(jogador2)
        self.jogadores_mortos = 0

        # Criação da velocidade geral dos inimigos no inicio do jogo
        self.velocidade_inimigos = 1.2

        # Quantidade de vezes que os updates foram loopados 
        # (usado para mudar sprites devido a problemas com o animated walking sprite)
        self.loops = 0
        self.resets = 0
        self.update_time = 20

        # Definição do nível do jogo
        self.nivel = nivel

        # Sorteio da chance do misterio aparecer
        self.lista_naves = arcade.SpriteList()
        if self.nivel != 1:
            if random.randint(1,5) == 1:
                nova_nave = Misterio(10, 680, 'misterio')
                self.lista_naves.append(nova_nave)
                arcade.play_sound(arcade.load_sound('jogo/sons/mysteryentered.wav'))

        # Definição do estado do jogo    (0 - Pausado  1 - Rodando  2- Avançar nivel  3- Game Over  4 - Menu Inicial)
        self.estado = estado
        
        # Criação dos covers, (na verdade listas de bloquinhos destrutíveis(Bloco_cover))
        self.lista_covers = []
    
        for cover in range (4):
            novo_cover = arcade.SpriteList()
            center_x = 120+cover*150
            center_y = 150

            for linha in range (4):
                for coluna in range (8):
                    bloco_x = center_x-28 + coluna*10      
                    # Cálculo X = Pega o center_x do cover como um todo, menos ele dividido por 2 menos metade 
                    #de um quadrado (10/2) mais a quantidade de colunas que já foram vezes a larugra dum bloco
                    bloco_y = center_y+43 - linha*10
                    # Cálculo Y = Pega o center_y do cover como um todo, menos ele  dividido por 2 menos a metade
                    # de um quadrado (10/2) mais a quantidade de linhas percorridas vezes a altura dum bloco
                    novo_bloco = Bloco_cover(bloco_x, bloco_y, 1)
                    novo_cover.append(novo_bloco)
            self.lista_covers.append(novo_cover)
  
    def on_key_press(self, key, modifiers): # O que executar ao pressionar uma tecla #

        #Sair da tela inicial
        if self.estado == 4:
            if key == arcade.key.W or key == arcade.key.UP:
                self.estado = 1

        #Sair da tela de game over
        elif self.estado == 3:
            if key == arcade.key.W or key == arcade.key.UP:
                self.setup()

        else: 
            # Resetar o jogo
            if key == arcade.key.R:
                self.setup(1)

            # Pausar o jogo
            if key == arcade.key.P:
                if self.estado == 1:
                    self.estado = 0
                else:
                    self.estado = 1
            
            # Debug nivel  - Deixar um inimigo vivo pra testes
            if key == arcade.key.F:
                for inimigo in self.lista_inimigos[:-1]:
                    inimigo.kill()
                for cover in self.lista_covers:
                    self.lista_covers.remove(cover)
            
            # Debug nivel  - Causar game over 
            if key == arcade.key.G:
                for jogador in self.lista_jogadores:
                    jogador.remover_vidas(3)

        #Se estive rodando normal  - Separado pra não dar de atirar no pause
        if self.estado == 1:
            # Atualização no jogadores
            for jogador in self.lista_jogadores:
                jogador.on_key_press(key, modifiers)


    
    def on_key_release(self, key, modifiers): # O que executar ao soltar uma tecla #

        # Movimentação dos jogadores
        for jogador in self.lista_jogadores:
            jogador.on_key_release(key, modifiers)

    def on_draw(self):  # Desenhar os itens na tela #

        arcade.start_render()

        #Mostrar menu inicial
        if self.estado == 4:
            self.menu_inicial.draw()
        
        #Mostrar tela game over
        elif self.estado == 3:
            self.interface.mostrar_game_over(self.nivel, self.lista_jogadores[0].get_pontos(),self.lista_jogadores[1].get_pontos())

        #Elementos do jogo em execução normal
        else:
            self.lista_naves.draw()

            for cover in self.lista_covers:
                cover.draw()
            self.lista_jogadores.draw()
            self.lista_inimigos.draw()
            for jogador in self.lista_jogadores:
                jogador.lista_lasers.draw()
            self.lista_laser_inimigos.draw()

            arcade.draw_rectangle_filled(0, 50, 1600, 5, (255, 0 ,0),)

            # Informa o texto do topo
            self.interface.mostrar_texto_topo()

            # Informa pontuação na tela
            self.interface.mostrar_pontuacao(self.lista_jogadores)

            # Informa as vidas na tela
            self.interface.mostrar_vidas(self.lista_jogadores)

            # Informa o nível atual
            self.interface.mostrar_nivel(self.nivel)

            # Informa se o jogo está pausado
            if self.estado == 0:
                self.interface.mostrar_menu_pause()

            # Informe se avançar de nivel
            if self.estado == 2:
                self.interface.mostrar_avancar_nivel(self.nivel)

    def update(self, delta_time): # O que é atualizado constantemente com o jogo rodando 

        # Todas as ações dependende do update_time, definido no setup, pra saber o quao constantemente serão executadas
        # Cada passagem de update += 1 loop de update, o update_time é a quantidade dessses loops pra cada atualização

        # Checa se o jogo esta pausado
        if self.estado == 1:

            #Atualiza a velocida de update baseado na quantidade de inimigos mortos
            temp_up = int(20 - (self.inimigos_mortos*0.28))
            self.update_time = int(temp_up)

            # Checa se há um jogador vivo
            # Muda a textura e trava jogador caso morrer  (Explicação em jogador.py)  
            self.jogadores_mortos = 0
            for jogador in self.lista_jogadores:
                jogador.mudar_textura(self.loops, self.resets, self.update_time)
                if jogador.get_estado() == 'mortofull':
                   self.jogadores_mortos += 1
            if self.jogadores_mortos == 2:
                self.estado = 3

            # Checa se deve avançar de nivel
            if len(self.lista_inimigos) == 0 :
                self.nivel+=1                
                self.estado = 2

            # Update do mistério
            for nave in self.lista_naves:
                nave.change_x = 1

            # Update dos inimigos
            self.lista_inimigos.update()
            self.lista_inimigos.update_animation()
            self.lista_laser_inimigos.update()
            self.lista_laser_inimigos.update_animation()
            self.lista_naves.update()
            self.lista_naves.update_animation()


            # Cálculo da velocidade dos inimigos, dependendo de quantos há na tela
            if self.direcao_inimigos == 0:   #Movimento dos inimigos for para a direita (eixo x positivo)
                self.velocidade_inimigos = 1.2 + self.inimigos_mortos*(0.02*self.nivel/4)
            elif self.direcao_inimigos == 1: #Movimento dos inimigos for para a esquerda (eixo x negativo)
                self.velocidade_inimigos = -(1.2 + self.inimigos_mortos*0.02*self.nivel/4)


            # Movimentação dos inimigos e mudança de sprites
            for inimigo in self.lista_inimigos:
                if inimigo.get_estado() == 'vivo':
                    if self.loops == self.update_time:
                        inimigo.mudar_textura_andar()

                    #Atualiza a velocidade    
                    inimigo.change_x = self.velocidade_inimigos

                    #Verifica se bateu na parede direita
                    if inimigo.get_center_x()  > 650:
                        for i in self.lista_inimigos:
                            i.set_center_x(i.get_center_x()-1)
                            i.set_center_y(i.get_center_y()-5)
                        self.direcao_inimigos = 1

                    #Verifica se bateu na parede esquerda
                    elif inimigo.center_x < 50:
                        for i in self.lista_inimigos:
                            i.set_center_x(i.get_center_x()+1)
                            i.set_center_y(i.get_center_y()-5)
                        self.direcao_inimigos = 0

                    #Verifica se bateu chegou na altura dos jogadores
                    elif inimigo.center_y < 100:
                        self.estado = 3

                #Matar o inimigo
                else:
                    if self.loops == 5:
                        inimigo.kill()
                        self.inimigos_mortos += 1


            # Toca os sons de transição dos inimigos (separado pra não sobrepor)
            if self.resets %2 == 0 and self.loops == self.update_time:
                arcade.play_sound(arcade.load_sound('jogo/sons/0.wav'))
            elif self.loops == self.update_time:
                arcade.play_sound(arcade.load_sound('jogo/sons/1.wav'))
            

            # Descobrir quais colunas ainda tem inimigos vivos
            self.colunas_restantes = []
            for inimigo in self.lista_inimigos:
                if not(inimigo.get_coluna() in self.colunas_restantes):
                    self.colunas_restantes.append(inimigo.get_coluna())

            # Sorteia a coluna para atirar e atira com algum inimigo dela
            if len(self.colunas_restantes) > 0:
                sorteio_coluna = random.choice(self.colunas_restantes)
                
            #Acha um inimigo na coluna sorteada e atira
            if len(self.lista_laser_inimigos) < (self.nivel//6)+1:
                for inimigo in reversed(self.lista_inimigos):
                    if inimigo.get_coluna() == sorteio_coluna:
                        novo_laser_inimigo = Laser_alien(inimigo.center_x, inimigo.bottom-20, -4)
                        self.lista_laser_inimigos.append(novo_laser_inimigo)
                        break      
                    
            
            # Atualiza o sprite do laser dos aliens (separado para ser mais rápido)
            if self.loops == 5:
                if self.resets % 2 == 0:
                    for laser in self.lista_laser_inimigos:
                        laser.set_texture(1)
                else:
                    for laser in self.lista_laser_inimigos:
                        laser.set_texture(0)
                
            # Update dos covers
            for cover in self.lista_covers:
                cover.update()
                cover.update_animation()

            # Update dos jogadores
            self.lista_jogadores.update()
            self.lista_jogadores.update_animation()
             
            #Update dos lasers dos jogadores
            for jogador in self.lista_jogadores:


                # Checa se o jogador está vivo
                if jogador.get_vidas() <= 0:
                    jogador.set_vidas(0)
                    jogador.set_estado('mortofull')
                    jogador.set_texture(1)

                else:
                    #Manter eles na tela
                    jogador.manter_na_tela(self.width, self.height, jogador.bottom, jogador.top, jogador.left, jogador.right)

                    # Checa a colisão com laseres inimigos
                    hit_list = arcade.check_for_collision_with_list(jogador, self.lista_laser_inimigos)
                    if len(hit_list) > 0:
                        jogador.remover_vidas(1)
                        jogador.set_estado('morto')

                    # Checagem da colisão do laser dos jogadores    
                    jogador.lista_lasers.update()
                    jogador.lista_lasers.update_animation()
                    for laser in jogador.lista_lasers:
                        laser.change_y = laser.speed

                        # Checa se o laser bate em um cover e se o remove
                        for cover in self.lista_covers:
                            hit_list = arcade.check_for_collision_with_list(laser, cover)
                            if len(hit_list) > 0:
                                laser.kill()
                            for bloco in cover:
                                if arcade.check_for_collision(bloco, laser):
                                    bloco.kill()

                        # Checa se o laser bate em um inimigo e se o remove
                        hit_list = arcade.check_for_collision_with_list(laser, self.lista_inimigos)
                        if len(hit_list) > 0:
                            laser.kill()
                            # Adiciona pontuação e faz som caso acertar inimigo
                            for inimigo in hit_list:
                                inimigo.set_texture(2)
                                inimigo.set_estado('morto')
                                arcade.play_sound(inimigo.get_som_morte())
                                jogador.adicionar_pontos(inimigo.get_pontuacao())

                        # Checa se o laser bate em um misterio e se o remove
                        hit_list = arcade.check_for_collision_with_list(laser, self.lista_naves)
                        if len(hit_list) > 0:
                            laser.kill()
                            for nave in hit_list:
                                if nave.get_vida() == 0:
                                    nave.kill()
                                    jogador.adicionar_pontos(nave.get_pontos())
                                    arcade.play_sound(arcade.load_sound('jogo/sons/mysterykilled.wav'))
                                else:
                                    nave.remover_vida(1)

                        # Checa se bate em um laser de alien e o remove
                        hit_list = arcade.check_for_collision_with_list(laser, self.lista_laser_inimigos)
                        if len(hit_list) > 0:
                            self.lista_laser_inimigos.pop()

                        # Se o laser sair da tela, remove ele
                        laser.remover_se_sair(self.width, self.height, laser.bottom, laser.top, laser.left, laser.right)
                        
            #Update dos lasers dos inimigos
            for laser in self.lista_laser_inimigos:
                laser.change_y = laser.get_speed()

                #Checa se algum bate num jogador
                hit_list = arcade.check_for_collision_with_list(laser, self.lista_jogadores)
                if len(hit_list) > 0:
                    laser.kill()

                # Checa se o laser bate em um cover e se o remove
                for cover in self.lista_covers:
                    hit_list = arcade.check_for_collision_with_list(laser, cover)
                    if len(hit_list) > 0:
                        laser.kill()
                    for bloco in cover:
                        if arcade.check_for_collision(bloco, laser):
                            bloco.kill()

                # Checa se o laser bate em outro alien e o joga para baixo
                for inimigo in self.lista_inimigos:
                    hit_list = arcade.check_for_collision_with_list(laser, self.lista_inimigos)
                    if len(hit_list) > 0:
                        laser.center_y+= -40
                
                # Se o laser bater no limite inferior da tela, remover ele
                laser.remover_se_sair(self.width, self.height, laser.bottom, laser.top, laser.left, laser.right)

            # Reinicia os loops umas vez que feche o update_time
            if self.loops == self.update_time:  
                self.resets += 1
                self.loops = 0
            else:
                self.loops +=1  

        # Mostrar tela de passar de fase
        elif self.estado == 2:
            self.setup(self.nivel, self.lista_jogadores[0].get_pontos(), self.lista_jogadores[0].get_vidas(), self.lista_jogadores[1].get_pontos(), self.lista_jogadores[1].get_vidas(), 1)
            time.sleep(1.5)

        # Mostra a tela de menu inicial
        elif self.estado == 4:
            self.menu_inicial.update(self.loops)
        
        
def main(): # Criação da janela, chamada do setup, e ordem para inicialização 

    window = Jogo()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()