import json

class GameStats():
    """Отслеживание статистики игры"""

    def __init__(self, ai_game):
        """Инициаолизация статистики"""
        self.settings = ai_game.settings

        self.filename = "high_score.json"
        with open(self.filename) as f: #Открытие файла json для чтения
            self.high_score = int(json.load(f)) #Чтение из файла

        self.score = 0

        self.game_active = True

    def reset_stats(self):
        self.score = 0

    def save_high_score(self):
        with open(self.filename, "w") as f: #Открытие файла json для записи
            json.dump(self.high_score, f) #Запись списка в файл
