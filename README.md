# Space Invaders - PyArcade

Projeto desenvolvido em Python3.7 utilizando a biblioteca [PyArcade](http://arcade.academy/) que visa recriar o classico jogo **"Space Invaders" **,
porém, com uma jogabilidade competitiva aonde dois jogadores competem por mais pontos contra uma invasão alien.

## Desenvolvimento do projeto

O jogo foi projetado como uma forma de aprendizado da biblioteca [PyArcade](http://arcade.academy/) e da O.O.P como um todo, na disciplina de Programação do segundo ano de **Técnico de Informática no Instituto Federal Catarinense - Campus Blumenau**.

Os aspectos principais foram planejados para a disciplina de **Engenharia de Sofwate** e podem ser econtrados em:

* [Diagrama de Classes - UML ](https://www.lucidchart.com/invitations/accept/521ac160-6dbe-4b68-99d4-3f349e7ae05e) - Utilizado como base para as funcionalidades e lógica das classes.
* [Requisitos Funcionais e Não-Funcionais](https://docs.google.com/document/d/1MDXXXvBGJVtEZA573gmeRsSRpweHLWi_mhOSCG5KCzw/edit?usp=sharing) - Requisitos levantados para o projeto.


[![menu1.gif](https://s5.gifyu.com/images/menu1.gif)](https://gifyu.com/image/mFcE)


## Instalação e Uso

O programa pode ser tanto rodado a partir da execução do arquivo "jogo.py" ou instalado como um pacote, incluindo assim todas as classes para uso em outros projetos.
(A Instalação é bem simples, utilizando apenas o sistema simples de packages)

### Requerimentos

O projeto faz o uso, principalmente, da biblioteca PyArcade e dos seus próprios Requerimentos, porém tudo deve ser atendido com um simples pip install do arquivo requirements.txt, naturalmente presente no pacote.

Em caso de problemas ou dúvidas, apenas rode o seguinte no terminal, uma vez dentro da pasta:
```
python3 -m pip install -r requirements.txt
```

### Compreensão por terceiros

Toda a funcionalidade do projeto é extensamente comentada e explicada no seu decorrer, para um melhor entendimento de alguem que possa querer modifica-lo ou vir a utiliza-lo como base.


## Gameplay

[![gp2b2b4c5d648b06cea.gif](https://s5.gifyu.com/images/gp2b2b4c5d648b06cea.gif)](https://gifyu.com/image/mFc0)

Já na tela inicial, o jogador é apresentado aos comandos básicos de movimentação e ataque.
Cada um dos aliens são criados de maneira específica para sua coluna, com uma textura e dando uma pontuação diferente ao serem abatidos.

```
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
```
A partir dai, o jogo segue o modelo clássico de SpaceInvaders, no qual várias fileiras de aliens se movem em direção dos jogadores, ganhando velocidade conforme mais deles são abatidose os níveis avançam.

```
# Cálculo da velocidade dos inimigos, dependendo de quantos há na tela
            if self.direcao_inimigos == 0:   #Movimento dos inimigos for para a direita (eixo x positivo)
                self.velocidade_inimigos = 1.2 + self.inimigos_mortos*(0.02*self.nivel/4)
            elif self.direcao_inimigos == 1: #Movimento dos inimigos for para a esquerda (eixo x negativo)
                self.velocidade_inimigos = -(1.2 + self.inimigos_mortos*0.02*self.nivel/4)
```

### Multiplayer
Diferentemente do original, essa versão apresenta jogabilidade de dois jogadores, no qual ambos tentam se defender dos aliens, porém competem para ver quem consegue a maior pontuação no final, a qual é demonstrada em tempo real no topo da tela, incluindo qual deles está vencendo no momento.
Cada jogador também possuí seu próprio número de vidas, sendo que o jogo só acaba quando as de ambos forem esgotadas.

[![score2.gif](https://s5.gifyu.com/images/score2.gif)](https://gifyu.com/image/mFc9)

### Cobertura
Pode-se tambem notar que há diferentes coberturas para proteger os jogadores dos lazers inimigos e vice-versa.
Essas coberturas são destruídas de maneria dinâmica pelos disparos e compostas por uma série de diferentes pedaços, de maneira que cada um seja independente.

[![Imagem das coberturas](https://s5.gifyu.com/images/cover1.gif)](https://gifyu.com/image/mFc3)
```
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
```
