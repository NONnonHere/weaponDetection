# weaponDetection

Weapon Detection with YOLO11
This project implements a weapon detection system using YOLO11, trained on the "Weapon Detection Test" dataset from Kaggle. It detects objects like guns and knives in images and real-time webcam feeds. The model is built and trained using the Ultralytics YOLO11 repository, with support for GPU inference.


<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
  <img src="https://github.com/user-attachments/assets/68f9b104-3733-4b49-a3b2-1bbc6179d380" alt="Image 1" style="width: 100%;"/>
  <img src="https://github.com/user-attachments/assets/26f41989-ea07-47ca-b8c1-aedeae934b28" alt="Image 3" style="width: 100%;"/>
  <img src="https://github.com/user-attachments/assets/3a3e1d4e-c558-4aad-bdf8-600122b4211b" alt="Image 2" style="width: 100%;"/>
</div>



Clone the Repository:
```
git clone https://github.com/NONnonhere/weaponDetection.git
cd weaponDetection
```


Set Up Virtual Environment:
```
python -m venv yolo_env

.\yolo_env\Scripts\Activate.ps1

yolov5_env\Scripts\activate
```

If blocked by execution policy, set it temporarily:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Clone Ultralytics YOLO:
```
https://github.com/ultralytics/ultralytics
cd ultralytics
```


Install Dependencies:
```
pip install -e .
pip install opencv-python
```

For GPU Support:
```
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

For the File of the model 

https://drive.google.com/file/d/1cXBESTEypw6MxW925XTNR_zrzRasyDjY/view?usp=sharing



