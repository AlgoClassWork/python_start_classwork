import cv2

# каскад для глаз
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # поиск глаз
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # блюрим область глаз
    for (x, y, w, h) in eyes:
        # вырезаем область глаза
        eye_region = frame[y:y+h, x:x+w]

        # применяем сильный blur
        blurred_eye = cv2.GaussianBlur(eye_region, (51, 51), 30)

        # вставляем обратно в кадр
        frame[y:y+h, x:x+w] = blurred_eye

    cv2.imshow('Eye Blur Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
