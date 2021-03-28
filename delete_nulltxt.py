import os
import numpy as np

txtpath = '/home/yi/Downloads/YOLOv3-model-pruning-master/delete_null/test/'
imagepath = '/home/yi/Downloads/YOLOv3-model-pruning-master/delete_null/image/'
for txt in os.listdir(txtpath):

    with open(txtpath+txt, "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        box = data.replace('\n', '').split(' ')
        len1 = len(box)
        if len1<=1:
            img_path = imagepath+txt.replace(".txt", ".jpg")
            if os._exists(imagepath):
                img_path = imagepath + txt.replace(".txt", ".png")
            os.remove(img_path)

