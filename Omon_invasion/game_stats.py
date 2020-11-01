class GameStats():
	"""Отслеживание статистики для игры Omon Invasion."""
	def __init__(self, ai_settings):
		"""Инициализирует статистику."""
		self.ai_settings = ai_settings
		self.reset_stats()
		# Игра запускатся в активном состоянии.
		self.game_active = True

	def reset_stats(self):
		"""Инициализирует статистику, изменяющуюся в ходе игры."""
		self.navalnys_left = self.ai_settings.navalny_limit