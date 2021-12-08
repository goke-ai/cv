import os
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for
from PIL import Image
import io
import base64
import mimetypes
from flask import Flask, request, make_response, jsonify, render_template, redirect, url_for
import numpy as np
import cv2 as cv

# instance of Flask
app = Flask(__name__)


@app.errorhandler(500)
def not_found(e):
    # return also the code error
    return jsonify({"status": "internal error", "message": "internal error occurred in server"}), 500


@app.errorhandler(404)
def not_found(e):
    # return also the code error
    return jsonify({"status": "not found", "message": "route not found"}), 404


@app.errorhandler(400)
def bad_request(e):
    # return also the code error
    return jsonify({"status": "not ok", "message": "this server could not understand your request"}), 400


data = {'1': 'afiq',
        '2': 'azureen',
        '3': 'gavin',
        '4': 'cve',
        '5': 'inamul',
        '6': 'jincheng',
        '7': 'mahmuda',
        '8': 'numan',
        '9': 'saseendran'
        }


@app.route('/')
def index():
    page = 'index'
    description = """This is an api for computer vision class. The api gets you the students in class.
    Please enjoy and have some fun.
    The api routes are the following:
    1. get all: /api/cv
    2. get by id: /api/cv/5
    3. post: /api/cv
    4. put by id: /api/cv/5
    5. delete by id: /api/cv/5
    
    Thanks for check our api out
    """
    return render_template('index.html', page=page, description=description, data=data)


# get
# /api/cv


@app.route('/api/cv', methods=['GET'])
def get_all():
    return jsonify({"status": "ok", "students": data}), 200


# get_by_id
# /api/cv/1
@app.route('/api/cv/<int:id>', methods=['GET'])
def get_by_id(id):
    if id == 0:
        return jsonify({"status": "not ok", "message": "this server could not understand your request"}), 400

    student = data[id]

    return jsonify({"status": "ok", "student": student}), 200

# post
# /api/cv


@app.route('/api/cv', methods=['POST'])
def post():
    # get name posted
    name = request.json['name']

    # create name
    data.append(name)

    return jsonify({"status": "ok", 'id': len(data)}), 200

# put
# /api/cv/5


@app.route('/api/cv/<int:id>', methods=['PUT'])
def put(id):
    # bad request
    if id < 1 or id > 9:
        return jsonify({"status": "not ok", "message": "this server could not understand your request"}), 400

    # get index of id
    i = id - 1
    # get id name
    old_name = data[i]

    # get new name
    name = request.json['name']

    # insert new name at index i
    data.insert(i, name)
    # remove old name
    data.remove(old_name)

    return jsonify({"status": "ok", "student": {'id': i+1, 'name': data[i]}}), 200

# delete
# /api/cv/1


@app.route('/api/cv/<int:id>', methods=['DELETE'])
def delete(id):
    if id == 0:
        return jsonify({"status": "not ok", "message": "this server could not understand your request"}), 400

    name = data[id-1]
    data.remove(name)

    return jsonify({"status": "ok"}), 200


# delete
# /api/cv/1
@app.route('/api/cv/all/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def all(id):
    message = 'GET'
    status = 'ok'
    bodyJson = request.json

    if request.method == 'POST':
        message = 'POST'
    elif request.method == 'PUT':
        message = 'PUT'
    elif request.method == 'DELETE':
        message = 'DELETE'
    else:
        message = 'GET'

    return jsonify({'status': status, 'message': message, 'id': id, 'bodyJson': bodyJson}), 200

#


UPLOAD_FOLDER = r'C:\github\cv\gokPrj\static\uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
save_mode = 0  # 1001


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/cv/upload', methods=['GET', 'POST'])
def upload_file():
    # get querystring
    filename = '' if request.args.get(
        'filename') is None else request.args.get('filename')
    uri = '' if request.args.get('uri') is None else request.args.get('uri')
    uri2 = '' if request.args.get('uri2') is None else request.args.get('uri2')
    #
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            root, ext = os.path.splitext(filename)
            print(root, ext)
            ext = ext.lower()
            ext = '.jpeg' if ext == '.jpg' else ext

            if save_mode == 0:
                file.save(filePath)
                uri = f'/static/uploads/{filename}'
            else:
                f = file.read()
                print('file-len', len(f))
                imgArray = np.frombuffer(f, np.uint8)

                # create image
                img = cv.imdecode(imgArray, cv.IMREAD_COLOR)

                if save_mode == 1000:
                    # write image to path
                    cv.imwrite(filePath, img)
                    uri = f'/static/uploads/{filename}'

                mime = mimetypes.types_map[ext]
                if save_mode == 1010:
                    # transform to base64 url
                    # 1
                    uri = to_base64_uri_pil(img, ext, mime)

                if save_mode == 1001:
                    # 2
                    uri = to_base64_uri(img, ext, mime)

            return redirect(url_for('upload_file', uri=uri))

    return f'''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>      
    </form>
    <img src="{uri}" />
    '''


def to_base64_uri_pil(img, ext, mime):
    imgRGB = img[:, :, ::-1]
    imgPIL = Image.fromarray(imgRGB)
    buff = io.BytesIO()

    imgFormat = ext[1:]
    print(imgFormat)

    imgPIL.save(buff, format=imgFormat)
    imgBase64 = base64.b64encode(buff.getvalue()).decode("utf-8")

    uri = f"data:{mime};base64,{imgBase64}"
    return uri


def to_base64_uri(img, ext, mime):
    retval, buffer = cv.imencode(ext, img)
    imgBase64_2 = base64.b64encode(buffer).decode("utf-8")

    uri2 = f"data:{mime};base64,{imgBase64_2}"
    return uri2


if __name__ == "__main__":
    app.run(host='0.0.0.0')
