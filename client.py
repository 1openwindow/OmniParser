import requests
import base64
from PIL import ImageGrab
import io

# Capture the screenshot
screenshot = ImageGrab.grab()
buffered = io.BytesIO()
screenshot.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

url = 'http://localhost:5000/check_ocr_box'
data = {
    'image': img_str
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Failed:', response.status_code, response.text)