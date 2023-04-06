# -*- coding: utf-8 -*-
import cv2
import inspect
filename = inspect.getfile(inspect.currentframe())
import json
from Log import Log
log = Log(filename)
import numpy as np
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf

def DataGenerator(path:str) -> tuple :
    """json 파일을 읽어 훈련 데이터를 생성한다.
    
    Parameter
    ----------
    path(str)
        json 파일 이름을 포함한 전체 경로
        
    Yields
    ----------
    image(np.ndarray)
        normalized된 이미지
        np.float32
    label(np.ndarray)
        이미지의 라벨
        np.int32
    """
    with open(path, "r", encoding = "UTF-8") as f :
        while True :
            line = f.readline()
            if line == "" : break
            line = json.loads(line)
            image = np.fromfile(line["file"], np.uint8)
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            image = np.float32(image) / 255.0
            label = np.int32(line["label"])
            if label == 0 :
                for i in range(2) :
                    yield image, label
            else :
                yield image, label

def buildModel(input_dim:tuple, n_class:int) -> tf.keras.models.Model :
    """모델을 생성한다.
    
    Parameters
    ----------
    input_dim(tuple)
        모델의 입력 크기
    n_class(int)
        분류할 클래스 갯수
    
    Return
    ----------
    model(tf.keras.models.Model)
        분류기 모델
    """
    x = tf.keras.Input(shape = input_dim)
    y = tf.keras.layers.Flatten()(x)
    y = tf.keras.layers.Dense(512, activation = "relu")(y)
    y = tf.keras.layers.Dropout(0.2)(y)
    y = tf.keras.layers.Dense(n_class, activation = "softmax")(y)
    
    model = tf.keras.models.Model(inputs = x, outputs = y)
    model.summary()
    return model

def testGenerator(path:str) -> None :
    """DataGenerator에서 올바른 데이터가 출력되는지 확인한다.
    
    Parameter
    ----------
    path(str)
        json 파일 이름을 포함한 전체 경로
        
    Return
    ----------
    None
    """
    iters = iter(DataGenerator(path))
    image, label = next(iters)
    while True :
        image = np.uint8(image * 255)
        cv2.imshow("image", image)
        print(label)
        k = cv2.waitKey(0)
        if k == ord('d') :
            image, label = next(iters)
        elif k == 27 :
            break
    cv2.destroyAllWindows()
    
def Train(path:str, save_path:str, batch:int, input_dim:tuple, n_class:int, epoch:int, verbose:int = 0) -> None :
    """모델을 학습한다.
    
    Parameters
    ----------
    path(str)
        json 파일 이름을 포함한 전체 경로
    save_path(str)
        모델을 저장할 전체 경로
    batch(int)
        데이터의 batch
    input_dim(tuple)
        모델의 입력 크기
    n_class(int)
        분류할 클래스 갯수
    epoch(int)
        모델의 훈련 횟수
    verbose(int)
        현재 상태를 확인하기 위한 log 정보 단계
        (default 0)
        - 0 : None
        - 1 : 자세히
        - 2 : 간략히
    
    Return
    ----------
    None
    """
    if verbose > 2 :
        log.e("Train", "인수 verbose에는 [0, 1, 2]만 입력할 수 있습니다.")
        return
    log.i("Train", f"데이터 : {path}")
    if verbose == 1 :
        log.v("Train", f"\t- epoch : {epoch}")
        log.v("Train", f"\t- batch : {batch}")
        log.v("Train", f"\t- model input : {input_dim}")
        log.v("Train", f"\t- model output : {n_class}")
    elif verbose == 2 :
        log.v("Train", f"\t- model input : {input_dim}")
        log.v("Train", f"\t- model output : {n_class}")
        
    train_data = tf.data.Dataset.from_generator(DataGenerator, (tf.float32, tf.int32),
                                                (tf.TensorShape([input_dim[0], input_dim[1], input_dim[2]]), tf.TensorShape([])),
                                                args = (path, ))
    train_data = train_data.batch(batch)
    train_data = train_data.shuffle(batch)
    if verbose >= 1 :
        log.v("Train", "데이터셋이 생성되었습니다.")
    
    model = buildModel(input_dim, n_class)
    if verbose >= 1 :
        log.v("Train", "모델이 생성되었습니다.")
    if n_class == 2 :
        if verbose == 1 :
            log.v("Train", "모델을 컴파일 합니다. optimizer = 'adam', loss = 'BinaryCrossentropy'")
        model.compile(optimizer = "adam", loss = "BinaryCrossentropy", metrics = ["accuracy"])
    else :
        if verbose == 1 :
            log.v("Train", "모델을 컴파일 합니다. optimizer = 'adam', loss = 'SparseCategoricalCrossentropy'")
        model.compile(optimizer = "adam", loss = "SparseCategoricalCrossentropy", metrics = ["accuracy"])
    
    if verbose >= 1 :
        log.v("Train", "모델 훈련을 시작합니다.")
    model.fit(train_data, epochs = epoch)
    if verbose >= 1 :
        log.v("Train", "모델 훈련이 완료되었습니다.")
    model.save(save_path + "Status_classification")
    log.i("Train", f"모델이 저장되었습니다. {save_path}Status_classification")