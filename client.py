from __future__ import print_function
import requests
import json
import cv2
import numpy as np

addr = 'http://127.0.0.1:5000'
test_url = addr + '/api/test'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('images/receipt.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response
#print(response.text)
#      ^^^^^^^^^^^^^^
#      ||||||||||||||
#      NEW IMAGE BYTES
