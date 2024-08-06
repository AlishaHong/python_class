# [실습1] myadder.py 프로그램 작성
# 1. python myadder.py [시작값] [ 종료값]
# ex) python myadder.py 1 10  -> 1~10까지 더하기, 그리고 결과값 출력

import sys
# def myadder(a,b):
#     sum = 0
#     for i in range(a,b+1):
#         sum += i
#     return sum
        
# if __name__ == '__main__':
#     print(myadder(int(sys.argv[1]), int(sys.argv[2])))
    
    
    
if __name__ == '__main__':
    result = 0
    start = int(sys.argv[1])
    end = int(sys.argv[2])


    for i in range(start, end+1):
        result += i
    
    print(f'{start}에서 {end}까지의 result : {result}')
    
