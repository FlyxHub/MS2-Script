import autoit
import keyboard

while True:
    if keyboard.is_pressed('CTRL'):
        autoit.mouse_down('left')