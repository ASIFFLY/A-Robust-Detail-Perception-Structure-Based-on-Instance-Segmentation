import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/OCSDCCe/weights/best.pt')#
    # model.load('yolov8s.pt')  # loading pretrain weights
    model.predict(source='Predict/All//01image',#
                imgsz=640,
                project='runs/segment',
                name='OCSDCCe',
                save=True,
                conf=0.2,
                #save_txt=False,
                #visualize=True # visualize model features maps
                )
