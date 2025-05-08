from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from PIL import Image
import tempfile
from steganography_functions import encode_lsb, decode_lsb
import base64
from io import BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        message = request.form.get('message', '')
        key = request.form.get('key', '')
        
        if not file or not message or not key:
            return jsonify({'error': 'Missing required fields'}), 400
        
        if file and allowed_file(file.filename):
            # Read the image
            img = Image.open(file.stream)
            
            # Convert to PNG if needed
            if file.filename.lower().endswith(('.jpg', '.jpeg')):
                temp = BytesIO()
                img.save(temp, format='PNG')
                img = Image.open(temp)
            
            # Encode the message
            try:
                encoded_img = encode_lsb(img, message)
                
                # Save to BytesIO
                output = BytesIO()
                encoded_img.save(output, format='PNG')
                output.seek(0)
                
                # Convert to base64 for preview
                encoded_string = base64.b64encode(output.getvalue()).decode()
                
                return jsonify({
                    'success': True,
                    'preview': f'data:image/png;base64,{encoded_string}'
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        
        return jsonify({'error': 'Invalid file type'}), 400
    
    return render_template('encode.html')

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        key = request.form.get('key', '')
        
        if not file or not key:
            return jsonify({'error': 'Missing required fields'}), 400
        
        if file and allowed_file(file.filename):
            # Read the image
            img = Image.open(file.stream)
            
            # Convert to PNG if needed
            if file.filename.lower().endswith(('.jpg', '.jpeg')):
                temp = BytesIO()
                img.save(temp, format='PNG')
                img = Image.open(temp)
            
            # Decode the message
            try:
                decoded_message = decode_lsb(img)
                if not decoded_message:
                    return jsonify({'error': 'No hidden message found'}), 400
                
                return jsonify({
                    'success': True,
                    'message': decoded_message
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        
        return jsonify({'error': 'Invalid file type'}), 400
    
    return render_template('decode.html')

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        file = request.files['image']
        
        if not file:
            return jsonify({'error': 'Missing image file'}), 400
        
        if file and allowed_file(file.filename):
            # Read the image
            img = Image.open(file.stream)
            
            # Convert to PNG if needed
            if file.filename.lower().endswith(('.jpg', '.jpeg')):
                temp = BytesIO()
                img.save(temp, format='PNG')
                img = Image.open(temp)
            
            # Perform detection
            try:
                from steg_detector import SteganographyDetector
                from malware_detector import MalwareDetector
                
                steg_detector = SteganographyDetector()
                malware_detector = MalwareDetector()
                
                steg_results = steg_detector.detect_steganography(img)
                malware_results = malware_detector.detect_malware(img)
                
                return jsonify({
                    'success': True,
                    'steg_results': steg_results,
                    'malware_results': malware_results
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
        
        return jsonify({'error': 'Invalid file type'}), 400
    
    return render_template('detect.html')

if __name__ == '__main__':
    app.run(debug=True) 