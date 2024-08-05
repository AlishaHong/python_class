#디버깅
#함수가 실행되는 시간을 계산해보자!
#time 


#시간,수학라이브러리 호출
import time
import math

#일반함수 실행 시간

result = 0
def plus_ten(x):
    return x + 10

startTime = time.time()
for i in range(1000000):
    result += plus_ten(i)
endTime = time.time()

print(f'plus_ten : {endTime - startTime:.5f}sec')


result2 = 0
#람다함수 실행시간
lambda_result = lambda x : x + 10
startTime2 = time.time()
for i in range(1000000):
    result2 += lambda_result(i)
endTime2 = time.time()

print(f'lambda_result : {endTime2 - startTime2:.5f}sec')


# time.sleep(10)    # 테스트를 위해 임의의 sec(초) 입력 
# math.factorial(100000)
# 지금은 별 차이가 없지만 람다함수가 훨씬 빠른 상황이나 시점이 있다.





import time

start = time.time()
time.sleep(10)
end = time.time()

print(f"{end - start:.5f} sec")