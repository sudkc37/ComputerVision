import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

Project_Name = "Computer-Vision"

list_of_file = [
    ".github/workflows/.gitkeep",
    "main.py",
    "app.py",
    "Dcokerfile",
    "requirements.txt",
    "setup.py",
    "research/Base_Mode/base.ipynb",
    "research/CNN_Model/cnn.ipynb",
    "research/VGG16_Model/vgg16.ipynb",
    "research/VGG19_Model/vgg19.ipynb",
    "research/RESNET50_Model/resnet50.ipynb",
    "research/Tuned_RESNET50_Model/tuned_resnet.ipynb",
    "templates/index.html"

]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directiry: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")
    else:
        logging.info(f"{filename} is alreay exists")
