import pyperclip
from time import sleep
import ctypes
user32 = ctypes.windll.user32
strs = ['0x0x0', 'x0x0x', '0x0x0', 'x0x0x', '0x0x0', 'x0x0x', '0x0x0', 'x0x0x', '0x0x0', 'x0x0x']
for i in strs:
    print(i)
    pyperclip.copy(i)
    if i is strs[0]:
        user32.keybd_event(0x12, 0, 0, 0) #Alt
        sleep(0.05)
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.05)
        user32.keybd_event(0x09, 0, 2, 0) #Tab
        sleep(0.05)
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.05)
        user32.keybd_event(0x09, 0, 2, 0) #Tab
        sleep(0.05)
        user32.keybd_event(0x12, 0, 2, 0) #Alt
        sleep(2)
    user32.keybd_event(0x11, 0, 0, 0) #ctrl
    sleep(0.05)
    user32.keybd_event(0x56, 0, 0, 0) #v
    sleep(0.05)
    user32.keybd_event(0x56, 0, 2, 0) #~v
    sleep(0.05)
    user32.keybd_event(0x11, 0, 2, 0) #~ctrl
    sleep(0.05)
    if i is not strs[-1]:
        user32.keybd_event(0x09, 0, 0, 0)
        sleep(0.05)
        user32.keybd_event(0x09, 0, 2, 0)
        sleep(0.05)

print("Happy Scheduling\n-PMARINA")
