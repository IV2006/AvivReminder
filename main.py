import pyautogui
import pyperclip
from PIL import Image
from io import BytesIO
import win32clipboard
import time
from datetime import datetime
from pytz import timezone


def copy_image(filepath: str):
    image = Image.open(filepath)
    time.sleep(1)
    output = BytesIO()
    time.sleep(1)
    image.convert("RGB").save(output, "BMP")
    time.sleep(1)
    data = output.getvalue()[14:]
    time.sleep(1)
    output.close()
    time.sleep(1)

    win32clipboard.OpenClipboard()
    time.sleep(1)
    win32clipboard.EmptyClipboard()
    time.sleep(1)
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    time.sleep(1)
    win32clipboard.CloseClipboard()


if __name__ == "__main__":
    WHATSAPP_SEARCH_BAR = 150, 180
    WHATSAPP_CONTACT_ICON = 150, 275
    WHATSAPP_MESSAGE_BAR = 1750, 970
    pyperclip.py2 = True
    ICONS_BOX = (0, 1010, 1919, 69)

    while True:
        curr_time = datetime.now(timezone('Asia/Jerusalem'))
        time.sleep(1)
        if curr_time.hour == 13 and curr_time.minute == 0:
            x, y, *_ = pyautogui.locateOnScreen("WHATSAPP_ICON.png", grayscale=True, region=ICONS_BOX, confidence=0.5)
            time.sleep(1)
            pyautogui.leftClick(x, y)
            time.sleep(1)
            pyautogui.leftClick(WHATSAPP_SEARCH_BAR)
            time.sleep(1)
            pyperclip.copy("Aviv")
            time.sleep(1)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(1)
            pyautogui.leftClick(WHATSAPP_CONTACT_ICON)
            time.sleep(1)
            copy_image("reminder.jpg")
            time.sleep(1)
            pyautogui.leftClick(WHATSAPP_MESSAGE_BAR)
            time.sleep(1)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(1)
            pyperclip.copy("ביפ בופ אני בוט")
            time.sleep(1)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(1)
            pyautogui.hotkey("enter")
            time.sleep(60)  # I can add a flag, or I can sleep for a minute, both work, one is simpler
