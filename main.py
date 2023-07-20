import pyautogui as pyauto
from time import *

sleep(2)
start_game_button = pyauto.locateOnScreen('Photos/start_game_button.png')
pyauto.click(start_game_button)
