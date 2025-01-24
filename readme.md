# In-Game Translator

1. Edit the script to add your openai api key
2. Run the program 'python game-translator.py'
3. Press enter to trigger the translation
   
[![Watch the demo](https://private-user-images.githubusercontent.com/580550/406599818-723fc594-15ce-407d-9d62-3c3e7241f7dc.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzc3NTU5NDksIm5iZiI6MTczNzc1NTY0OSwicGF0aCI6Ii81ODA1NTAvNDA2NTk5ODE4LTcyM2ZjNTk0LTE1Y2UtNDA3ZC05ZDYyLTNjM2U3MjQxZjdkYy5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEyNFQyMTU0MDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kYzRmOTNmZTg2MmQzMmRmMGVhNmQxZDI3MjAxZjNmNmRiN2RiN2YwMzk1MTM5ZWM1MzlmMDYxYjljNmJlNzVlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Llcz3vV1Oeex8EueU_rfKaB3pl1t5oMJXyol6xe-WdQ)](https://private-user-images.githubusercontent.com/580550/406599818-723fc594-15ce-407d-9d62-3c3e7241f7dc.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzc3NTU5NDksIm5iZiI6MTczNzc1NTY0OSwicGF0aCI6Ii81ODA1NTAvNDA2NTk5ODE4LTcyM2ZjNTk0LTE1Y2UtNDA3ZC05ZDYyLTNjM2U3MjQxZjdkYy5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEyNFQyMTU0MDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kYzRmOTNmZTg2MmQzMmRmMGVhNmQxZDI3MjAxZjNmNmRiN2RiN2YwMzk1MTM5ZWM1MzlmMDYxYjljNmJlNzVlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Llcz3vV1Oeex8EueU_rfKaB3pl1t5oMJXyol6xe-WdQ)
## Overview

**In-Game Translator** is a Python tool designed to help gamers translate Spanish text within their games seamlessly. By capturing screenshots of a specific screen area, sending them to OpenAI's GPT-4 Vision for translation, and displaying the results in a clean overlay, this tool enhances your gaming experience without interrupting gameplay.

## Features

- **Global Hotkey Detection**: Press **Enter** at any time to trigger a translation.
- **Quadrant-Based Screenshot**: Automatically captures the **Bottom Left** quadrant of your screen.
- **Real-Time Translation**: Utilizes OpenAI's GPT-4 Vision to translate Spanish text to English.
- **Overlay Display**: Shows translations in a borderless, semi-transparent window for easy reading.
- **Cancellation of Previous Requests**: New hotkey presses cancel ongoing translations and start fresh ones.
- **Quit Functionality**: Press **Ctrl+Shift+Q** to exit the translator gracefully.

## Requirements

- Python 3.6 or higher
- Libraries:
  - `openai`
  - `pyautogui`
  - `keyboard`
  - `tkinter` (usually included with Python)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/egokick/game-translator.git
   cd game-translator
