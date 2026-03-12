import cv2
import os


def enroll_user(user_id):
    if not user_id.isdigit():
        return

    face_detector = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cam = cv2.VideoCapture(0)
    count = 0

    path = f"dataset/user_{user_id}"
    os.makedirs(path, exist_ok=True)

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face = gray[y:y+h, x:x+w]
            cv2.imwrite(f"{path}/{count}.jpg", face)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Enroll User", frame)

        if cv2.waitKey(1) & 0xFF == ord("q") or count >= 30:
            break

    cam.release()
    cv2.destroyAllWindows()
