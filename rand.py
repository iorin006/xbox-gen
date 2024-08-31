import random
import string
import pyperclip
import keyboard
import time
def randomname(n):
    randlst = [
        random.choice(string.ascii_letters + string.digits) for i in range(n)
    ]
    return "".join(randlst)

w = randomname(10)
p = randomname(10)
pyperclip.copy(f"a{w}@outlook.jp")
while True:
    if keyboard.is_pressed('ctrl + v'):
        time.sleep(0.1)
        pyperclip.copy(p)
        break