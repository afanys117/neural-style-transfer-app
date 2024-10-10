from flask import Flask, render_template, request, jsonify, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
import torch
from model import run_style_transfer, image_loader
from torchvision import transforms  # Import transforms here

app = Flask(__name__)

# Configuration for upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'content' not in request.files or 'style' not in request.files:
        return jsonify({"error": "No file part"}), 400

    content_file = request.files['content']
    style_file = request.files['style']

    if (content_file and allowed_file(content_file.filename) and
        style_file and allowed_file(style_file.filename)):
        
        # Secure file names
        content_filename = secure_filename(content_file.filename)
        style_filename = secure_filename(style_file.filename)

        # Save the uploaded images to the upload folder
        content_path = os.path.join(app.config['UPLOAD_FOLDER'], content_filename)
        style_path = os.path.join(app.config['UPLOAD_FOLDER'], style_filename)
        content_file.save(content_path)
        style_file.save(style_path)

        # Load the images
        content_img = image_loader(content_path)
        style_img = image_loader(style_path)

        # Run the neural style transfer
        output_img = run_style_transfer(content_img, style_img)

        # Save the output image
        output_filename = 'output.png'
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        transforms.ToPILImage()(output_img.cpu().squeeze(0)).save(output_path)

        # Return image paths for display
        return jsonify({
            'content_url': url_for('uploaded_file', filename=content_filename),
            'style_url': url_for('uploaded_file', filename=style_filename),
            'output_url': url_for('uploaded_file', filename=output_filename)
        })
    else:
        return jsonify({"error": "Invalid file type"}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
