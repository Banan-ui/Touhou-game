import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует татические настройки игры."""
        self.screen_width = 500
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.monitor = 1
        self.bg_image = pygame.image.load('images/background.png')
        self.player_speed = 1
