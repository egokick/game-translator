In-Game Translator
Overview
In-Game Translator is a Python tool designed to help gamers translate Spanish text within their games seamlessly. By capturing screenshots of a specific screen area, sending them to OpenAI's GPT-4 Vision for translation, and displaying the results in a clean overlay, this tool enhances your gaming experience without interrupting gameplay.

Features
Global Hotkey Detection: Press Enter at any time to trigger a translation.
Quadrant-Based Screenshot: Automatically captures the Bottom Left quadrant of your screen.
Real-Time Translation: Utilizes OpenAI's GPT-4 Vision to translate Spanish text to English.
Overlay Display: Shows translations in a borderless, semi-transparent window for easy reading.
Cancellation of Previous Requests: New hotkey presses cancel ongoing translations and start fresh ones.
Quit Functionality: Press Ctrl+Shift+Q to exit the translator gracefully.
Requirements
Python 3.6 or higher
Libraries:
openai
pyautogui
keyboard
tkinter (usually included with Python)
Installation
Clone the Repository

bash
Copy
git clone https://github.com/yourusername/game-translator.git
cd game-translator
Install Dependencies

Open Command Prompt as Administrator and run:

bash
Copy
pip install openai pyautogui keyboard
Configure API Key

Open game-translator.py in a text editor.

Replace "sk-..." with your actual OpenAI API key:

python
Copy
client = OpenAI(api_key="sk-...")  # Replace with your actual API key
Usage
Run the Script as Administrator

Right-click on Command Prompt and select Run as administrator.

Navigate to the script directory:

bash
Copy
cd C:\source\game-translator
Execute the script:

bash
Copy
python game-translator.py
Using the Translator

Trigger Translation: Press Enter while in your game to capture and translate the Bottom Left screen area.
Quit Translator: Press Ctrl+Shift+Q to exit the application.
Troubleshooting
Overlay Not Visible

Ensure the script is running with Administrator privileges.
Verify that the Bottom Left quadrant contains the text you want to translate.
Check the terminal for any error logs.
Hotkey Not Working

Make sure the script is running as Administrator.
Ensure no other application is intercepting the Enter key.
Translation Issues

Confirm that your OpenAI API key is correct and has the necessary permissions.
Check your internet connection.
Review the terminal logs for any API-related errors.
Customization
Change Capture Quadrant

To capture a different quadrant (e.g., Top Left, Top Right, Bottom Right), modify the capture_quadrant_name variable in the script:

python
Copy
capture_quadrant_name = "bottom_left"  # Options: 'top_left', 'top_right', 'bottom_right'
Adjust Overlay Size and Position

Modify the overlay_width, overlay_height, x_pos, and y_pos variables to change the size and position of the translation window.