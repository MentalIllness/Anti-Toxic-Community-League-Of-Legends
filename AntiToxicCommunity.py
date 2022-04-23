import pyautogui
import keyboard
from pynput.keyboard import Key, Listener
from time import sleep

TriggerEventKeyBind = Key.delete
AllCommand = "/all"
MessageBeforeMute = "I'm using AntiToxicCommunity and it helps me to stay away from toxic people like you :)"
muteAllCommand = '/mute all'

def show(key):

    if key == TriggerEventKeyBind:
         keyboard.press_and_release('enter')
         sleep(0.01)
         pyautogui.typewrite(AllCommand + " " + MessageBeforeMute)
         keyboard.press_and_release('enter')
         sleep(0.01)
         keyboard.press_and_release('enter')
         sleep(0.01)
         pyautogui.typewrite(muteAllCommand)
         keyboard.press_and_release('enter')

with Listener(on_press = show) as listener:   
    listener.join()