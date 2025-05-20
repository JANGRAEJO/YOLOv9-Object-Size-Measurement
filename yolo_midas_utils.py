# yolo_midas_utils.py
import cv2
import torch
import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent / "yolov9"))

from models.common import DetectMultiBackend
from utils.general import non_max_suppression, scale_boxes
from utils.augmentations import letterbox
from utils.torch_utils import select_device

REFERENCE_CLASS_NAME = 'cell phone'  # 기준 물체 클래스
REFERENCE_WIDTH_CM = 8.5             # 예: 신용카드 너비
IMG_SIZE = 640
DEVICE = select_device('0' if torch.cuda.is_available() else 'cpu')
YOLO_PATH = Path("weights/yolov9-e.pt")

yolo = DetectMultiBackend(YOLO_PATH, device=DEVICE)
stride, names, pt = yolo.stride, yolo.names, yolo.pt
yolo.warmup(imgsz=(1, 3, IMG_SIZE, IMG_SIZE))

def detect_and_measure(frame):
    img = letterbox(frame, IMG_SIZE, stride=stride, auto=True)[0]
    img = img.transpose((2, 0, 1))[::-1]
    img = np.ascontiguousarray(img)
    img = torch.from_numpy(img).to(DEVICE).float() / 255.0
    if img.ndim == 3:
        img = img.unsqueeze(0)

    with torch.no_grad():
        pred = yolo(img)[0]
        pred = non_max_suppression(pred, conf_thres=0.25, iou_thres=0.45)[0]

    if pred is None or len(pred) == 0:
        return frame

    ref_px_width = None
    for *xyxy, conf, cls in pred:
        cls_name = names[int(cls)]
        x1, y1, x2, y2 = map(int, xyxy)
        w = x2 - x1
        if cls_name == REFERENCE_CLASS_NAME:
            ref_px_width = w
            break

    if ref_px_width is None:
        return frame  # 기준 객체 없으면 크기 측정 생략

    px_per_cm = ref_px_width / REFERENCE_WIDTH_CM

    for *xyxy, conf, cls in pred:
        x1, y1, x2, y2 = map(int, map(int, xyxy))
        width_px = x2 - x1
        height_px = y2 - y1
        width_cm = width_px / px_per_cm
        height_cm = height_px / px_per_cm

        label = f"W: {width_cm:.1f}cm H: {height_cm:.1f}cm"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return frame
