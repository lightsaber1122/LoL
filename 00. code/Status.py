import cv2
import inspect
filename = inspect.getfile(inspect.currentframe())
import numpy as np
from Log import Log
log = Log(filename)
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
    
def SaveStatusWindowInVideo(video_path:str, save_path:str, freq:int=1, verbose:int = 0) -> None :
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
    verbose(int)
        현재 상태를 확인하기 위한 log 정보 단계
        (default 0)
        - 0 : None
        - 1 : 자세히
        - 2 : 간략히
    
    Raise
    ----------
    ValueError
        verbose에 3 이상의 숫자가 입력된 경우
    ValueError
        비디오 파일을 찾을 수 없는 경우
    
    Return
    ----------
    None
    """
    TAG = "SaveStatusWindowInVideo"
    if verbose > 2 :
        log.e(TAG, "인수 verbose에는 [0, 1, 2]만 입력할 수 있습니다.")
    video = cv2.VideoCapture(video_path)
    if verbose == 1 or verbose == 2 :
        log.v(TAG, f"영상 : {video_path}")
    count = 0
    
    if verbose == 1 :
        if video.isOpened() :
            fps = int(video.get(cv2.CAP_PROP_FPS))
            log.i(TAG, f"\t- fps : {fps}")
            width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            log.v(TAG, f"\t- screen : {width} X {height}")
            f_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            times = divmod(f_count//fps, 60)
            hour = 0
            minute = times[0]
            second = times[1]
            if times[0] > 59 :
                hour, minute = divmod(times[0], 60)
            log.v(TAG, f"\t- length : {str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}")
            
        else :
            return
    
    if verbose == 1 or verbose == 2 :
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
                        if verbose == 1 :
                            if count == 0 :
                                log.v(TAG, f"\n캡처본이 저장되었습니다. {save_path}{str(count).zfill(4)}.jpg")
                            else :
                                log.v(TAG, f"캡처본이 저장되었습니다. {save_path}{str(count).zfill(4)}.jpg")
                        count += 1
                    if k == 27 :
                        log.v(TAG, f"작업이 중단되었습니다. 마지막으로 저장된 파일 : {save_path}{str(count).zfill(4)}.jpg")
                        break
                except AttributeError :
                    log.v(TAG, "작업이 완료되었습니다.")
                    break
    else :
        for i in range(f_count) :
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