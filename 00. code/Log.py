# -*- coding: utf-8 -*-
from datetime import datetime
import os
os.system('color')
from termcolor import colored

class Log() :
    def __init__(self, filename:str or None) :
        super(Log, self).__init__(filename)
        self.attributes = ["bold", "dark", "underline", "blink", "reverse", "concealed"]
        if filename is None :
            self.filename = "System"
        else :
            self.filename = filename.split("\\")[-1]
        
    def time(self) -> str :
        now = datetime.now()
        return f"{now.year}-{str(now.month).zfill(2)}-{str(now.day).zfill(2)} {str(now.hour).zfill(2)}:{str(now.minute).zfill(2)}:{str(now.second).zfill(2)}.{str(now.microsecond)[:3]}"
    
    def e(self, TAG:str, message:str, **kwargs) -> None :
        """ERROR에 대한 log를 표시한다.
        
        Paramters
        ----------
        TAG(str)
            현재 위치 및 함수명 등 발생 위치를 특정할 수 있는 태그
        message(str)
            오류에 대한 상세 내용
        """
        if kwargs is not None :
            for key, value in kwargs.items() :
                if key == "filename" :
                    print(colored(f"{self.time()} {value} E/{TAG}: {message}", "red", "on_white", attrs = [self.attributes[0]]))
        else :
            print(colored(f"{self.time()} {self.filename} E/{TAG}: {message}", "red", "on_white", attrs = [self.attributes[0]]))
        
    def w(self, TAG:str, message:str) -> None :
        """WARNING에 대한 log를 표시한다.
        
        Parameters
        ----------
        TAG(str)
            현재 위치 및 함수명 등 발생 위치를 특정할 수 있는 태그
        message(str)
            경고에 대한 상세 내용
        """
        print(colored(f"{self.time()} {self.filename} W/{TAG}: {message}", "red", attrs = ["bold"]))
        
    def i(self, TAG:str, message:str) -> None :
        """INFO에 대한 log를 표시한다.
        
        Paramters
        ----------
        TAG(str)
            현재 위치 및 함수명 등 발생 위치를 특정할 수 있는 태그
        message(str)
            정보에 대한 상세 내용
        """
        print(colored(f"{self.time()} {self.filename} I/{TAG}: {message}", "yellow", attrs = ["bold"]))
    
    def d(self, TAG:str, message:str) -> None :
        """DEBUG에 대한 log를 표시한다.
        
        Parameters
        ----------
        TAG(str)
            현재 위치 및 함수명 등 발생 위치를 특정할 수 있는 태그
        message(str)
            디버깅 상세 내용
        """
        print(colored(f"{self.time()} {self.filename} D/{TAG}: {message}", attrs = ["bold"]))
        
    def v(self, TAG:str, message:str) -> None :
        """VERBOSE에 대한 log를 표시한다.
        
        Parameters
        ----------
        TAG(str)
            현재 위치 및 함수명 등 발생 위치를 특정할 수 있는 태그
        message(str)
            상세 정보 내용
        """
        print(colored(f"{self.time()} {self.filename} V/{TAG}: {message}", "green", attrs = ["bold"]))
    
    def wtf(self, TAG:str, message:str) -> None :
        """ASSERT에 대한 log를 표시한다.
        
        Note
        ----------
        매우 심각한 수준의 오류에만 사용
        
        Parameters
        ----------
        TAG(str)
            현재 위치 및 함수명 등 발생 위치를 특정할 수 있는 태그
        message(str)
            오류에 대한 상세 내용
        """
        print(colored(f"{self.time()} {self.filename} E/{TAG}: {message}", "white", "on_red", attrs = ["bold"]))
        
    def exception(self, TAG:str, error:type, error_message:str) -> None :
        """정의된 log에 따라 오류를 표시한다.
        
        Note
        ----------
        except Error as e :
            Log.exception(TAG, Error, e)
        
        Parameters
        ----------
        TAG(str)
            현재 위치 및 함수명 등 발생 위치를 특정할 수 있는 태그
        error(type)
            예외처리를 할 오류의 종류
        error_message(str)
            오류 문구
        """
        Exceptions = [KeyError, ValueError, IndexError, SyntaxError, NameError, ZeroDivisionError,
                      FileNotFoundError, TypeError, AttributeError, ConnectionError]
        if error in Exceptions :
            self.e(TAG, f"[{error.__name__}] {error_message}")
        else :
            self.e(TAG, f"[ValueError] {error}는 정의되어있지 않습니다.", filename = "Log")
            
    def model(self, TAG:str, summary:str) -> None :
        """모델 정보를 요약하고, log로 표시한다.
        
        Parameters
        ----------
        TAG(str)
            현재 위치 및 함수명 등 발생 위치를 특정할 수 있는 태그
        summary(str)
            tensorflow에서 반환된 모델의 요약 정보
        """
        self.i(TAG, summary)