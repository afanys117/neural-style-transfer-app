# Neural Style Transfer App

The Neural Style Transfer App allows users to combine the style of one image with the content of another to create an artistic output. The app applies advanced deep learning techniques to generate stunning visuals by transferring the style of famous artworks or patterns to content images.

### Example
[Example Image](images/example1.png)

This web application utilizes PyTorch's VGG19 model for extracting content and style features, and combines them using neural style transfer. Users can upload their content and style images to generate an output image that blends both.

## Features
- User-friendly interface to upload content and style images.
- Generates stylized images with just one click.
- Built with Flask for the backend, and HTML/CSS/JavaScript for the frontend.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Model**: VGG19 for neural style transfer
- **Environment**: Python 3.10, pip for package management

## Installation

### Prerequisites
- Python 3.10 or higher
- pip (or conda)

### Clone the Repository
```bash
git clone https://github.com/afanys117/neural-style-transfer-app.git
cd neural-style-transfer-app
```

### Install Requirements
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the App
Ensure you are in the project directory.

Run the Flask app:
```bash
python app.py
```

Open your web browser and go to `http://127.0.0.1:5000`.

## Usage
1. Upload your **Content Image** and **Style Image**.
2. Click on the **Generate** button.
3. The generated stylized image will be displayed along with the uploaded images.
