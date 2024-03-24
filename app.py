from flask import Flask, render_template, request, send_file,redirect,url_for
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw, ImageFont
from IPython.display import display
from skimage.io import imread,imshow
import os
import io
import base64
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go 
import matplotlib.pyplot as plt
import cv2
import rembg

app = Flask(__name__)
#functions
def rotate_image(angle):
    im = Image.open('rotated_image.jpg')
    im = im.rotate(angle)
    byte_io = io.BytesIO()
    im.save(byte_io, format="JPEG")
    byte_io.seek(0)  # Reset pointer to the beginning of the BytesIO object
    return byte_io
def Cropping(coordinate, width, height):
    im = Image.open('rotated_image.jpg')
    im = im.crop((coordinate[0], coordinate[1], coordinate[0] + width, coordinate[1] + height))
    byte_io = io.BytesIO()
    im.save(byte_io, format="JPEG")
    byte_io.seek(0)
    return byte_io
def Blurring(stepsize):
    # image=imread(name)
    im = Image.open('rotated_image.jpg')
    image=imread('temp_image.jpg')
    # dimension=image.shape
    im = im.filter(ImageFilter.GaussianBlur(radius=stepsize))

    byte_io = io.BytesIO()
    im.save(byte_io, format="JPEG")
    byte_io.seek(0)  
    return byte_io
def RemoveBackground(name):
    # input_image = Image.open()
    im = Image.open('rotated_image.jpg')
    input_array = np.array(im)
    output_array = rembg.remove(input_array)
    im = Image.fromarray(output_array)
    im = im.convert('RGB')
    # output_image = output_image.convert('RGB')

    byte_io = io.BytesIO()
    im.save(byte_io, format="JPEG")
    byte_io.seek(0)  
    return byte_io
def imagewriter(font,font_size,text,colour,position):
    coordinates = position.split(",")
    position=(int(coordinates[0].strip()), int(coordinates[0].strip()))
    im= Image.open('rotated_image.jpg')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font, font_size)
    draw.text(position, text, fill=colour, font=font,align=position)

    byte_io = io.BytesIO()
    im.save(byte_io, format="JPEG")
    byte_io.seek(0)  
    return byte_io
def erase_region(top_left_x, top_left_y, width, height):
    im= Image.open('rotated_image.jpg').convert('RGB')
    img_arr = np.array(im)
    img_arr[top_left_y:top_left_y + height, top_left_x:top_left_x + width] = (0, 0, 0)
    im = Image.fromarray(img_arr)
    
    byte_io = io.BytesIO()
    im.save(byte_io, format="JPEG")
    byte_io.seek(0)  
    return byte_io


# app routing
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


@app.route('/features', methods=['GET', 'POST'])
def features():
    img_base64 = ''
    if request.method =='POST':
        img_file = request.files['image']
        global temp_filename
        temp_filename = 'temp_image.jpg'
        img_file.save(temp_filename)
        global img
        try:
            with Image.open(temp_filename) as img:
                global output_filename
                output_filename = 'rotated_image.jpg'
                img.save(output_filename)
    
                img_byte_array = io.BytesIO()
                img.save(img_byte_array, format='JPEG')
    
                img_byte_array = img_byte_array.getvalue()
                img_base64 = base64.b64encode(img_byte_array).decode('utf-8')
                if request.form.get('angle'):
                    return redirect('/feature1',temp_filename=temp_filename)
                if request.form.get('width'):
                    return redirect('/feature2',temp_filename=temp_filename)
                if request.form.get('stepsize'):
                    return redirect('/feature3',temp_filename=temp_filename)
                if request.form.get('removebackground'):
                    return redirect('/feature4',temp_filename=temp_filename)
                if request.form.get('text'):
                    return redirect('/feature5',temp_filename=temp_filename)
                return render_template('index.html', img_base64=img_base64)
        except (IOError, OSError) as e:
            return render_template('error.html')
    return render_template('index.html')

@app.route('/feature1', methods=['GET', 'POST'])
def feature1():
    if request.method == 'POST':
        angle = int(request.form.get('angle'))
        img_byte_io = rotate_image(angle)
        global output_filename
        output_filename = 'rotated_image.jpg'
        with open(output_filename, 'wb') as output_file:
            output_file.write(img_byte_io.getvalue())
        img_base64 = base64.b64encode(img_byte_io.read()).decode()
        return render_template('index.html', img_base64=img_base64, output_filename=output_filename)

@app.route('/feature2', methods=['GET', 'POST'])
def feature2():
    if request.method == 'POST':
        # coordinate = request.form.get('coordinate')
        width = int(request.form.get('width'))
        height = int(request.form.get('height'))
        x = int(request.form.get('coordinatex'))
        y = int(request.form.get('coordinatey'))
        img_byte_io = Cropping([x,y],width,height)

        global output_filename
        output_filename = 'rotated_image.jpg'
        with open(output_filename, 'wb') as output_file:
            output_file.write(img_byte_io.getvalue())
        img_base64 = base64.b64encode(img_byte_io.read()).decode()
        return render_template('index.html', img_base64=img_base64, output_filename=output_filename)   

@app.route('/feature3', methods=['GET', 'POST'])
def feature3():
    if request.method == 'POST':
        # coordinate = request.form.get('coordinate')
        stepsize = int(request.form.get('stepsize'))
        img_byte_io = Blurring(stepsize)
        global output_filename
        output_filename = 'rotated_image.jpg'
        with open(output_filename, 'wb') as output_file:
            output_file.write(img_byte_io.getvalue())
        img_base64 = base64.b64encode(img_byte_io.read()).decode()
        return render_template('index.html', img_base64=img_base64, output_filename=output_filename) 

@app.route('/feature4', methods=['GET', 'POST'])
def feature4():
    if request.method == 'POST':
        # coordinate = request.form.get('coordinate')
        name=0
        img_byte_io = RemoveBackground(name)
        global output_filename
        output_filename = 'rotated_image.jpg'
        with open(output_filename, 'wb') as output_file:
            output_file.write(img_byte_io.getvalue())
        img_base64 = base64.b64encode(img_byte_io.read()).decode()
        return render_template('index.html', img_base64=img_base64, output_filename=output_filename) 

# @app.route('/feature5', methods=['GET', 'POST'])
# def feature5():
#     if request.method == 'POST':
#         font=request.form.get('font')
#         font_size=int(request.form.get('font_size'))
#         text=request.form.get('text')
#         colour=request.form.get('color')
#         position=request.form.get('position')
#         img_byte_io = imagewriter(font,font_size,text,colour,position)
#         global output_filename
#         output_filename = 'rotated_image.jpg'
#         with open(output_filename, 'wb') as output_file:
#             output_file.write(img_byte_io.getvalue())
#         img_base64 = base64.b64encode(img_byte_io.read()).decode()
#         return render_template('index.html', img_base64=img_base64, output_filename=output_filename) 




@app.route('/feature5', methods=['GET', 'POST'])
def feature5():
    if request.method == 'POST':
        font = ImageFont.load_default()  # Load default system font
        font_size = int(request.form.get('font_size'))
        text = request.form.get('text')
        colour = request.form.get('color')
        position = request.form.get('position')
        img_byte_io = imagewriter(font, font_size, text, colour, position)
        global output_filename
        output_filename = 'rotated_image.jpg'
        with open(output_filename, 'wb') as output_file:
            output_file.write(img_byte_io.getvalue())
        img_base64 = base64.b64encode(img_byte_io.read()).decode()
        return render_template('index.html', img_base64=img_base64, output_filename=output_filename)


@app.route('/feature6', methods=['GET', 'POST'])
def feature6():
    if request.method == 'POST':
        width = int(request.form.get('width'))
        height = int(request.form.get('height'))
        x = int(request.form.get('coordinatex'))
        y = int(request.form.get('coordinatey'))
        img_byte_io = Cropping([x,y],width,height)
        img_byte_io = erase_region( x, y, width, height)
        global output_filename
        output_filename = 'rotated_image.jpg'
        with open(output_filename, 'wb') as output_file:
            output_file.write(img_byte_io.getvalue())
        img_base64 = base64.b64encode(img_byte_io.read()).decode()
        return render_template('index.html', img_base64=img_base64, output_filename=output_filename) 

@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    return send_file(filename, as_attachment=True)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('contributions.html')

if __name__ == '__main__':
    app.run(debug=True)

    
