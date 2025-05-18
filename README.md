# 🔐 Brute Force GUI Automation Tool (Educational Use Only)

This is a Python-based tool that automates brute force login attempts on GUI-based applications using the `pyautogui` library. It simulates typing email and password combinations from text files and clicks on the login button using screen coordinates.

> ⚠️ **DISCLAIMER**  
> This tool is developed for **educational purposes only**. Use it **only on your own systems or with explicit permission**. Unauthorized use may be illegal and unethical.

---

## 📦 Features

- Automates GUI login using emails and passwords from `.txt` files
- Works on **Windows**, **Linux**, and **macOS**
- Uses screen coordinates to locate form fields
- Allows easy customization of input files and coordinates
- Perfect for ethical hacking training and login testing

---


## 🔧 Setup Instructions

### Step 1: Clone or Download This Repo

```bash
git clone https://github.com/Saurabhm2/brute-force-tool.git
cd brute-force-tool
pip install -r requirements.txt
```

### Step 2: Install Required Python Libraries

```bash
Make sure Python is installed. Then run:
pip install -r requirements.txt
```
This installs required packages like pyautogui.

### Step 3: Prepare Your Email and Password Lists
Create two files in the root directory:

emails.txt
```bash
user1@example.com
user2@example.com
```
password.txt
```bash
password123
admin@123
```
You can add as many combinations as needed.

### Step 4: Capture Screen Coordinates
Run the coordinate capture script:

```bash
python coordinates.py
```

Follow the on-screen instructions:

- Click the Email input field
- Click the Password input field
- Click the Login button

This will create a file called coords.json like this:
```bash
{
  "email": [1571, 471],
  "password": [1562, 529],
  "login": [1575, 637]
}
```

### Step 5: Run the Brute Force Attack Script
Now you're ready to run the attack:

```bash
python brute.py
```


The script will:

- Loop through each email and password pair
- Move the mouse to the correct fields using screen coordinates
- Type the email and password
- Click the login button
- Wait between each attempt

### 📌 Example Output

```bash
Trying user1@example.com : password123  
Trying user1@example.com : admin@123  
Trying user2@example.com : password123  
...
```


## 🛡️ Legal & Ethical Use
This tool is intended ONLY for:

- ✅ Educational cybersecurity training
- ✅ Local app or dummy login testing
- ✅ Ethical penetration testing (with permission)

❌ Never use on real systems, websites, or applications without permission. Doing so is illegal and unethical.

## 🙋‍♂️ Author
  Saurabh Mahamuni.
---
  GitHub: @Saurabhm2.

🌟 Contributions
- Pull requests and feedback are welcome.
- Feel free to fork and improve the tool!

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚨 Legal Notice

Unauthorized use of this tool against systems you don't own or have explicit permission to test is:
- Illegal under computer crime laws (CFAA, GDPR, etc.)
- A violation of GitHub's Terms of Service
- Unethical in cybersecurity practice

The author assumes no liability for misuse of this software.
