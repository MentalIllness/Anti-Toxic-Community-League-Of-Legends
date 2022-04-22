import pyautogui
from pynput.keyboard import Key, Listener

TriggerEventKeyBind = Key.delete
muteAllCommand = '/mute all'

def show(key):

    if key == TriggerEventKeyBind:
         pyautogui.typewrite(muteAllCommand)
         pyautogui.press('enter')

# Collect all event until released
with Listener(on_press = show) as listener:   
    listener.join()