import pygame
from random import randint

class Enemy():
    """Класс поведения противника"""
    def __init__(self, ai_game):    

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/marisa.png')
        self.rect = self.image.get_rect(midtop=self.screen_rect.midtop)
        #Опускание от верхней точки окна для вывода статистики игры
        self.rect.y += 50
        self.new_position = self.rect.centerx

        self.x = float(self.rect.x)

    def create_new_position(self):
        """Создание новой позиции для перемещения"""
        self.new_position = randint(50, self.screen_rect.width-50)

    def update_position(self):
        """Обновление позиции"""
        if self.rect.centerx != self.new_position:
            if self.rect.centerx < self.new_position:
                self.x += 0.5
            elif self.rect.centerx > self.new_position:
                self.x -= 0.5
            self.rect.x = self.x

    def blit_me(self):
        """Рисует Марису в текущей позиции"""
        self.screen.blit(self.image, self.rect)

