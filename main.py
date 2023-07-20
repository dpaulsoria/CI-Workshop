import time
import keyboard

def on_key_press(event):
    print("Tecla presionada:", event.name)
    if event.name == "c":
        global flag
        flag = False

def run():
    c = 0
    global flag
    flag = True
    while flag:
        print(c)
        c += 1
        # Esperar un segundo
        time.sleep(1)

if __name__ == '__main__':
    keyboard.on_press(on_key_press)
    run()
