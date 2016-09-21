import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_DIR = 'upload'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'mp4'])

app = Flask(__name__)
app.config['UPLOAD_DIR'] = UPLOAD_DIR

app.secret_key = 'super-secret-key'

def allowed_file(filename):
    return '.' in filename and (filename.rsplit('.', 1)[1]).lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'video_file' not in request.files:
            flash('No video_file part')
            return redirect(request.url)
        if 'image_files' not in request.files:
            flash('No image_files part')
            return redirect(request.url)

        file = request.files.getlist("video_file")[0]
        print (file)
        flash('File loaded: {0}'.format(file.filename))
        filename = secure_filename(file.filename)
        vid_filename = filename
        vid_path = os.path.join(app.root_path, os.path.join(app.config['UPLOAD_DIR'], filename))
        file.save(vid_path)

        files = request.files.getlist("image_files")
        images_paths = []
        print (files)
        for file in files:
            if file.filename == '':
                flash('Missing file')
            if file and allowed_file(file.filename):
                flash('File loaded: {0}'.format(file.filename))
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.root_path, os.path.join(app.config['UPLOAD_DIR'], filename)))
                images_paths.append("/uploads/{}".format(filename))
        return render_template('index.html', uploaded = True, vid_path = "/uploads/{}".format(vid_filename), images_paths = images_paths)
    return render_template('index.html', uploaded = False)

'''

'''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_DIR'], filename)



