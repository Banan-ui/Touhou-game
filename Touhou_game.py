import sys
import pygame

from settings import Settings
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

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            self._check_events()
            self.player.update()
            self._update_screen()


    def _check_events(self):
        """Отслеживание событий игры"""         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

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

    def _check_key_up(self, event):
        """При отпускании клавиш"""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
            self.player.change_image()
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False 
            self.player.change_image()

    def _update_screen(self):
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg_image, (0, 0))

        self.player.blitme()
        pygame.display.flip()
 
if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = TouhouGame()
    ai.run_game()