class Game_stats():

    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.highscore = 0
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1
