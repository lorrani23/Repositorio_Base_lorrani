import pyautogui as aut
import flet as ft

# aut.mouseInfo()
aut.press('win')
aut.write('gmail')
aut.press('enter')
aut.sleep(2)
aut.moveTo(264,372)
aut.click()
aut.sleep(2)
aut.moveTo(24,164)
aut.click()
aut.sleep(2)
aut.write('ricardo.rlima@sp.senai.br')
aut.press('tab')
aut.press('tab')
aut.write('ola')
aut.press('tab')
aut.press('enter')

