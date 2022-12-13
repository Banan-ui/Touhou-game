import pygame.font

class Scoreboard():
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.game_stats

        self.level_color = (30, 30, 30)
        self.text_color = (200, 200, 200)
        self.level_font = pygame.font.SysFont(None, 20)
        self.score_font = pygame.font.SysFont(None, 28)
        self.live_star_image = pygame.image.load("images/live_star.png")
        self.live_star_rect = self.live_star_image.get_rect()

        self.prep_score()
        self.score_rect = self.score_image.get_rect()
        self.score_rect.topleft = [12, 36]

        self.prep_high_score()
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.topright = [self.screen_rect.width-12, 36]

        self.prep_level()
        self.prep_damage()


    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        score = f"Score: {self.stats.score:06}"
        self.score_image = self.score_font.render(score, True, self.text_color)
        self.check_high_score()

    def prep_level(self):
        level = f"level: {self.settings.level}"
        self.level_image = self.level_font.render(level, True, self.level_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.midtop = [self.screen_rect.width/2, 12]

    def prep_high_score(self):
        """Преобразует текущий счет в графическое изображение."""
        highscore = f"Highscore: {self.stats.high_score:06}"
        self.high_score_image = self.score_font.render(highscore, True, self.text_color)

    def prep_damage(self):
        if self.settings.variable_damage == self.settings.max_variable_damage:
            damage = "DMG:MAX"
        else:
            damage = f"DMG: {self.settings.variable_damage:02}"
        self.damage_image = self.score_font.render(damage, True, self.text_color)
        self.damage_rect = self.damage_image.get_rect()
        self.damage_rect.topright = [self.screen_rect.width-12, 60]


    def check_high_score(self):
        """Проверяет, появился ли новый рекорд."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.damage_image, self.damage_rect)
        for live in range(0, self.settings.player_lives):
            self.screen.blit(self.live_star_image,
                [12+self.live_star_rect.width*live, 60])




