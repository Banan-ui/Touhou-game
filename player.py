import pygame

class Player():
    """Класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение корабля и получает прямоугольник.
        self.left_image = pygame.image.load('images/reimu_left.png')
        self.right_image = pygame.image.load('images/reimu_right.png')
        self.idle_image = pygame.image.load('images/reimu_idle.png')
        self.image = self.idle_image
        self.rect = self.image.get_rect()

        #Булевые значения движениея
        self.moving_left = False
        self.moving_right = False

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 20

        self.x = float(self.rect.x)

    def update(self): #side 1 влево, 0 в право
        if self.moving_left and self.rect.x > 0:
            self.x -= self.settings.player_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        self.rect.x = self.x  

    def change_image(self):
        if self.moving_right and self.moving_left:
            self.image = self.idle_image
        elif self.moving_left:
            self.image = self.left_image
        elif self.moving_right:
            self.image = self.right_image
        else:
            self.image = self.idle_image

    def blitme(self):
        """Рисует персонажа в текущей позиции."""
        self.screen.blit(self.image, self.rect)
