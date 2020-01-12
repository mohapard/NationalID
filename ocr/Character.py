#!/usr/bin/env python
# coding: utf-8

import os
import cv2
import numpy as np
import flask
import pytesseract
from PIL import Image
from flask import Flask,request,render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)



@app.route('/character', methods=['GET'])
def character():
    # Let's load a simple image with 3 black squares 
    image = cv2.imread('4.png') 
    
    # Grayscale 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    (thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


    image = cv2.resize(im_bw, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    image = cv2.medianBlur(image, 3)
    image = cv2.GaussianBlur(image,(5,5),0)
    
    return pytesseract.image_to_string(image, lang= 'ara')

@app.route('/digit', methods=['GET'])
def digit():

    # Let's load a simple image with 3 black squares 
    image = cv2.imread('6.png') 
    
    # Grayscale 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    (thresh, im_bw) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    image = cv2.resize(im_bw, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    image = cv2.medianBlur(image, 3)
    image = cv2.GaussianBlur(image,(5,5),0)
 
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    cv2.drawContours(image, contours, -1, (255, 255, 255), thickness=cv2.FILLED) 
    return pytesseract.image_to_string(image, lang= 'tur')

app.run("0.0.0.0","8080")




