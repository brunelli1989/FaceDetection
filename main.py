import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
face_detection = mp.solutions.face_detection
detector = face_detection.FaceDetection()
output_frame = mp.solutions.drawing_utils

while True:
    success, frame = webcam.read()
    if not success:
        break

    faces = detector.process(frame)

    for detection in faces.detections:
        output_frame.draw_detection(frame, detection)
        print(detection.score)

    cv2.imshow("Rostos na WebCam", frame)

    if cv2.waitKey(10) == 27:
        break

webcam.release()
cv2.destroyAllWindows()