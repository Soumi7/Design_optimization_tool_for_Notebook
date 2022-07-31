from distutils.log import debug
from flask import Flask, request, jsonify, render_template, url_for, make_response
from werkzeug.utils import secure_filename
import os
import json
import numpy as np
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./imgdir"
import numpy as np
import cv2
import pandas as pd
import io
from PIL import Image
#import StringI

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/fan_orientation', methods=["GET","POST"])
def fan_orientation():
    return render_template('fan_orientation.html')

@app.route('/unit_of_measure', methods=["GET","POST"])
def unit_of_measure():
    return render_template('unit_of_measure.html')

@app.route('/calculate', methods=["GET","POST"])
def list_post():    
    # #data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) #number of images 1 (RGB image)
    # data = request.files['data']
    # in_memory_file = io.BytesIO()
    # filepath = os.path.join(app.config['imgdir'], "img")
    # filepath.save(in_memory_file)
    
    # # filename = secure_filename(data.filename) # save file 
    
    # # data.save(filepath)
    # img = cv2.imread(filepath,0)

    #npimg = np.fromfile(request.files['file'], numpy.uint8)
    # convert numpy array to image
    #img = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE

    json_body = request.get_json()
    predictions = 2 * json_body[0]   
    #predictions = list(predictions)
    #return jsonify(results = predictions)

    #######################

    # inputs

    int_features = [x for x in request.form.values()]
    print(int_features)

    date=int_features[0]
    
    group=int_features[1]

    #####################


    file = request.files['file']
    npimg = np.fromfile(file, np.uint8)
    img = cv2.imdecode(npimg, 0)

    thresh,img_bin = cv2.threshold(img,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    img_bin = 255-img_bin
    #####################
    
    

        


    ##############################3
    arr = np.array(outer)
    # print(arr)    
    dataframe = pd.DataFrame(arr.reshape(len(row), countcol))
    data = dataframe.style.set_properties(align="left")
    # dataframe.to_csv("output.csv")
    # dataframe=pd.read_csv("output.csv")

    resp = make_response(dataframe.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=table.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)