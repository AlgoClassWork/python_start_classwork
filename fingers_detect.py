import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

# детектор руки, распознает 1 руку
detector = HandDetector(detectionCon=0.8, maxHands=1)

finger_names = ["Большой", "Указательный", "Средний", "Безымянный", "Мизинец"]

while True:
    success, frame = cap.read()
    if not success:
        break

    # поиск руки
    hands, frame = detector.findHands(frame)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # координаты кончиков пальцев
        lmList = hand["lmList"]  # список координат всех 21 ключевой точки

        for i, finger_up in enumerate(fingers):
            if finger_up:  # палец поднят
                # выводим в консоль название пальца
                print(f"{finger_names[i]} поднят")
                
                # выводим текст на видео
                x, y = lmList[4*i + 4][:2]  # кончик пальца
                cv2.putText(frame, finger_names[i], (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Finger Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
