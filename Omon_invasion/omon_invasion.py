import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from navalny import Navalny
from omon import Omon
import game_functions as gf

def run_game():
	# Инициализирует игру, settings и создает обьект экрана.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, 
	ai_settings.screen_height))
	pygame.display.set_caption("Omon Invasion")
        
        #Создание кнопки play. 
        play_button = Button(ai_settings, screen, "play") 

	# Создание экземпляра для хранения игровой статистики.
	stats = GameStats(ai_settings)
	# Создание Навального.
	navalny = Navalny(ai_settings, screen)
	# Создание омоновца и их группы.
	omons = Group()
	gf.create_formation(ai_settings, screen, navalny, omons)
	# Создание группы для хранения пуль.
	bullets = Group()

	# Назначение цвета фона.
	bg_color = (230, 230, 230)

	# Запуск основного цикла игры.
	while True:
		# Отслеживание событий клавиатуры и мыши.
		gf.check_events(ai_settings, screen, navalny, bullets)
		navalny.update()
		gf.update_bullets(ai_settings, screen, navalny, omons, bullets)
		gf.update_omons(ai_settings, stats, screen, navalny, omons, bullets)
		gf.update_screen(ai_settings, screen, navalny, omons, bullets, 
                                 play_button)

run_game()
