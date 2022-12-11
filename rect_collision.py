import pygame

from pygame.sprite import Sprite

class RectCollision(Sprite):
    """Создание класса квадрата для проверки пересечений"""
    def __init__(self, center, side, screen):
        """Создание прямоугольника в центре спрайта с указанной длиной стороны"""
        super().__init__()
        self.rect = pygame.Rect(0, 0, side, side)
        self.rect.center = center
        self.image = pygame.image.load('images/bullet.png')


        #Для тестов
        self.screen = screen
        self.color = (255, 0, 0)

    def update(self):
        """Отрисовка прямоугольника на экране(для тестов)"""
        pygame.draw.rect(self.screen, self.color, self.rect)


