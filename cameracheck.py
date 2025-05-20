import cv2

print("🔍 Searching for available camera indices...")
for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"✅ Camera index {i} is available")
        cap.release()
    else:
        print(f"❌ Camera index {i} not available")