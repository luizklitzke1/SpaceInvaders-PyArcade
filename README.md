# Space Invaders - PyArcade

Projeto desenvolvido em Python3.7 utilizando a biblioteca [PyArcade](http://arcade.academy/) que visa recriar o classico jogo **Space Invaders**,
porém, com uma jogabilidade multiplayer local, aonde dois jogadores competem por mais pontos contra uma invasão alien.

## Desenvolvimento do projeto

O jogo foi projetado como uma forma de aprendizado da biblioteca [PyArcade](http://arcade.academy/) e de **O.O.P** como um todo, na disciplina de Programação do segundo ano de **Técnico de Informática no Instituto Federal Catarinense - Campus Blumenau**.

Os aspectos principais foram planejados para a disciplina de **Engenharia de Sofwate** e podem ser econtrados em:

* [Diagrama de Classes - UML ](https://www.lucidchart.com/invitations/accept/521ac160-6dbe-4b68-99d4-3f349e7ae05e) - Utilizado como base para as funcionalidades e lógica das classes.
* [Requisitos Funcionais e Não-Funcionais](https://docs.google.com/document/d/1MDXXXvBGJVtEZA573gmeRsSRpweHLWi_mhOSCG5KCzw/edit?usp=sharing) - Requisitos levantados para o projeto.


[![menu1.gif](https://s5.gifyu.com/images/menu1.gif)](https://gifyu.com/image/mFcE)


## Instalação e Uso

O programa pode ser tanto rodado a partir da execução do arquivo "jogo.py" ou instalado como um pacote, incluindo assim todas as classes para uso em outros projetos.
(A Instalação é bem simples, utilizando apenas o sistema de packages)

### Requerimentos

O projeto faz o uso, principalmente, da biblioteca PyArcade e dos seus próprios Requerimentos, porém tudo deve ser atendido com um simples pip install do arquivo requirements.txt, naturalmente presente no pacote.

```
python3 -m pip install -r requirements.txt
```

### Compreensão por terceiros

Toda a funcionalidade do projeto é extensamente comentada e explicada no seu decorrer, para um melhor entendimento de alguem que possa querer modifica-lo ou vir a utiliza-lo como base.


## Gameplay

[![gp2b2b4c5d648b06cea.gif](https://s5.gifyu.com/images/gp2b2b4c5d648b06cea.gif)](https://gifyu.com/image/mFc0)

Já na tela inicial, o jogador é apresentado aos comandos básicos de movimentação e ataque.

Cada um dos aliens são criados de maneira específica para sua coluna, com uma textura e pontuação específica.

A partir dai, o jogo segue o modelo clássico de **SpaceInvaders**, no qual várias fileiras de aliens se movem em direção dos jogadores, ganhando velocidade conforme mais deles são abatidose os níveis avançam.


### Multiplayer
Diferentemente do original, essa versão apresenta jogabilidade de dois jogadores local, no qual ambos tentam se defender dos aliens, porém competem para ver quem consegue a maior pontuação no final, a qual é demonstrada em tempo real no topo da tela, incluindo qual deles está vencendo no momento.
Cada jogador também possuí seu próprio número de vidas, sendo que o jogo só acaba quando as de ambos forem esgotadas.

[![score2.gif](https://s5.gifyu.com/images/score2.gif)](https://gifyu.com/image/mFc9)

### Cobertura
Pode-se tambem notar que há diferentes coberturas para proteger os jogadores dos lazers inimigos e vice-versa.
Essas coberturas são destruídas de maneria dinâmica pelos disparos e compostas por uma série de diferentes pedaços, de maneira que cada um seja independente.

[![Imagem das coberturas](https://s5.gifyu.com/images/cover1.gif)](https://gifyu.com/image/mFc3)

