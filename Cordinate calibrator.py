import pyautogui
import time
import keyboard  # Import keyboard library

print("Move your mouse to the position. Press ESC to exit.")

try:
    while True:
        
        x, y = pyautogui.position()
        print(f"Mouse position: ({x}, {y})", end="\r")  
        

        # Check if ESC key is pressed
        if keyboard.is_pressed('esc'):
            print("\n Exiting...")
            break  # Exit the loop if ESC is pressed

except KeyboardInterrupt:
    print("\nDone!")
