import sys
import pygame

from settings import Settings
from bullet import Bullet
from player import Player

class TouhouGame:
    """Класс для управления ресурсами и поведением игры."""
 
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
 
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height), display=self.settings.monitor)
        pygame.display.set_caption("Touhou game")
 
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.fire = False

        #Таймер для ограничения скорости создания пуль
        self.fire_timing = True


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            self._check_events()
            self.player.update()
            if self.fire and self.fire_timing:
                self._create_bullets()
            self._update_bullets()
            self._update_screen()

    def _create_bullets(self): #!!!
        """Создание новых пуль в соответствии с кол-вом и расположением шаров"""
        self.fire_timing = False
        if self.settings.ball == 1:
            self.bullets.add(Bullet(self, "center"))
        elif self.settings.ball == 2:
            self.bullets.add(Bullet(self, "right"))
            self.bullets.add(Bullet(self, "left"))
        elif self.settings.ball == 3:
            self.bullets.add(Bullet(self, "right"))
            self.bullets.add(Bullet(self, "left"))
            self.bullets.add(Bullet(self, "center"))


    def _update_bullets(self):
        """Обновление позиции и удаления пуль"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_timings(self):
        """Сброс таймера при начале стрельбы"""
        pygame.time.set_timer(pygame.USEREVENT, 100)


    def _check_events(self):
        """Отслеживание событий игры"""         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)
            elif event.type == pygame.USEREVENT:
                self.fire_timing = True        

    def _check_key_down(self, event):
        """При нажатии клавиш"""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
            self.player.change_image()
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
            self.player.change_image()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_z:
            self.fire = True
            self._create_timings()

    def _check_key_up(self, event):
        """При отпускании клавиш"""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
            self.player.change_image()
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False 
            self.player.change_image()
        elif event.key == pygame.K_z:
            self.fire = False

    def _update_screen(self):
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg_image, (0, 0))
        self.player.blitme()
        self.bullets.draw(self.screen)
        pygame.display.flip()
 
if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = TouhouGame()
    ai.run_game()