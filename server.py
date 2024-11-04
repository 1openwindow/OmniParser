from flask import Flask, request, jsonify
from utils import check_ocr_box
import base64
from PIL import Image
import io

app = Flask(__name__)

@app.route('/check_ocr_box', methods=['POST'])
def check_ocr_box_api():
    data = request.get_json()
    image_data = base64.b64decode(data['image'])
    image = Image.open(io.BytesIO(image_data))
    image_path = 'temp_image.png'
    image.save(image_path)

    ocr_bbox_rslt, is_goal_filtered = check_ocr_box(
        image_path, 
        display_img=False, 
        output_bb_format='xyxy', 
        goal_filtering=None, 
        easyocr_args={'paragraph': False, 'text_threshold': 0.9}
    )
    text, ocr_bbox = ocr_bbox_rslt
    return jsonify({'text': text, 'ocr_bbox': ocr_bbox, 'is_goal_filtered': is_goal_filtered})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
