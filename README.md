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
---
### 🛠️ Tech Stack

- YOLOv8
- DeepSort for object tracking
- OpenCV for computer vision
- Flask for web integration
---
### 📌 Notes
Follow the click sequence strictly: 
- **North Entry ⬇️ South Exit ⬇️** → from the **top side**  
- **East Entry ⬆️ West Exit ⬆️** → from the **bottom side**

![Capture1](https://github.com/user-attachments/assets/0dfc04c1-7ffa-4963-98f3-dbaa56ef0ff4)
![Capture2](https://github.com/user-attachments/assets/06a2b264-7c76-4422-8568-df759cbdb53c)
![Capture4](https://github.com/user-attachments/assets/c824d5f6-fb49-4560-99f9-43ed97696629)
![Capture3](https://github.com/user-attachments/assets/778e973f-d98e-4bf5-b590-5fa7ed4a90e1)
![Capture5](https://github.com/user-attachments/assets/feba4b42-3d98-4ea3-aabe-2cb6eed6df23)
![Capture6](https://github.com/user-attachments/assets/dabd2a4a-ba50-42fc-9d63-dae6cc7b7856)
