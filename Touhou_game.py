import sys
import pygame

from settings import Settings
from bullet import Bullet
from player import Player
from point import Point
from enemy import Enemy
from life_bar import LifeBar

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
        self.enemy = Enemy(self)
        self.bullets = pygame.sprite.Group()
        self.points = pygame.sprite.Group()
        self.life_bar = LifeBar(self)

        self.fire = False


        #Таймер для ограничения скорости создания пуль и создания поинтов
        pygame.time.set_timer(pygame.USEREVENT+1, self.settings.time_spawn_new_point)
        self.fire_timing = True

        #Таймер для смещение позиуии противника
        pygame.time.set_timer(pygame.USEREVENT+2, self.settings.time_change_enemy_position)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            self._check_events()
            self.player.update()
            if self.fire and self.fire_timing:
                self._create_bullets()
            self._update_bullets()
            self.enemy.update_position()
            self._update_points()
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
        self._check_ballet_enemy_collisions()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _check_ballet_enemy_collisions(self):
        """Проверка колиизии Марисы и пуль"""
        collision = pygame.sprite.spritecollideany(self.enemy, self.bullets)
        if collision:
            #Уменьшение хп и перерисовка полоски жизни
            self.settings.enemy_hp -= self.settings.damage_for_hit
            self.life_bar.create_green_bar()
            collision.kill()

    def _update_points(self):
        """Обновления позиции поинта"""
        self.points.update()
        if self.points:
            self._check_point_player_collisions()
        for point in self.points.copy():
            if point.rect.top >= self.screen.get_height():
                self.points.remove(point)

    def _check_point_player_collisions(self):
        """Проверка коллизий поинта с персонажем"""
        collision = pygame.sprite.spritecollideany(self.player, self.points)
        if collision:
            collision.kill()
            if self.settings.variable_damage < self.settings.max_variable_damage:
                self._added_damage_and_change_ball()

    def _added_damage_and_change_ball(self):
        """Увеличение урона и изменение количества шаров"""
        self.settings.variable_damage += 1

        leaving = self.settings.variable_damage % 10 #Кратное десяти
        if not leaving and self.settings.variable_damage < 30:
            """0 -> 9 = 1 ball;
            10 -> 19 = 2 balls;
            20 -> max_damage = 3 balls"""
            self.settings.ball = int(self.settings.variable_damage / 10)+1
            self.player.update_ball_image()

        self.settings.update_full_damage()


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
            elif event.type == pygame.USEREVENT+1:
                self.points.add(Point(self))
            elif event.type == pygame.USEREVENT+2:
                self.enemy.create_new_position()


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
        self.points.draw(self.screen)
        self.enemy.blit_me()
        self.life_bar.draw_bars()
        pygame.display.flip()
 
if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = TouhouGame()
    ai.run_game()