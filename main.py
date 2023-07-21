import pyautogui as pyauto
import time
import cv2 as cv

# Sleep so I can switch to the game
time.sleep(3)



#Start BloonsTD6
start_game_button = pyauto.locateOnScreen('Photos/start_game_button.png', confidence=0.7)
pyauto.leftClick(start_game_button)

time.sleep(5)

#Open map selector
open_map_selector_button = pyauto.locateOnScreen('Photos/open_map_selector_button.png', confidence=0.7)
pyauto.leftClick(open_map_selector_button)
