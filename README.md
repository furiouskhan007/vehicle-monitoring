# 🚦 TrafficInsight  
YOLOv8 + DeepSort + OpenCV + Flask  

TrafficInsight is a real-time vehicle monitoring system that allows **ROI (Region of Interest) selection** by mouse clicks and logs detected traffic events into a CSV file.  

---
## ✨ Features  
- ROI selection via mouse clicks (**North → South → East → West**)  
- Line drawing logic: **Left ➝ Right**  
- Vehicle detection & tracking with **YOLOv8 + DeepSort**  
- Data storage in CSV format  
**Click Sequences:**  
- **North Entry ⬇️ South Exit ⬇️** → from the **top side**  
- **East Entry ⬆️ West Exit ⬆️** → from the **bottom side**  
**CSV Log Format:**  
| ID | Type | Entry Point | Exit Point | Entry Time |  
|----|------|-------------|------------|------------|  
| 10 | car  | north       | west       | 10:31.7    |  
---
## ⚙️ Requirements  
- Python **3.11.5**  
- Dependencies listed in `requirements.txt`  
---

## 🚀 How to Run  

### Step 1: Clone or Download Repository  
```bash
git clone https://github.com/furiouskhan007/vehicle-monitoring.git 
cd TrafficInsight
```
### Step 2: Download Weights
- Download YOLOv8 weights → yolov8n.pt
- Place it in the root directory 
- Download DeepSort checkpoint weights → Google Drive Link [ckpt.t7](https://drive.google.com/drive/folders/1xhG0kRH1EX5B9_Iz8gQJb7UNnn_riXi6)
- Place inside:
- vehicle-monitoring-main/deep_sort_pytorch/deep_sort/deep/checkpoint/

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
Step 4: Run the Application
```bash
python app.py
```

### 🛠️ Tech Stack

- YOLOv8
- DeepSort for object tracking
- OpenCV for computer vision
- Flask for web integration

### 📌 Notes
Follow the click sequence strictly: North → South → East → West
North/South clicks are drawn from the top side
East/West clicks are drawn from the bottom side
