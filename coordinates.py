import pyautogui
import time

print("Move your mouse to the desired positions...")
time.sleep(4)

print("Email field coordinates:")
time.sleep(5)
email_x, email_y = pyautogui.position()
print(f"Email: ({email_x}, {email_y})")

print("Password field coordinates:")
time.sleep(5)
pass_x, pass_y = pyautogui.position()
print(f"Password: ({pass_x}, {pass_y})")

print("Login button coordinates:")
time.sleep(5)
login_x, login_y = pyautogui.position()
print(f"Login Button: ({login_x}, {login_y})")