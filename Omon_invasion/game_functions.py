import sys
from time import sleep
import pygame
from bullet import Bullet
from omon import Omon

def navalny_hit(ai_settings, stats, screen, navalny, omons, bullets):
	"""Обрабатывает столкновение корабля с пришельцем"""
	# Уменьшение navalny_left.
	if stats.navalnys_left > 0:
		stats.navalnys_left -= 1
		# Очистка списков омона и пуль.
		omons.empty()
		bullets.empty()
		# Создание нового строя и размещение навального в центре.
		create_formation(ai_settings, screen, navalny, omons)
		navalny.center_navalny()
		# Пауза.
		sleep(0.5)
	else:
		stats.game_active = False

def check_keydown_events(event, ai_settings, screen, navalny, bullets):
	"""Реагирует на нажатие клавиш."""
	if event.key == pygame.K_RIGHT:
		navalny.moving_right = True
	elif event.key == pygame.K_LEFT:
		navalny.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, navalny, bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_keyup_events(event, navalny):
	"""Реагирует на отпускание клавиш."""
	if event.key == pygame.K_RIGHT:
		navalny.moving_right = False
	elif event.key == pygame.K_LEFT:
		navalny.moving_left = False

def check_events(ai_settings, screen, navalny, bullets):
	"""Обрабатывает нажатия клавиш и мыши"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, navalny, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, navalny)
			
def update_screen(ai_settings, screen, navalny, omons, bullets):
	# При каждом проходе цикла перерисовывается экран.
	screen.fill(ai_settings.bg_color)
	# Все пули выводятся позади навального и противников
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	navalny.blitme()
	omons.draw(screen)
	# Отображение последнего прорисованного экрана.
	pygame.display.flip()

def update_bullets(ai_settings, screen, navalny, omons, bullets):
	"""Обновляет позиции пуль и убирает старые пули."""
	# Обновление позиции пуль.
	bullets.update()
	# Удаление пуль, вышедших за край экрана.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_omon_collisions(ai_settings, screen, navalny, omons, bullets)
	
def check_bullet_omon_collisions(ai_settings, screen, navalny, omons, bullets):
	"""Обработка коллизий пуль с омоном."""
	# Удаление пуль и омона, учавствующих в коллизиях.
	collisions = pygame.sprite.groupcollide(bullets, omons, True, True)
	if len(omons) == 0:
		# Уничтожение существующих пуль и создание нового флота.
		bullets.empty()
		create_formation(ai_settings, screen, navalny, omons)

def fire_bullet(ai_settings, screen, navalny, bullets):
	"""Выпускает пулю, если максимум еще не достигнут."""
	# Создание новой пули и включение ее в группу bullets.
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, navalny)
		bullets.add(new_bullet)

def create_formation(ai_settings, screen, navalny, omons):
	"""Создает флот пришельцев"""
	# Создание пришельца и вычисление кол-ва пришельцев в ряду. 
	omon = Omon(ai_settings, screen)
	number_omons_x = get_number_omons_x(ai_settings, omon.rect.width)
	number_rows = get_number_rows(ai_settings, navalny.rect.height, omon.rect.height)
	# Создание флота омоновцев.
	for row_number in range(number_rows): 
		# Создание первого ряда омоновцев.
		for omon_number in range(number_omons_x):
			# Создание омоновца и размещение его в ряду.
			create_omons(ai_settings, screen, omons, omon_number, row_number)

def get_number_omons_x(ai_settings, omon_width):
	"""Вычисляет количество пришельцев в ряду"""
	available_spase_x = ai_settings.screen_width - 2 * omon_width
	number_omons_x = int(available_spase_x / (2 * omon_width))
	return number_omons_x

def create_omons(ai_settings, screen, omons, omon_number, row_number):
	"""Создает пришельца и размещает его в ряду"""
	omon = Omon(ai_settings, screen)
	omon_width = omon.rect.width
	omon.x = omon_width + 2 * omon_width * omon_number
	omon.rect.x = omon.x
	omon.rect.y = omon.rect.height + 2 * omon.rect.height * row_number
	omons.add(omon)

def get_number_rows(ai_settings, navalny_height, omon_height):
	"""Определяет кол-во рядов, помещяющихся на экране."""
	available_spase_y = (ai_settings.screen_height - (3 * omon_height) - navalny_height)
	number_rows = int(available_spase_y / (2 * omon_height))
	return number_rows

def check_formation_edges(ai_settings, omons):
	"""Реагирует на достижение омоном края экрана"""
	for omon in omons.sprites():
		if omon.check_edges():
			change_formation_direction(ai_settings, omons)
			break

def change_formation_direction(ai_settings, omons):
	"""Опускает весь строй и меняет направление"""
	for omon in omons.sprites():
		omon.rect.y += ai_settings.formation_drop_speed
	ai_settings.formation_direction *= -1

def check_omons_bottom(ai_settings, stats, screen, navalny, omons, bullets):
	"""Проверяет, добрались ли омоновцы до нижнего края экрана."""
	screen_rect = screen.get_rect()
	for omon in omons.sprites():
		if omon.rect.bottom >= screen_rect.bottom:
			# Происходит то же, что при столкновении с кораблем.
			navalny_hit(ai_settings, stats, screen, navalny, omons, bullets)
			break

def update_omons(ai_settings, stats, screen, navalny, omons, bullets):
	"""
	Проверяет, достиг ли строй края экрана, 
	после чего обновляет позиции всех омоновцев в строю.
	"""
	check_formation_edges(ai_settings, omons)
	omons.update()
	# Проверка коллизий "омон-навальный"
	if pygame.sprite.spritecollideany(navalny, omons):
		navalny_hit(ai_settings, stats, screen, navalny, omons, bullets)
	check_omons_bottom(ai_settings, stats, screen, navalny, omons, bullets)

