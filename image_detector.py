# pip install ultralytics
from ultralytics import YOLO

# Загрузка максимально качественной модели
model = YOLO('yolov8x.pt')   # можно заменить на yolov8l.pt или свою обученную модель

# Параметры оптимизации:
# imgsz=1280 — лучшее качество распознавания
# conf=0.15 — низкий порог, чтобы не пропускать слабые объекты
# iou=0.45 — оптимальный NMS
# max_det=500 — увеличенный лимит объектов
# augment=True — включение тестовой аугментации (чуть медленнее, но точнее)
# half=False — FP32 лучший по качеству (если нужен максимум)
# verbose=False — убираем лишний вывод

result = model.predict(
    source='foto.jpg',
    save=True,
    show=True,
    imgsz=1280,
    conf=0.15,
    iou=0.45,
    max_det=500,
    augment=True,
    half=False,
    verbose=False
)
