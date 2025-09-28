import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/OnlyCSDC/weights/best.pt')  #
    model.val(data='分割\p1.yaml',
              split='test',
              imgsz=640,
              batch=16,

              project='runs/val',
              name='OnlyCSDC',
              )  # data

