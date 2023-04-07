# -*- coding: utf-8 -*-
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
import cv2
import inspect
filename = inspect.getfile(inspect.currentframe())
import json
from Log import Log
log = Log(filename)
import numpy as np
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
            decode = json.loads(line)
            try :
                image = np.fromfile(decode["file"], np.uint8)
                image = cv2.imdecode(image, cv2.IMREAD_COLOR)
                image = cv2.resize(image, (22, 22))
                image = np.float32(image) / 255.0
                label = np.int32(decode["label"])
                yield image, label
            except FileNotFoundError :
                log.exception("DataGenerator", FileNotFoundError, f"{decode['file']}에서 이미지를 불러올 수 없습니다.")
                return

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
    cv2.namedWindow("image")
    while True :
        print(label)
        cv2.imshow("image", np.uint8(image * 255))
        k = cv2.waitKey(0)
        if k == ord('d') :
            image, label = next(iters)
        elif k == 27 :
            break
    cv2.destroyAllWindows()

def buildModel(input_dim:tuple, n_class:int, summary:bool = False) -> tf.keras.models.Model :
    """모델을 생성한다.
    
    Parameters
    ----------
    input_dim(tuple)
        모델의 입력 크기
    n_class(int)
        분류할 클래스 갯수
    summary(bool)
        모델 정보를 요약한 log를 띄울 것인지 선택
    
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
    if summary == True :
        log.model("buildModel", model.summary())
    return model

def Train(path:str, input_dims:tuple, n_class:int, batch:int, epoch:int, save_path:str, verbose:int = 0, summary:bool = False) -> None :
    """모델을 학습한다.
    
    Parameters
    ----------
    path(str)
        json 파일 이름을 포함한 전체 경로
    input_dim(tuple)
        모델의 입력 크기
    n_class(int)
        분류할 클래스 갯수
    batch(int)
        데이터의 batch
    epoch(int)
        모델의 훈련 횟수
    save_path(str)
        모델을 저장할 전체 경로
    verbose(int)
        현재 상태를 확인하기 위한 log 정보 단계
        (default 0)
        - 0 : None
        - 1 : 자세히
        - 2 : 간략히
    summary(bool)
        모델 정보를 요약한 log를 띄울 것인지 선택
    
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
        log.v("Train", f"\t- model input : {input_dims}")
        log.v("Train", f"\t- model output : {n_class}")
    elif verbose == 2 :
        log.v("Train", f"\t- model input : {input_dims}")
        log.v("Train", f"\t- model output : {n_class}")
    
    train_dataset = tf.data.Dataset.from_generator(DataGenerator, (tf.float32, tf.int32),
                                                   (tf.TensorShape([input_dims[0], input_dims[1], input_dims[2]])), (tf.TensorShape([])),
                                                    args = (path, ))
    train_dataset = train_dataset.batch(batch)
    train_dataset = train_dataset.shuffle(batch)
    
    if verbose >= 1 :
        log.v("Train", "데이터셋이 생성되었습니다.")
        
    model = buildModel(input_dims, n_class, summary)
    if verbose >= 1 :
        log.v("Train", "모델이 생성되었습니다.")

    if verbose == 1 :
        log.v("Train", "모델을 컴파일 합니다. optimizer = 'adam', loss = 'SparseCategoricalCrossentropy'")
    model.compile(optimizer = "adam", loss = "SparseCategoricalCrossentropy", metrics = ["accuracy"])
    
    if verbose >= 1 :
        log.v("Train", "모델 훈련을 시작합니다.")
    model.fit(train_dataset, epochs = epoch)
    if verbose >= 1 :
        log.v("Train", "모델 훈련이 완료되었습니다.")
    model.save(save_path + "Status_classification")
    log.i("Train", f"모델이 저장되었습니다. {save_path}Champion_classification")