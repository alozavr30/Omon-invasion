class Settings():
	"""Класс для хранения всех настроек игры Omon Invasion."""
	def __init__(self):
		"""Инициализирует настройки игры."""

		# Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		
		# Параметры пули.
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# Настройки омона.
		self.omon_speed_factor = 1
		self.formation_drop_speed = 10
		# formation_direction = 1 обозначает движение вправо; а -1 - влево.
		self.formation_direction = 1

		# Настройки навального.
		self.navalny_speed_factor = 1.5
		self.navalny_limit = 3