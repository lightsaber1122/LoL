# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
from Utils import ToInputImage
import Variables

def testModel(image_path:str, model_path:str) -> None :
    image_index = 0
    image_files = os.listdir(image_path)
    
    model = tf.keras.models.load_model(model_path)
    
    while True :
        image = np.fromfile(image_path + image_files[image_index], np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        if image.shape[:2] != Variables.status_window_size :
            image = cv2.resize(image, (Variables.status_window_size[1], Variables.status_window_size[0]))
        
        img = ToInputImage(image)
        label = np.argmax(model(img).numpy())
        
        cv2.imshow("image", image)
        print(label)
        k = cv2.waitKey(0)
        if k == ord('d') :
            if image_index == len(image_files) - 1 :
                break
            else :
                image_index += 1
        elif k == 27 :
            break
    cv2.destroyAllWindows()