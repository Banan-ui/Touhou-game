import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game, side):
        """Создает объект пуль в указанном положении шара."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/bullet.png')
 
        # Создание снаряда в позиции (0,0) и назначение правильной позиции.
        if side == "left":
            self.rect = self.image.get_rect(midleft = ai_game.player.rect.midleft)
        elif side == "right":
            self.rect = self.image.get_rect(midright = ai_game.player.rect.midright)
        elif side == "center":
            self.rect = self.image.get_rect(midbottom = ai_game.player.rect.midtop)
 
        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает пулю вверх по экрану."""
        # Обновление позиции снаряда в вещественном формате.
        self.y -= self.settings.bullet_speed
        # Обновление позиции прямоугольника.
        self.rect.y = self.y

