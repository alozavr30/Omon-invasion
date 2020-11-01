import pygame

class Navalny():

	def __init__(self, ai_settings, screen):
		"""Инициализирует Навального и задает его начальную позицию."""
		self.screen = screen
		self.ai_settings = ai_settings

		# Загрузка изображения Навального и получение прямоугольника.
		self.image = pygame.image.load('images/navalny.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Каждый новый Навальный появляется у нижнего края экрана.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		# Сохранение вещественной координаты центра Навального.
		self.center = float(self.rect.centerx)
		# Флаги перемещения.
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Обновляет позицию Навального с учетом флагов."""
		# Обновляется атрибут center, не rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.navalny_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.navalny_speed_factor
		# Обновление атрибута rect на основании self.center.
		self.rect.centerx = self.center

	def blitme(self):
		"""Рисует Навального в текущей позиции."""
		self.screen.blit(self.image, self.rect)

	def center_navalny(self):
		"""Размещает корабль в центре нижней стороны."""
		self.center = self.screen_rect.centerx