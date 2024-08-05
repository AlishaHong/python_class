
#터미널에서 매개변수로 파일내용을 읽어오는 방법 
#매개변수로 받아온 파일의 이름을 변수에 담아서 
#해당 변수를 읽어오는 방식 

#예외처리


#readline과 readlines의 차이점 확인하기 

import sys

filename = sys.argv[1]


#예외처리
try:
    #인코딩 안됨
    f = open(filename, 'r',encoding="utf-8")
except FileNotFoundError:
    print("열고자하는 파일이 없습니다.")
    sys.exit(0)
    
print("파일을 정상적으로 읽었습니다.")


f = open(filename, 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line,end = '')
f.close()

# readline과 readlines의 차이 : 
# readline은 몇 라인인지 모르기 때문에 한줄씩 while문으로 읽고
# readlines은 처음부터 끝까지 한번 읽었기 때문에 몇라인인지 알고 있어서 for문으로 반복 가능

f = open("test.txt", 'r')
lines = f.readlines()
print("\n"+''.join(lines))

f.close()


f = open("test.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)

# print("\n"+''.join(lines))

f.close()

a = sys.argv[1]
b = sys.argv[2]

print(a,b)



#리눅스에서 파일 복사
#!ls -al
#!cp a.txt b.txt
#a.txt를 복사해서 b.txt를 만들어라