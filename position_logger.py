import pyautogui
import time
import win32api

toggle = False
start_time = time.time()

while True:
    if win32api.GetKeyState(0x01) == 0 and not toggle:
        mouse_pos = pyautogui.position()
        final_time = time.time() - start_time
        print(final_time, mouse_pos)
        start_time = time.time()
        toggle = True
    if win32api.GetKeyState(0x01) == 1 and toggle:
        mouse_pos = pyautogui.position()
        final_time = time.time() - start_time
        print(final_time, mouse_pos)
        start_time = time.time()
        toggle = False
