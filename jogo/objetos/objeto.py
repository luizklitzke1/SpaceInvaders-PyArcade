import arcade

class Objeto(arcade.Sprite):

    def __init__(self, imagem, dimensao_imagem, center_x=0, center_y=0):
        super().__init__(imagem, dimensao_imagem)
        self.center_x = center_x
        self.center_y = center_y

    def set_center_x(self, novo_x):
        self.center_x = novo_x

    def get_center_x(self):
        return self.center_x

    def set_center_y(self, novo_y):
        self.center_y = novo_y
        
    def get_center_y(self):
        return self.center_y

    #Remove o objeto da tela caso passe dos limites:
    def remover_se_sair(self, width, height,  bottom, top, left, right):
        if bottom < 50 or top > height - 70 or right < 0 or left > width:
            self.kill()
