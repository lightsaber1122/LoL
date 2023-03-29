import cv2
import numpy as np

def CheckRectPosition(image_path:str, rect:tuple or list, color:tuple, thickness:int) -> None :
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