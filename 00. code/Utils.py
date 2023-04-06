import cv2
import inspect
filename = inspect.getfile(inspect.currentframe())
from Log import Log
log = Log(filename)
import numpy as np
from termcolor import colored
import Variables

def CheckRectPosition(image_path:str, rect:tuple or list, color:tuple, thickness:int=2) -> None :
    """이미지 상에서의 구역 위치를 확인한다.
    
    Parameters
    ----------
    image_path(str)
        원본 이미지
    rect(tuple or list)
        확인할 구역
    color(tuple)
        화면에 표시될 사각형 색상
        (B, G, R) 순으로 색상값(0-255) 입력
    thickness(int)
        사각형의 두께 (default 2)
        -1로 설정할 경우, 색상이 채워진 사각형 출력
        
    Return
    ----------
    None
    """
    try :
        image = np.fromfile(image_path, np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    except FileNotFoundError :
        log.exception("CheckRectPosition", FileNotFoundError, f"{image_path}에서 파일을 불러올 수 없습니다.")
    
    while True :
        image = DrawRect(image, rect, color, thickness)
        cv2.imshow("image", image)
        k = cv2.waitKey(0)
        if k == 27 :
            break
    cv2.destroyAllWindows()

def DrawRect(image:np.ndarray, rect:tuple or list, color:tuple, thickness:int=2) -> np.ndarray :
    """이미지에 사각형을 그린다.
    
    Paramters
    ----------
    image(np.ndarray)
        원본 이미지
    rect(tuple or list)
        사각형을 그리고자 하는 영역
        (x, y, w, h) 형태
    color(tuple)
        사각형의 색상
        (B, G, R) 순으로 색상값(0-255) 입력
    thickness(int)
        사각형의 두께 (default 2)
        -1로 설정할 경우, 색상이 채워진 사각형 출력
    
    Return
    ----------
    img(np.ndarray)
        사각형이 그려진 이미지
    """
    img = image.copy()
    x, y, w, h = rect[0], rect[1], rect[2], rect[3]
    img = cv2.rectangle(img, tuple((int(x), int(y))), tuple((int(x+w), int(y+h))), color, thickness)
    return img

def getChampRect(team:str, pos:str) -> tuple :
    """현재 팀과 라인의 챔피언 이미지를 얻기 위한 영역을 구한다.
    
    Parameters
    ----------
    team(str)
        현재 팀 (blue/red)
    pos(str)
        현재 라인 (top/jug/mid/adc/sup)
    
    Raises
    ----------
    ValueError
        팀이 잘못 입력된 경우
    ValueError
        라인이 잘못 입력된 경우
    
    Return
    ----------
    champ_rect(tuple)
        챔피언 이미지가 위치한 영역
    """
    blue_champ_rect = Variables.champion_rect_blue
    red_champ_rect = Variables.champion_rect_red
    if team == "blue" or team == "b" :
        if pos == "top" or pos == "t" :
            return blue_champ_rect[0]
        elif pos == "jug" or pos == "j" :
            return blue_champ_rect[1]
        elif pos == "mid" or pos == "m" :
            return blue_champ_rect[2]
        elif pos == "adc" or pos == "a" :
            return blue_champ_rect[3]
        elif pos == "sup" or pos == "s" :
            return blue_champ_rect[4]
        else :
            log.exception("getChampRect", ValueError, "pos 입력이 잘못되었습니다.")
    elif team == "red" or team == "r" :
        if pos == "top" or pos == "t" :
            return red_champ_rect[0]
        elif pos == "jug" or pos == "j" :
            return red_champ_rect[1]
        elif pos == "mid" or pos == "m" :
            return red_champ_rect[2]
        elif pos == "adc" or pos == "a" :
            return red_champ_rect[3]
        elif pos == "sup" or pos == "s" :
            return red_champ_rect[4]
        else :
            log.exception("getChampRect", ValueError, "pos 입력이 잘못되었습니다.")
    else :
        log.exception("getChampRect", ValueError, "team 입력이 잘못되었습니다.")
    
def getCSRect(team:str, pos:str) -> tuple :
    """현재 팀과 라인의 CS 갯수를 얻기 위한 영역을 구한다.
    
    Parameters
    ----------
    team(str)
        현재 팀 (blue/red)
    pos(str)
        현재 라인 (top/jug/mid/adc/sup)
    
    Raises
    ----------
    ValueError
        팀이 잘못 입력된 경우
    ValueError
        라인이 잘못 입력된 경우
    
    Return
    ----------
    cs_rect(tuple)
        CS가 위치한 영역
    """
    blue_cs_rect = Variables.cs_rect_blue
    red_cs_rect = Variables.cs_rect_red
    if team == "blue" or team == "b" :
        if pos == "top" or pos == "t" :
            return blue_cs_rect[0]
        elif pos == "jug" or pos == "j" :
            return blue_cs_rect[1]
        elif pos == "mid" or pos == "m" :
            return blue_cs_rect[2]
        elif pos == "adc" or pos == "a" :
            return blue_cs_rect[3]
        elif pos == "sup" or pos == "s" :
            return blue_cs_rect[4]
        else :
            log.exception("getCSRect", ValueError, "pos 입력이 잘못되었습니다.")
    elif team == "red" or team == "r" :
        if pos == "top" or pos == "t" :
            return red_cs_rect[0]
        elif pos == "jug" or pos == "j" :
            return red_cs_rect[1]
        elif pos == "mid" or pos == "m" :
            return red_cs_rect[2]
        elif pos == "adc" or pos == "a" :
            return red_cs_rect[3]
        elif pos == "sup" or pos == "s" :
            return red_cs_rect[4]
        else :
            log.exception("getCSRect", ValueError, "pos 입력이 잘못되었습니다.")
    else :
        log.exception("getCSRect", ValueError, "team 입력이 잘못되었습니다.")

def ImageConvert(image_file:str, save_path:str, extension:str="jpg") -> None :
    """WEBP 형식의 이미지를 변환한다.

    Parameters
    ----------
    image_file(str)
        WEBP 이미지 경로 및 파일 이름
    save_path(str)
        저장 경로 (파일 이름 제외)
    extension(str)
        변환하고자 하는 파일 형식
        - jpg
        - png

    Raise
    ----------
    ValueError
        extension에 지원되지 않는 형식을 입력한 경우
    """
    from PIL import Image
    img_format = ""
    if extension == "jpg" or extension == ".jpg" :
        extension = ".jpg"
        img_format = "jpeg"
    elif extension == "png" or extension == ".png" :
        extension = ".png"
        img_format = "png"
    else :
        log.exception("ImageConvert", ValueError, "확장자 입력을 확인해주세요.")
    file = image_file.split("/")[-1]
    try :
        image = Image.open(image_file).convert("RGB")
    except FileNotFoundError :
        log.exception("ImageConvert", FileNotFoundError, f"{image_file}을 불러올 수 없습니다.")
    image.save(save_path + file[:-5] + extension, img_format)
    log.i(f"파일이 저장되었습니다. {save_path + file[:-5] + extension}")
    
def ImageCrop(image:np.ndarray, rect:tuple or list) -> np.ndarray :
    """이미지의 원하는 영역을 추출한다.
    
    Parameters
    ----------
    image(np.ndarray)
        자르고자 하는 원본 이미지
    rect(tuple or list)
        이미지에서 자르고자 하는 영역
        (x, y, w, h) 형태
    
    Return
    ----------
    crop_img(np.ndarray)
        추출된 영역의 이미지
    """
    img = image.copy()
    x, y, w, h = rect[0], rect[1], rect[2], rect[3]
    try :
        crop_img = img[y:y+h, x:x+w]
    except cv2.error :
        log.exception("ImageCrop", IndexError, f"{rect}에 맞추어 이미지를 crop할 수 없습니다.")
    return crop_img

def ToInputImage(image:np.ndarray) -> np.ndarray :
    """이미지를 모델에 입력할 수 있도록 변경한다.
    
    Parameter
    ----------
    image(np.ndarray)
        모델에 입력할 이미지
    
    Return
    ----------
    img(np.ndarray)
        모델에 맞게 변경된 이미지
    """
    img = image.copy()
    img = np.float32(img) / 255.0
    img = np.expand_dims(img, axis = 0)
    return img