import os
import cv2
import numpy as np
import pandas as pd
import logging


def read_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def read_classids(annotations_path, index=-2):
    with open(annotations_path, 'r') as f:
        annotations = f.read().splitlines()
    class_ids = [ann.split()[index] for ann in annotations]
    return class_ids


def get_unique_classes(labels_path, label_index):
    n_classes = dict()
    count = 0
    for i, label_path in enumerate(labels_path):
        for name in read_classids(label_path, label_index):
            if name not in n_classes.keys():
                n_classes[name] = count
                count += 1
            else:
                continue
    return n_classes


def create_logger():
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:- %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger = logging.getLogger("APT_Realignment")
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        logger.addHandler(console_handler)
    logger.propagate = False
    return logger


def class_colors(names):
    """
    Create a dict with one random BGR color for each
    class name
    """
    return {name: (
        np.random.randint(0, 255),
        np.random.randint(0, 255),
        np.random.randint(0, 255)) for name in names}


def xywh2xyxy(coordinates: list()):
    x, y, w, h = np.asarray(coordinates, dtype=np.float32)
    x1 = x - w / 2
    y1 = y - h / 2
    x2 = x + w / 2
    y2 = y + h / 2
    return [x1, y1, x2, y2]


def read_annotations(annotations_path, cls_index=-2):
    with open(annotations_path, 'r') as f:
        annotations = f.read().splitlines()
    img_annot = list()
    class_ids = list()
    for ann in annotations:
        x1, y1 = ann.split()[:2]
        x2, y2 = ann.split()[4:6]
        cls_id = ann.split()[-2]
        class_ids.append(cls_id)
        img_annot.append([int(float(x)) for x in [x1, y1, x2, y2]])
    return [img_annot, class_ids]


def plot_boxes(img, boxes, score=None, name='Object', color=(0, 255, 0)):
    line_width = max(round(sum(img.shape) / 2 * 0.003), 2)
    if score:
        w, h = \
            cv2.getTextSize("{} {:.2f}".format(name, score), 0, fontScale=line_width / 3,
                            thickness=max(line_width - 1, 1))[0]
    else:
        w, h = cv2.getTextSize("{}".format(name), 0, fontScale=line_width / 3, thickness=max(line_width - 1, 1))[0]
    x1, y1, x2, y2 = boxes
    # add a context line on bbox
    outside = y1 - h - 3 >= 0  # label fits outside box
    p2 = x1 + w, y1 - h - 3 if outside else y1 + h + 3
    img = cv2.rectangle(img, (x1, y1), p2, color, -1, cv2.LINE_AA)
    if score:
        text = "{} {:.2f}".format(name, score)
    else:
        text = "{}".format(name)
    img = cv2.putText(img, text, (x1, y1 - 2 if outside else y1 + h + 3), 0, line_width / 3, (255, 255, 255), 2,
                      lineType=cv2.LINE_AA)
    img = cv2.rectangle(img, (x1, y1), (x2, y2), color, line_width // 3, lineType=cv2.LINE_AA)
    return img
