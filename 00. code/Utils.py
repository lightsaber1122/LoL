import cv2
import numpy as np
import Variables
import time

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
    image = np.fromfile(image_path, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
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
            raise ValueError("pos 입력이 잘못되었습니다.\n['top', 'jug', 'mid', 'adc', 'sup'] 중에 하나를 입력해주세요.")
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
            raise ValueError("pos 입력이 잘못되었습니다.\n['top', 'jug', 'mid', 'adc', 'sup'] 중에 하나를 입력해주세요.")
    else :
        raise ValueError("team 입력이 잘못되었습니다.\n['blue', 'red'] 중에 하나를 입력해주세요.")
    
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
            raise ValueError("pos 입력이 잘못되었습니다.\n['top', 'jug', 'mid', 'adc', 'sup'] 중에 하나를 입력해주세요.")
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
            raise ValueError("pos 입력이 잘못되었습니다.\n['top', 'jug', 'mid', 'adc', 'sup'] 중에 하나를 입력해주세요.")
    else :
        raise ValueError("team 입력이 잘못되었습니다.\n['blue', 'red'] 중에 하나를 입력해주세요.")
        

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
        raise ValueError("확장자 입력을 확인해주세요.\n지원하는 확장자 :\n\t- jpg\n\t- png")
    filename = image_file.split("/")[-1]
    image = Image.open(image_file).convert("RGB")
    image.save(save_path + filename[:-5] + extension, img_format)
    print(f"파일이 저장되었습니다.\n파일 위치 : {save_path + filename[:-5] + extension}")
    
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
    crop_img = img[y:y+h, x:x+w]
    return crop_img

def RaiseError(error_type:str, func:str or None, message:str) :
    error_list = ["AttributeError", "KeyError", "ValueError"]
    if error_type not in error_list :
        print(f"입력한 {error_type}은 Error 목록에 없습니다.")
        return
    WriteLog("e", func, f"{error_type}: {message}")

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

def WriteLog(sep:str, func:str or None, message:str) :
    """콘솔창에 로그를 출력한다.
    
    Parameters
    ----------
    sep(str)
        로그 구분자
        로그의 의미를 나타내며, 다음 종류를 입력으로 함
        - E : Error
        - W : Warning
        - I : Info
        - D : Debug
        - V : Verbose
        - wtf : Assert
    func(str or None)
        현재 로그를 표시하는 함수명
        입력값이 없을 경우 'System'으로 표기
    message(str)
        로그 내용
    
    Raise
    ----------
    ValueError
        `sep`에 해당하지 않는 문자를 입력한 경우
    """
    sep_list = ["E", "W", "I", "D", "V", "WTF"]
    if sep.upper() not in sep_list :
        raise ValueError("로그 구분자를 확인해주세요.")
    if func is None :
        func = "System"
    now = time.strftime("%y/%m/%d %X")
    print(f"[{now}] {sep.upper()}/{func} {message}")