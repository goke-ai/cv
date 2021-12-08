from PIL import Image
from flask import Flask, request, make_response
import urllib.request
import numpy as np
import cv2 as cv

# instance of Flask
app = Flask(__name__)

# default route
@app.route("/")
def index():
    return "Welcome! to Index Page"

# /hello
@app.route("/hello")
def hello_world():
    return "<h1>Hello, World!</h1>"

# /user
@app.route("/user/<username>")
def hello_user(username):
    return f"Welcome!, {username}"

# /display
@app.route('/display/', methods=['GET'])
def display():
    print('display')
    externalURL = r'https://raw.githubusercontent.com/goke-ai/cv/master/essential/assets/Picture1.png'
    fileURL = r'file:///github/cv/samples/data/face.jpg'
    
    imgUrl = request.args.get('url')
    
    if imgUrl is None:
        imgUrl = fileURL
        
    # Get the image:
    with urllib.request.urlopen(imgUrl) as url:
        img = np.asarray(bytearray(url.read()), dtype=np.uint8)

    print(img.shape)
    
    # Convert the image to OpenCV format:
    imgBGR = cv.imdecode(img, -1)
    
    print(imgBGR.shape)

    
    # Compress the image and store it in the memory buffer:
    retval, buffer = cv.imencode('.jpeg', imgBGR)
    
    
    print(len(buffer))
    print(buffer.shape)
    
    # Build the response:
    response = make_response(buffer.tobytes())
    response.headers['Content-Type'] = 'image/jpeg'
    # Return the response:
    return response



# pass parameter or aguement in route
# /add/a/b
@app.route("/add/<a>/<b>")
def add(a, b):
    a1 = int(a)
    b1 = int(b)
    sum = a1 + b1
    return f"{a} + {b} = {sum}"

# pass parameter or aguement in query-string
# /add2?a=10&b=5
# use GET i.e httpGet
@app.route("/add2", methods=['GET'])
def add2():
    a = request.args.get('a')
    b = request.args.get('b')
    a1 = int(a)
    b1 = int(b)
    sum = a1 + b1
    return f"{a} + {b} = {sum}"

# 



if __name__ == "__main__":
    app.run(host='0.0.0.0')