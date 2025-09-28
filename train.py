import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO
from ultralytics import RTDETR
if __name__ == '__main__':
    # model = YOLO('mymodels/yolov8-seg-MyBest2-OCSDC.yaml')# model=RTDETR,
    model = YOLO('runs\\train\\OnlyECSA\weights\\last.pt')  # model=RTDETR,
    # model.load('runs/train/exp10/weights/best.pt')  # loading pretrain weights
    model.train(data='分割/p1.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=16, #16
                close_mosaic=10,
                patience=50,
                workers=8,
                device='0',

                # lr0=0.001,
                cos_lr=True,
                # mixup=0.2,
                hsv_v=0.4,
                optimizer='Adam',  # using SGD
                resume=True,
                # resume='runs\\train\exp11\weights\\best.pt',
                # freeze=list(range(9)),
                label_smoothing= 0.1,
                copy_paste=0.3,

                # amp=False,  # close amp
                # fraction=0.2,
                project='runs/train',
                name='OnlyECSA',
                )
    # print(model.info())#若每一层结构信息+(detailed=True)
