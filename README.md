# YOLOv9 + MiDaS Real-Time Object Size Estimation

This project enables **real-time object detection and physical size estimation** using [YOLOv9](https://github.com/WongKinYiu/yolov9) and [MiDaS](https://github.com/isl-org/MiDaS). It uses a webcam and provides a browser-based interface via Flask.

> 📏 Measurements are calibrated using a known reference object (like an A4 paper) for accurate pixel-to-centimeter scaling.

---

## 📦 Features

- ✅ YOLOv9 object detection (runs on GPU or CPU)
- ✅ Depth-aware size estimation using MiDaS
- ✅ Web UI for real-time preview (OpenCV + Flask)
- ✅ Reference-based calibration using fixed object (e.g., A4 paper)

---

## 🧰 Requirements

- Python 3.10
- CUDA 12.1 (for GPU mode — optional)
- A webcam
- pip packages listed in `requirements.txt`

---

## 🚀 Installation

```bash
# Clone YOLOv9 repo (used for model modules)
git clone https://github.com/WongKinYiu/yolov9.git

# Set up virtual environment
python -m venv yolov_env
.\yolov_env\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
