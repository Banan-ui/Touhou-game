import pygame

class LifeBar():
    """Класс для создания полоски жизни врага"""
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Цвета
        self.green = (100, 240, 40)
        self.red = (250, 40, 10)

        #Прямоугольник красной полоски жизни
        self.border = 12
        self.rect_width = self.screen_rect.width-self.border*2
        self.rect = pygame.Rect(self.border, self.border, 
            self.rect_width, self.border)

        self.new_bar_settings()        
        self.create_green_bar()

    def new_bar_settings(self):
        """Создание пропорции одного пиксеся полоски жизни к кол-ву хп"""
        self.one_pixel_hp = self.settings.start_enemy_hp / self.rect_width #float

    def create_green_bar(self):
        """Создание зеленой полоски для отображения оставшегося здоровья"""
        green_distant = int(self.settings.enemy_hp / self.one_pixel_hp)
        self.green_rect = pygame.Rect(self.border, self.border,
            green_distant, self.border)

    def draw_bars(self):
        """Отрисовка полосок"""
        self.screen.fill(self.red, self.rect)
        self.screen.fill(self.green, self.green_rect)


