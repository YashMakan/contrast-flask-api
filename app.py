from flask import Flask, request, Response
import numpy as np
import cv2
import os
import base64
from random import randint
# Initialize the Flask application
app = Flask(__name__)

def getFile():
    while True:
        filenamed='{}.jpg'.format(str(randint(0,100000000000000000000000000000000000000000000000000)))
        if os.path.isfile(filenamed):
            pass
        else:
            return filenamed
# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    filenamed=getFile()
    cv2.imwrite(filenamed,final)
    with open(filenamed, "rb") as imageFile:
        st = base64.b64encode(imageFile.read())
    os.remove(filenamed)
    return Response(response=st, status=200)


# start flask app
app.run()
