import pygame
from pygame.sprite import Sprite
from random import randint

class Point(Sprite):
    """Класс поинта увеличения силы"""
    def __init__(self, ai_game):
        """Создания поинта"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/power.png')

        """Создание рандомной позиции поинта за экраном"""
        self.rect = self.image.get_rect()
        random_pos = randint(self.rect.width, self.screen_rect.width-self.rect.width*2)

        self.rect.y = -self.rect.height
        self.rect.x = random_pos

    def update(self):
        self.rect.y += self.settings.point_speed






