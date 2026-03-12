import cv2
import os
import time
import winsound


def recognize_user():
    face_detector = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer/trainer.yml")

    intruder_dir = "intruder"
    os.makedirs(intruder_dir, exist_ok=True)

    cam = cv2.VideoCapture(0)

    authorized_count = 0
    intruder_count = 0
    intruder_saved = False

    THRESHOLD = 50        # LBPH distance threshold
    CONSISTENT_FRAMES = 5

    print("Press Q to quit")

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            _, confidence = recognizer.predict(face)

            # Frame-based decision
            if confidence < THRESHOLD:
                authorized_count += 1
                intruder_count = 0
            else:
                intruder_count += 1
                authorized_count = 0

            # Final decision after consistency
            if authorized_count >= CONSISTENT_FRAMES:
                label = "AUTHORIZED"
                color = (0, 255, 0)
                intruder_saved = False

            elif intruder_count >= CONSISTENT_FRAMES:
                label = "🚨 INTRUDER"
                color = (0, 0, 255)

                if not intruder_saved:
                    filename = f"intruder_{time.strftime('%Y%m%d_%H%M%S')}.jpg"
                    cv2.imwrite(os.path.join(intruder_dir, filename), frame)
                    winsound.Beep(1200, 800)
                    intruder_saved = True
            else:
                label = "SCANNING..."
                color = (255, 255, 0)

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(
                frame,
                label,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                color,
                2
            )

        cv2.imshow("Facial Authentication", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()
