import cv2
import numpy as np

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
    KeyError
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
        raise KeyError("확장자 입력을 확인해주세요.\n지원하는 확장자 :\n\t- jpg\n\t- png")
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