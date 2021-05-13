from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import numpy as np
from PIL import Image
import json
import math
import requests
from django.conf import settings


# Create your views here.
@login_required
def home(request):
    return render(request, 'doctors/home.html')

@login_required
def appointments(request):
    return redirect('calendar')

@login_required
def predict(request):
    if request.method == 'GET':
        return render(request, 'doctors/predict.html')
    else:
        print('entered else')
        print("file recieved")
        form = request.FILES
        print(form['file'])

        file_object = request.FILES["file"]
        file_name = str(file_object)
        print(f'[INFO] File Name: {file_name}')
        path = os.path.join('doctors/static/doctors/', file_name)
        with open(path, 'wb+') as f:
            for chunk in file_object.chunks():
                f.write(chunk)
        #images = os.listdir("path/to/images") #Can use glob as well
        url = 'https://skin-cancer-sample.herokuapp.com/'
        img = np.asarray(Image.open(path).resize((256,256)))
        # img.save(settings.MEDIA_URL + 'cancer_images/', file_name)
        #print(img)
        class NumpyEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, np.ndarray):
                    return obj.tolist()
                return json.JSONEncoder.default(self, obj)
        json_dump = json.dumps({"image":img}, cls = NumpyEncoder)
        #print(json_dump)
        send_request = requests.post(url, json_dump)
        print(send_request)
        result = send_request.json()['results']
        print(result)
        index = np.argmax(result)
        print(result[0][index])

        cancers = {
            0: 'Actinic kerastose',
            1: 'Basal cell carcinoma',
            2: 'Benign keratosis-like lesions',
            3: 'Dermatofibroma',
            4: 'Melanocytic nevi',
            5: 'Melanoma',
            6: 'Vascular lessions'
        }
        path = 'doctors/' + file_name
        context = {
        "detected": cancers[index],
        "percentage": math.trunc(result[0][index]*100),
        "address": "Hyderabad, India",
        'images': path
        }

        return render(request, 'doctors/predict_res.html',context)
