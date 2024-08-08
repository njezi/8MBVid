from flask import Flask, request, send_file, render_template, after_this_request, jsonify
import os
import subprocess
import random
import string

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'compressed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

def random_filename(length=8):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def delete_file(file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress_video():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        random_name = random_filename() + '.mp4'
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], random_name)
        
        # compressing the video
        subprocess.run(['ffmpeg', '-i', file_path, '-fs', '8M', output_path])

        @after_this_request
        def cleanup_files(response):
            delete_file(file_path) # deleting the uploaded file
            def remove_compressed_file():
                delete_file(output_path)
            import threading
            threading.Timer(300, remove_compressed_file).start()  # deleting the compressed file after 5 min
            return response

        return jsonify({'filename': random_name})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    
    if not os.path.exists(output_path):
        return 'File not found', 404
    
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    app.run(debug=True)
