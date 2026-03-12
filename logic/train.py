import cv2
import numpy as np
import os


def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces = []
    labels = []

    for folder in os.listdir("dataset"):
        label = int(folder.split("_")[1])
        folder_path = os.path.join("dataset", folder)

        for img in os.listdir(folder_path):
            img_path = os.path.join(folder_path, img)
            face = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            faces.append(face)
            labels.append(label)

    recognizer.train(faces, np.array(labels))
    os.makedirs("trainer", exist_ok=True)
    recognizer.save("trainer/trainer.yml")
