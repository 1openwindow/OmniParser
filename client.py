import requests
import base64
from PIL import ImageGrab
import io
import pygetwindow as gw

# Get the active window
active_window = gw.getActiveWindow()

# Capture the screenshot of the active window
screenshot = ImageGrab.grab(bbox=active_window.box)
buffered = io.BytesIO()
screenshot.save(buffered, format="PNG")

# Open the screenshot
screenshot.show()

# Encode the screenshot to base64
img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

url = 'https://ngrok.endpoint/check_ocr_box'
data = {
    'image': img_str
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Failed:', response.status_code, response.text)
