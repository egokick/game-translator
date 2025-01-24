import time
import threading
import base64
import pyautogui
import tkinter as tk
import logging
import keyboard  # For global hotkeys

from openai import OpenAI

# -------------------------
# SETUP LOGGING
# -------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# -------------------------
# OPENAI CLIENT
# -------------------------
client = OpenAI(api_key="sk-???")

# Lock and ID to manage translation requests
translation_id_lock = threading.Lock()
current_translation_id = 0

def divide_screen_into_quadrants():
    """
    Divides the screen into four equally sized quadrants.
    Returns a dictionary with quadrant names as keys and their (x, y, width, height) as values.
    """
    screen_width, screen_height = pyautogui.size()
    half_width = screen_width // 2
    half_height = screen_height // 2

    quadrants = {
        "top_left": (0, 0, half_width, half_height),
        "top_right": (half_width, 0, half_width, half_height),
        "bottom_left": (0, half_height, half_width, half_height),
        "bottom_right": (half_width, half_height, half_width, half_height)
    }

    logger.debug(f"Screen divided into quadrants: {quadrants}")
    return quadrants

def capture_quadrant(quadrant_name, quadrants, file_path="screenshot.png"):
    """
    Captures a screenshot of the specified quadrant.
    :param quadrant_name: Name of the quadrant to capture (e.g., 'bottom_left')
    :param quadrants: Dictionary of quadrants with their regions
    :param file_path: Path to save the screenshot
    :return: Path to the saved screenshot or empty string on failure
    """
    if quadrant_name not in quadrants:
        logger.error(f"Quadrant '{quadrant_name}' is not defined.")
        return ""

    region = quadrants[quadrant_name]
    logger.debug(f"Capturing quadrant '{quadrant_name}' with region {region}")

    try:
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(file_path)
        logger.debug(f"Screenshot saved to {file_path}")
        return file_path
    except Exception as e:
        logger.exception(f"Failed to capture screenshot for quadrant '{quadrant_name}': {e}")
        return ""

def translate_image_with_gpt4_vision(image_path):
    """
    Sends the screenshot (as a base64 image) to GPT-4 with Vision for
    Spanish-to-English translation.
    Returns the translated text or an empty string on error.
    """
    logger.debug("Reading screenshot file to encode as base64...")
    try:
        with open(image_path, "rb") as f:
            image_data = f.read()
        b64_str = base64.b64encode(image_data).decode("utf-8")
        data_url = "data:image/png;base64," + b64_str
        logger.debug("Encoded image to base64 data URL.")
    except Exception as e:
        logger.exception(f"Failed to read or encode image: {e}")
        return ""

    logger.debug("Calling OpenAI GPT-4 Vision endpoint...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Replace with your actual vision model name
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Please translate any text in this image to English."
                                    "Please only respond with the translation, nothing else."
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": data_url},
                        },
                    ],
                }
            ],
        )
        logger.debug(f"request_id: {response._request_id}")
        logger.debug("OpenAI API call succeeded.")
        translation = response.choices[0].message.content.strip()
        logger.debug(f"Received translation: {translation}")
        return translation
    except Exception as e:
        logger.exception(f"Error calling OpenAI API: {e}")
        return ""

def show_translation(label_var, translation):
    """
    Updates the label with the translation, shows the window, and schedules it to hide.
    """
    if not translation:
        logger.debug("No text detected or empty translation.")
        label_var.set("[No Spanish text detected]")
    else:
        logger.debug(f"Setting translation text: {translation}")
        label_var.set(translation)

    # Make the window visible (alpha=0.7)
    logger.debug("Making overlay visible at 70% opacity.")
    root.attributes("-alpha", 0.7)
    root.lift()
    root.attributes("-topmost", True)
    root.update_idletasks()

    # Schedule hide_overlay after 10 seconds
    logger.debug("Scheduling hide_overlay in 10 seconds.")
    root.after(10_000, lambda: hide_overlay(root))

def hide_overlay(root):
    """
    Sets the overlay transparency to 0.0 (fully invisible).
    """
    logger.debug("Hiding overlay (alpha=0.0).")
    root.attributes("-alpha", 0.0)

def handle_translation(label_var, quadrants, capture_quadrant_name="bottom_left", translation_id=0):
    """
    Handles capturing and translating in a separate thread.
    """
    logger.debug("Handling translation in separate thread.")

    # Add a 100ms delay before capturing the screen
    logger.debug("Waiting for 100ms before capturing the screen...")
    time.sleep(0.1)  # 100 milliseconds

    # Capture screenshot
    img_path = capture_quadrant(capture_quadrant_name, quadrants, "screenshot.png")
    if not img_path:
        logger.error("Screenshot capture failed.")
        root.after(0, show_translation, label_var, "[Screenshot capture failed]")
        return

    # Translate
    translation = translate_image_with_gpt4_vision(img_path)

    # Check if this translation is still the latest
    with translation_id_lock:
        if translation_id != current_translation_id:
            logger.debug(f"Translation ID {translation_id} is outdated. Current ID is {current_translation_id}. Skipping display.")
            return

    # Schedule the update in the Tkinter main thread
    root.after(0, show_translation, label_var, translation)

def on_hotkey_press(label_var, quadrants, capture_quadrant_name="bottom_left"):
    """
    Function to be called when the Enter key is pressed globally.
    """
    logger.debug("Global Enter key detected.")

    # Increment the current_translation_id
    with translation_id_lock:
        global current_translation_id
        current_translation_id += 1
        translation_id = current_translation_id
        logger.debug(f"Assigned translation_id: {translation_id}")

    # Start a new thread to handle capture and translation
    threading.Thread(target=handle_translation, args=(label_var, quadrants, capture_quadrant_name, translation_id), daemon=True).start()

def on_quit_hotkey():
    """
    Function to be called when the quit hotkey is pressed (e.g., Ctrl+Shift+Q).
    """
    logger.debug("Quit hotkey detected. Exiting...")
    root.quit()

def keyboard_listener(label_var, quadrants, capture_quadrant_name="bottom_left"):
    """
    Sets up the global hotkey listener.
    """
    logger.debug("Starting keyboard listener thread. Press Enter to translate, Ctrl+Shift+Q to quit.")
    # Register the Enter key globally
    keyboard.add_hotkey('enter', on_hotkey_press, args=(label_var, quadrants, capture_quadrant_name))
    # Register a hotkey to quit, e.g., Ctrl+Shift+Q
    keyboard.add_hotkey('ctrl+shift+q', on_quit_hotkey)

    # Keep the listener running
    keyboard.wait()

def main():
    global root  # Make root accessible in handle_translation
    logger.debug("Starting main()...")
    root = tk.Tk()
    root.title("In-Game Translator")

    # Remove window decorations and keep it on top
    root.overrideredirect(True)  # Make the window borderless
    root.attributes("-topmost", True)

    # Start fully invisible until Enter is pressed
    root.attributes("-alpha", 0.0)

    # Get screen dimensions and define quadrants
    quadrants = divide_screen_into_quadrants()

    # Define which quadrant to capture
    capture_quadrant_name = "bottom_left"  # Change to 'top_left', 'top_right', or 'bottom_right' as needed

    # Define overlay window size (optional: adjust based on quadrant size)
    # Here, we set it to a fixed size. You might want to adjust it based on the quadrant size.
    overlay_width = 600
    overlay_height = 200

    # Position at bottom-right corner
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_pos = screen_width - overlay_width - 10
    y_pos = screen_height - overlay_height - 40

    root.geometry(f"{overlay_width}x{overlay_height}+{x_pos}+{y_pos}")

    label_text = tk.StringVar()
    label_text.set("Waiting for translation...")

    display_label = tk.Label(
        root,
        textvariable=label_text,
        fg="white",
        bg="black",
        wraplength=overlay_width - 20,
        font=("Arial", 14)
    )
    display_label.pack(expand=True, fill="both", padx=10, pady=10)

    # Start the keyboard listener in a separate thread
    listener_thread = threading.Thread(target=keyboard_listener, args=(label_text, quadrants, capture_quadrant_name), daemon=True)
    listener_thread.start()

    logger.debug("Tkinter mainloop starting.")
    root.mainloop()

if __name__ == "__main__":
    main()
