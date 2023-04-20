import pyautogui
import keyboard

while True:
    if keyboard.is_pressed('enter'):
        pyautogui.hotkey('alt', 'f4')
