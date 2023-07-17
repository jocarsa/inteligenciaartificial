import pyautogui
import time

contador = 1
for i in range(0,100):
    pyautogui.moveTo(960, 540)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite("cara"+str(i)+".jpg")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(1)

