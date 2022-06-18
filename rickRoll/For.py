#Originally made by Github user eccleses
#requires the pyautogui library to be downloaded (pip install PyAutoGUI)
import pyautogui
import time

def Linux():
    pyautogui.hotkey('ctrl','alt','t')
    time.sleep(1)
    pyautogui.typewrite('xdg-open https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    pyautogui.hotkey('enter')

def Windows():
    pyautogui.hotkey('win','x')
    pyautogui.typewrite('a')
    time.sleep(1)
    pyautogui.typewrite('start chrome https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    pyautogui.hotkey('enter')

