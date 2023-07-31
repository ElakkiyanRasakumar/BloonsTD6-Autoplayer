import pyautogui as pyauto
import time
import cv2 as cv


start_time = time.time()

time.sleep(1)

pyauto.press("win")
time.sleep(0.5)
for i in "Bloons TD 6":
    pyauto.press(i)
pyauto.press("enter")

start_game_button = False
open_map_selector_button = False
advanced_map_mode_button = False
another_brick_map_button = False
hard_mode_selector_button = False
standard_mode_button = False
overwrite_save = False


while True:
    #Start BloonsTD6
    if not start_game_button and pyauto.locateOnScreen('Photos/start_game_button.png', confidence=0.7) != None :
        pyauto.leftClick(pyauto.locateOnScreen('Photos/start_game_button.png', confidence=0.7))
        start_game_button = True

    #Open map selector
    if not open_map_selector_button and pyauto.locateOnScreen('Photos/open_map_selector_button.png', confidence=0.7) != None:
        pyauto.leftClick(pyauto.locateOnScreen('Photos/open_map_selector_button.png', confidence=0.7))
        open_map_selector_button = True

    #Select map difficulty
    if not advanced_map_mode_button and pyauto.locateOnScreen("Photos/advanced_map_mode_button.png", confidence=0.7) != None and pyauto.locateOnScreen("Photos/another_brick_map_button.png", confidence=0.7) is None:
        pyauto.leftClick(pyauto.locateOnScreen("Photos/advanced_map_mode_button.png", confidence=0.7))

    # Select "another brick" map if seen on screen
    elif not another_brick_map_button and pyauto.locateOnScreen("Photos/another_brick_map_button.png", confidence=0.7) != None:
        pyauto.leftClick(pyauto.locateOnScreen("Photos/another_brick_map_button.png", confidence=0.7))
        advanced_map_mode_button = True
        another_brick_map_button = True


    # Select hard mode
    if not hard_mode_selector_button and pyauto.locateOnScreen("Photos/hard_mode_selector_button.png", confidence=0.7) != None:
        pyauto.leftClick(pyauto.locateOnScreen("Photos/hard_mode_selector_button.png", confidence=0.7))
        hard_mode_selector_button = True

    #Select standard mode
    if not standard_mode_button and pyauto.locateOnScreen("Photos/standard_mode_button.png", confidence=0.7) != None:
        pyauto.leftClick(pyauto.locateOnScreen("Photos/standard_mode_button.png", confidence=0.7))
        standard_mode_button = True
        time.sleep(0.5)

    # Overwrite a save if a previous save exists
    if not overwrite_save and pyauto.locateOnScreen("Photos/overwrite_save.png", confidence=0.6) != None:
        pyauto.leftClick(pyauto.locateOnScreen("Photos/overwrite_save_ok_button.png", confidence=0.7))
        overwrite_save = True

    if overwrite_save or standard_mode_button:
        break


print(time.time() - start_time)
