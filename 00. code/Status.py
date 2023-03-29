import cv2
import numpy as np
from tqdm import tqdm
from Utils import CheckRectPosition, ImageCrop
from Variables import status_window_rect

def CheckStatusWindowPosition(image_path:str, color:tuple, thickness:int=2) -> None :
    """상태창 구역이 제대로 설정되었는지 확인한다.
    
    Parameters
    ----------
    image_path(str)
        이미지 파일 이름을 포함한 전체 경로
    color(tuple)
        사각형 색상
        (B, G, R) 순으로 색상값(0-255) 입력
    thickness(int)
        사각형의 두께 (default 2)
        -1로 설정할 경우, 색상이 채워진 사각형 출력
        
    Return
    ----------
    None
    """
    CheckRectPosition(image_path, status_window_rect, color, thickness)
    
def SaveStatusWindowInVideo(video_path:str, save_path:str, freq:int=1) -> None :
    """동영상에서 상태창을 추출해 저장한다.
    
    Parameters
    ----------
    video_path(str)
        동영상 파일 이름을 포함한 전체 경로
    save_path(str)
        추출한 이미지를 저장할 경로 (파일 이름 제외)
    freq(int)
        상태창을 추출할 주기 (단위 : 초)
        (default 1)
    
    Return
    ----------
    None
    """
    video = cv2.VideoCapture(video_path)
    count = 0
    
    if video.isOpened() :
        fps = int(video.get(cv2.CAP_PROP_FPS))
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        f_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"영상 속성\n\t- fps: {fps}\n\t- size: ({width} X {height})\n\t- time: {divmod((f_count//fps), 60)[0]} : {divmod((f_count//fps), 60)[1]}")
    else :
        raise KeyError(f"비디오 파일을 찾을 수 없습니다. 파일을 확인해주세요.\n{video_path}")
    
    for i in tqdm(range(f_count)) :
        if video.isOpened() :
            _, frame = video.read()
            try :
                status = ImageCrop(frame, status_window_rect)
                cv2.imshow("frame", frame)
                cv2.imshow("status", status)
                k = cv2.waitKey(fps)
                if(int(video.get(1)) % fps * freq == 0) :
                    cv2.imwrite(save_path + f"{str(count).zfill(4)}.jpg", status)
                    count += 1
                if k == 27 :
                    break
            except AttributeError :
                break
    video.release()
    cv2.destroyAllWindows()