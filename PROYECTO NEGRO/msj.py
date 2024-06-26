import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+51950692976')

sleep(10)

for i in range(20):
    pyautogui.typewrite('CONCHATUMAWRE')
    pyautogui.press('enter')