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
        self.player_speed = 2

        self.bullet_speed = 4
        self.ball = 1
        self.point_speed = 1
        self.time_spawn_new_point = 1000 #ms
        self.time_change_enemy_position = 5000 #ms

        self.start_damage = 15
        self.max_variable_damage = 30
        self.variable_damage = 0

        self.update_full_damage()

        self.start_enemy_hp = 1000
        self.enemy_hp = 1000
        

    def update_full_damage(self):
        """Обновляет значение общего домага и домага за одно попадание"""
        self.full_damage = self.start_damage + self.variable_damage
        self.damage_for_hit = int(self.full_damage / self.ball)
