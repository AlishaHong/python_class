# from myop import adder,divider
from myop import adder,divider

if __name__ == "__main__":
    a = 10
    b = 20
    print("hello")
    print(adder(a,b))
    print(divider(a,b))    
    
# 파일이 실행되자마자 실행되는 main 함수! 
# 일반 함수는 실행되지 않는다.

import sys

if __name__ == '__main__':
    print(sys.argv[0]) # main.py
    print(sys.argv[1]) # a
    print(sys.argv[2]) # b
    
    

if __name__ == '__main__':
    result = sys.argv[1]+sys.argv[2] 
    print(type(result))
    print(type(sys.argv[1]))
    print(result)


# [실습1] myadder.py 프로그램 작성
# 1. python myadder.py [시작값] [ 종료값]
# ex) python myadder.py 1 10  -> 1~10까지 더하기, 그리고 결과값 출력

# [실습2] myeditor.py 프로그램 작성
# python myeditor.py 실행시 파일명을 아래 문자열을
# 저장할 파일명 : [파일명 입력]
# [저장할 내용 입력]
# import os

# fileNames = os.listdir()
# print(fileNames)


