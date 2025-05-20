# YOLOv9 + MiDaS Real-Time Object Size Estimation

This project enables **real-time object detection** and **physical size estimation** using [YOLOv9](https://github.com/WongKinYiu/yolov9) and [MiDaS](https://github.com/isl-org/MiDaS). It uses a webcam and provides a **browser-based interface** via Flask.

📏 Measurements are calibrated using a **known reference object** (like an A4 paper or credit card) for accurate pixel-to-centimeter scaling.

---

## 📹 Demo Preview

![Demo](assets/YOLOv9MiDaSRealTimeObjectSizeMeasurement.gif)

---

## 📦 Features

- ✅ YOLOv9 object detection (runs on **GPU or CPU**)
- ✅ Depth-aware size estimation using **MiDaS**
- ✅ Web UI for real-time preview (**OpenCV + Flask**)
- ✅ Reference-based calibration using a fixed object (e.g., A4 paper or credit card)

---

## 🧰 Requirements

- Python 3.10
- CUDA 12.1 (for GPU mode — optional)
- A webcam
- Python packages listed in `requirements.txt`

---

## 🚀 Installation

```bash
# 1. Clone YOLOv9 repo (used for model modules)
git clone https://github.com/WongKinYiu/yolov9.git

# 2. Set up virtual environment
python -m venv yolov_env
.\yolov_env\Scripts\activate

# 3. Install required Python packages
pip install -r requirements.txt
```

---

## 💡 Note

This project **does not include** the model weight files for YOLOv9 and MiDaS due to file size and licensing limitations.

Please **manually download** the following files and place them in the `weights/` folder:

- `yolov9-e.pt`  
  🔗 [Download from YOLOv9 Releases](https://github.com/WongKinYiu/yolov9/releases)

- `dpt_hybrid_384.pt`  
  🔗 [Download from MiDaS Repository](https://github.com/isl-org/MiDaS#using-the-models)

Your directory structure should look like this:

```
YOLOv9-Object-Size-Measurement/
│
├── app.py
├── yolo_midas_utils.py
├── requirements.txt
├── camcheck.py
├── camtest.py
├── yolov9/                     # cloned yolov9 repo
├── weights/
│   ├── yolov9-e.pt
│   └── dpt_hybrid_384.pt
└── templates/
    └── index.html
```

---

## 🖼️ Preview

The application uses your webcam to display bounding boxes around objects, showing **real-time width and height in centimeters**. Measurements are adjusted based on a known reference object’s scale.

---

## 🙌 Acknowledgements

- [YOLOv9](https://github.com/WongKinYiu/yolov9) by WongKinYiu
- [MiDaS](https://github.com/isl-org/MiDaS) by Intel ISL
- OpenCV, Flask, and PyTorch communities

---

Built by [@JANGRAEJO](https://github.com/JANGRAEJO) 🚀
