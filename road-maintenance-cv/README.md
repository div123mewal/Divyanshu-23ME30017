# 📹 Road Maintenance Computer Vision Pipeline

A deployed machine learning vision system designed to detect and classify municipal infrastructure damage (potholes and cracks) from moving vehicular dashcam footage.

## 🛠️ Technical Highlights
* **Frame Preprocessing:** Developed a Computer Vision pipeline utilizing `OpenCV` to extract, normalize, and preprocess raw dashcam video frames.
* **Model Architecture:** Trained a custom `YOLOv8` object detection model, leveraging extensive data augmentation techniques to handle highly variable environmental lighting conditions.
* **Performance Metrics:** Achieved **88% mAP@0.5** and high IoU (Intersection over Union) scores, significantly minimizing false positives in critical defect detection.
* **Production Deployment:** Designed and deployed an interactive `Streamlit` dashboard to ingest video feeds and render synchronized, real-time bounding boxes for end-users.

## 🚀 Execution Instructions
Install the required dependencies:
```bash
pip install -r requirements.txt