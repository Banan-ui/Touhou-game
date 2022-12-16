import pygame

class Sound():
    """Класс для воспроизведения звуков и музыки игры"""
    def __init__(self):
        self.damage_sound = pygame.mixer.Sound('sounds/damage.wav')
        self.item_sound = pygame.mixer.Sound('sounds/item.wav')
        self.ok_sound = pygame.mixer.Sound('sounds/ok.wav')
        self.pldead_sound = pygame.mixer.Sound('sounds/pldead.wav')
        self.fire_sound = pygame.mixer.Sound('sounds/fire.wav')
        self.kill_sound = pygame.mixer.Sound('sounds/kill.wav')

        pygame.mixer.music.load(
            "sounds/Marisa Kirisame's Theme - Love-colored Master Spark.mp3")

    def damage_play(self):
        self.damage_sound.play()
        self.damage_sound.set_volume(0.2)

    def ok_play(self):
        self.ok_sound.play()
        self.ok_sound.set_volume(0.2)

    def item_play(self):
        self.item_sound.play()
        self.item_sound.set_volume(0.2)

    def pldead_play(self):
        self.pldead_sound.play()
        self.pldead_sound.set_volume(0.2)

    def fire_play(self):
        self.fire_sound.play()
        self.fire_sound.set_volume(0.2)

    def kill_play(self):
        self.kill_sound.play()
        self.kill_sound.set_volume(0.2)

    def play_music(self):
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.8)

    def stop_music(self):
        pygame.mixer.music.stop()



