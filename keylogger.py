import sys
import time

# Function to record keys from terminal input
def record_keys():
   
    
    print("Keylogger started. Type your keys (Press 'Enter' to stop recording):")
    
    # An empty list to store the keys that will be pressed
    keys = []  

    while True:
        # sys.stdin.read(1) will wait for the user to press a key and read it
        key = sys.stdin.read(1)
        
        # If the Enter key ('\n') is pressed, we stop the recording
        if key == '\n':  
            break

        # Append each pressed key to the 'keys' list
        keys.append(key)

        # For feedback, show the user which key was pressed
        print(f"Key pressed: {key}")

    # Once the loop is done (Enter pressed), return the list of collected keys
    return keys


# Function to save the recorded keys into a text file
def save_keys(keys):
    """
    This function writes the list of keys captured during typing into a file.
    It takes care of formatting special keys like spaces and Enter.
    """
    # Open a file called 'log.txt' in append mode, so we don't overwrite existing data
    with open("log.txt", "a") as file:
        # Go through each key in the list
        for key in keys:
            # If the key is a space, log it as [SPACE] for clarity in the file
            if key == ' ':
                file.write("[SPACE]")
            # If the key is Enter (which we stop recording with), write a newline in the file
            elif key == '\n':
                file.write("\n")
            # Otherwise, just write the key itself
            else:
                file.write(key)

    print("Keys have been saved to log.txt.")


# Main function to coordinate keylogging and saving
def main():
    """
    The main driver of the program. It starts the keylogging process, collects the typed keys, 
    and then saves them into a file.
    """
    # First, call the record_keys function to capture keyboard inputs
    keys = record_keys()  

    # Once we have the keys, we pass them to the save_keys function to store them in a file
    save_keys(keys)  


if __name__ == "__main__":
    # Start the keylogger
    main()
