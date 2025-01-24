# In-Game Translator

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
