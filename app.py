import os
from flask import Flask, request, render_template, send_from_directory
import numpy as np
import h5py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import spatial
from skimage import io
from werkzeug.utils import secure_filename

app = Flask(__name__)

h5f = h5py.File("/Users/sudipkhadka/Desktop/Computer-Vision/research/RESNET50_Model/RESNET50Features.h5", "r")
features = h5f['dataset_1'][:]
image_name = h5f['dataset_2'][:]
h5f.close()

path = "/Users/sudipkhadka/Desktop/Computer-Vision/Retraining_image/embedding"

def resnet_extract_feature(image_path):
    img = image.load_img(image_path, target_size=(input_shape[0], input_shape[1]))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    features = model.predict(img)
    norm_features = features[0]/LA.norm(features[0])
    return norm_features

def reterive_similar_image(query_image_path):  

    print("Reteriving Images.........")  
    X = resnet_extract_feature(query_image_path)

    scores = []
    for i in range(features.shape[0]):
        score  = 1 - spatial.distance.cosine(X, features[i])
        scores.append(score)
    scores = np.array(scores)
    rank_id = np.argsort(scores)[::-1]
    rank_score = scores[rank_id]

    n = 10
    lists = [os.path.join(path, image_name[index].decode('utf-8')) if isinstance(image_name[index], bytes) else os.path.join(path, image_name[index]) 
         for i, index in enumerate(rank_id[0:n])]
    return lists 


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["query_image"]
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join("path/uploads", filename)
            file.save(filepath)
            similar_images = retrieve_similar_image(filepath)
            return render_template("index.html", query_image=filepath, similar_images=similar_images)

    return render_template("index.html")

@app.route('/path/<path:filename>')
def serve_static(filename):
    return send_from_directory('path', filename)

if __name__ == "__main__":
    app.run(debug=True)