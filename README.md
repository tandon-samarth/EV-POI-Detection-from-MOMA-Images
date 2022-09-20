# EV-POI-Detection-from-MOMA-Images

The project objective is to leverage the power of AI and state of the art techniques for detetecting EV- charging stations in Italy. The Data consists of multiple EV stations near car parking around Italy .We use AI to detect the EV charging stations to improve the POI accuracy.

# Data 

Sample Image of Electric charging station.
![Image text](https://github.com/tandon-samarth/EV-POI-Detection-form-MOMA-Images/blob/main/sample-image.png)


# Yolov7 
YOLOv7 an object detectors in both speed and accuracy in the range from 5 FPS to 160 FPS and has the highest accuracy 56.8% AP among all known real-time object detectors with 30 FPS or higher on GPU V100. YOLOv7-E6 object detector (56 FPS V100, 55.9% AP) outperforms both transformer-based detector SWIN-L Cascade-Mask R-CNN (9.2 FPS A100, 53.9% AP) by 509% in speed and 2% in accuracy, and convolutional-based detector ConvNeXt-XL Cascade-Mask R-CNN (8.6 FPS A100, 55.2% AP) by 551% in speed and 0.7% AP in accuracy, as well as YOLOv7 outperforms: YOLOR, YOLOX, Scaled-YOLOv4, YOLOv5, DETR, Deformable DETR, DINO-5scale-R50, ViT-Adapter-B and many other object detectors in speed and accuracy. For more information [Yolov7](https://arxiv.org/abs/2207.02696)

## Data Preparation 

- YOLOv7 accepts label data in text (.txt) files in the following format
```
  images_0.jpg
  images_0.txt
```

- Format of txt files 
The txt files contains first value as the class label and normalized mid point of bounding box with width and height.
```
<class label> <x> <y> <w> <h> 
```

- Data Creation 
The data folder should be created in a way as shown 
```
  ├── yolov7
    └── train
      └── images (folder including all training images)
      └── labels (folder including all training labels)
    └── test
      └── images (folder including all testing images)
      └── labels (folder including all testing labels)
    └── valid
      └── images (folder including all valid images)
      └── labels (folder including all valid labels)
```

