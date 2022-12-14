import json

class GameStats():
    """Отслеживание статистики игры"""

    def __init__(self, ai_game):
        """Инициаолизация статистики"""
        self.settings = ai_game.settings

        self.filename = "high_score.json"
        with open(self.filename) as f: #Открытие файла json для чтения
            self.high_score = int(json.load(f)) #Чтение из файла

        self.score = 900

        self.game_active = True