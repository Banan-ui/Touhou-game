import pygame
from pygame.sprite import Sprite
from random import randint

from rect_collision import RectCollision

class Star(Sprite):
    """Класс для создания вражеских звезд"""
    def __init__(self, ai_game):
        """Инициализация звезды"""
        super().__init__()

        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.main_image = pygame.image.load("images/star.png")
        self.image = self.main_image
        self.center_position = [randint(50, self.screen_rect.width-50),
            -self.image.get_height()/2] #Центрольная точка звезды

        self.rect = self.image.get_rect(center=self.center_position)
        self.angle = 0

        self.rect_collision = RectCollision(self.rect.center, 30, ai_game.screen)

    def update(self):
        """Перемещение и поворот звезды"""
        #Поворот звезды
        if self.angle < 360:
            self.angle += 1
        else:
            self.angle = 0
        self.image = pygame.transform.rotate(self.main_image, self.angle)

        #Смена положения
        self.center_position[1] += self.settings.star_speed #Изменения позиции по y

        #Пересоздания rect
        self.rect = self.image.get_rect(center=self.center_position)
        self.rect_collision.rect.center = self.rect.center
