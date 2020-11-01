import pygame
from pygame.sprite import Sprite

class Omon(Sprite):
	"""Класс, представляющий одного омоновца."""
	def __init__(self, ai_settings, screen):
		"""Инициализирует омоновца и задает его начальную позицию."""
		super(Omon, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Загрузка изображения омона и назначение атрибута rect.
		self.image = pygame.image.load('images/omon.bmp')
		self.rect = self.image.get_rect()

		# Каждый новый омоновец появляется в левом верхнем углу экрана.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Сохранение точной позиции омоновца.
		self.x = float(self.rect.x)
	def blitme(self):
		"""Выводит омон в текущем положении."""
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		"""Возвращает True, если омон находится у края экрана."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
		"""Перемещает омон вправо или влео"""
		self.x += (self.ai_settings.omon_speed_factor * 
					self.ai_settings.formation_direction)
		self.rect.x = self.x