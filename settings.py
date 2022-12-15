import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует татические настройки игры."""
        self.screen_width = 500
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.monitor = 0
        self.bg_image = pygame.image.load('images/background.png')
        self.player_speed = 2.5

        self.bullet_speed = 4
        self.ball = 1
        self.point_speed = 1
        self.time_spawn_new_point = 1000 #ms
        self.time_change_enemy_position = 5000 #ms

        self.start_damage = 15
        self.max_variable_damage = 30
        self.variable_damage = 0
        self.neutral_status_time = 2000
        self.max_player_lives = 8

        self.update_full_damage()
        self.initialize_dynamic_settings()

    def update_full_damage(self):
        """Обновляет значение общего урона и урона за одно попадание"""
        self.full_damage = self.start_damage + self.variable_damage
        self.damage_for_hit = int(self.full_damage / self.ball)

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.score_for_hit = 10

        self.star_speed = 1
        self.time_star_spawn = 1000
        self.player_lives = 1
        self.level = 1
        self.start_enemy_hp = 1000
        self.enemy_hp = self.start_enemy_hp
        self.spawn_stars = 1

    def level_up(self):
        """Увеличивает настройки сложности для нового уровня"""
        self.level += 1
        if self.level <= 8:
            self.star_speed += 0.2
            self.time_star_spawn = int(self.time_star_spawn*0.9) 
            self.start_enemy_hp += 500
            #Увеличение кол-ва спавнушихся звезд за раз каждые уровня
            self.spawn_stars = int(self.level / 3)+1

        if self.player_lives < self.max_player_lives:
            self.player_lives += 1
        self.score_for_hit += 5
        self.enemy_hp = self.start_enemy_hp


