import pygame

from rect_collision import RectCollision

class Player():
    """Класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение корабля и получает прямоугольник.
        self.left_image = pygame.image.load('images/reimu_left.png')
        self.right_image = pygame.image.load('images/reimu_right.png')
        self.idle_image = pygame.image.load('images/reimu_idle.png')
        self.all_player_images = [self.left_image, self.right_image, self.idle_image]
        self.image = self.idle_image
        self.rect = self.image.get_rect()

        #Загружаем изображения шаров
        self.ball_images = [pygame.image.load('images/ball_1.png'), 
            pygame.image.load('images/ball_2.png'), 
            pygame.image.load('images/ball_3.png')]
        self.update_ball_image()

        #Булевые значения движениея
        self.moving_left = False
        self.moving_right = False

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 20

        self.rect_collision = RectCollision(self.rect.center, 20, ai_game.screen)


        self.x = float(self.rect.x)

    def update(self): #side 1 влево, 0 в право
        if self.moving_left and self.rect.x > 0:
            self.x -= self.settings.player_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        self.rect.x = self.x
        self.rect_collision.rect.center = self.rect.center

    def update_ball_image(self):
        self.ball_image = self.ball_images[self.settings.ball-1]

    def change_image(self):
        if self.moving_right and self.moving_left:
            self.image = self.idle_image
        elif self.moving_left:
            self.image = self.left_image
        elif self.moving_right:
            self.image = self.right_image
        else:
            self.image = self.idle_image


    def reset_position(self):
        """Перемещение персонажа на изначальную позицию"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 20
        self.x = float(self.rect.x)
        self.change_images_alpha(100)

    def change_images_alpha(self, value=255):
        """Изменение прозрачности изображений"""
        #Изменение прозрачно изображений персонажа
        for image in self.all_player_images:
            image.set_alpha(value)
        #Изменение прозрачно изображений шаров
        for image in self.ball_images:
            image.set_alpha(value)


    def blitme(self):
        """Рисует персонажа в текущей позиции."""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.ball_image, self.rect)

