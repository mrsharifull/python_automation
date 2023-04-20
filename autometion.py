import pyautogui
import time

pyautogui.press('win')
pyautogui.typewrite('Skype')
pyautogui.press('enter')
time.sleep(5)
if pyautogui.locateOnScreen('D:\Works\Auto File Open Python\python_automation\sback_arrow.png'):
    button_location = pyautogui.locateOnScreen('D:\Works\Auto File Open Python\python_automation\sback_arrow.png')
    button_center = pyautogui.center(button_location)
    time.sleep(2)
    pyautogui.click(button_center)
    time.sleep(2)

button_location = pyautogui.locateOnScreen('D:\Works\Auto File Open Python\python_automation\me.png')
button_center = pyautogui.center(button_location)
time.sleep(2)
pyautogui.click(button_center)
time.sleep(2)
if pyautogui.locateOnScreen('D:\Works\Auto File Open Python\python_automation\dot_menu.png'):
    button_location = pyautogui.locateOnScreen('D:\Works\Auto File Open Python\python_automation\dot_menu.png')
    button_center = pyautogui.center(button_location)
    time.sleep(2)
    pyautogui.click(button_center)
    time.sleep(2)
    pyautogui.press('tab',presses=2)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
else:
    button_location = pyautogui.locateOnScreen('D:\Works\Auto File Open Python\python_automation\image_menu.png')
    button_center = pyautogui.center(button_location)
    time.sleep(2)
    pyautogui.click(button_center)
    time.sleep(2)
    button_location = pyautogui.locateOnScreen('D:\Works\Auto File Open Python\python_automation\sall.png')
    button_center = pyautogui.center(button_location)
    time.sleep(2)
    pyautogui.click(button_center)

time.sleep(2)
pyautogui.press('down',presses=2)
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
button_location = pyautogui.locateOnScreen('D:\Works\Auto File Open Python\python_automation\image.png')
button_center = pyautogui.center(button_location)
time.sleep(2)
pyautogui.click(button_center)
time.sleep(2)
pyautogui.rightClick()
time.sleep(1)
pyautogui.press('down',)
time.sleep(1)
pyautogui.press('enter')




