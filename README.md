# 🔐 Facial Authentication System

A computer vision based authentication system that uses facial recognition to identify and verify users in real time.
The system captures face images, trains a recognition model, and authenticates users through a web interface.

---

## 📌 Project Overview

Traditional authentication methods such as passwords and PINs can be insecure or easily forgotten. Facial authentication provides a secure and convenient biometric solution.

This project implements a facial recognition based authentication system that allows users to:

* Register their face
* Train a face recognition model
* Authenticate users using live camera input
* Detect unknown users and trigger alerts

The system uses computer vision and machine learning techniques to provide real-time identity verification.

---

## 🚀 Features

* Face enrollment for new users
* Face recognition using trained model
* Real-time authentication
* Intruder detection for unknown faces
* Web interface for easy interaction
* Dataset creation and training pipeline

---

## 🧠 Technologies Used

* Python
* Flask
* OpenCV
* NumPy
* Machine Learning
* HTML / CSS
* Camera Integration

---

## 📂 Project Structure

```id="k5fj92"
facial-authentication-system
│
├── dataset/
│   └── (stored face images)
│
├── intruder/
│   └── (captured images of unknown users)
│
├── logic/
│   ├── enroll.py
│   ├── train.py
│   ├── recognize.py
│   └── intruder_alert.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── trainer/
│   └── trainer.yml
│
├── app.py
└── README.md
```

---

## ⚙️ Installation

Clone the repository

git clone https://github.com/YOUR_USERNAME/facial-authentication-system.git
```

Navigate to the project directory

cd facial-authentication-system
```

Create a virtual environment

python -m venv venv
```

Activate environment

Windows

venv\Scripts\activate
```

Install required libraries

pip install flask opencv-python numpy
```

---

## ▶️ Running the Application

Start the Flask server:
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000
```

---

## 🧩 System Workflow

1. **Enroll User**

   * Capture multiple face images
   * Store them in the dataset folder

2. **Train Model**

   * Train the face recognition model using captured images

3. **Authenticate**

   * System captures live camera feed
   * Detects and recognizes the face
   * Grants access if match found

4. **Intruder Detection**

   * Unknown faces are stored in the intruder folder
   * Alert is triggered

---

## 📈 Future Improvements

* Deploy the system on cloud servers
* Add deep learning face recognition models
* Improve accuracy with larger datasets
* Add login logs and monitoring dashboard
* Integrate with security systems

---

## 👩‍💻 Author

**Subhaashree Jagannathan**

GitHub:
https://github.com/Subhaashree06

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**!
