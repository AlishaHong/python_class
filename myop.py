def adder(a,b):
    return a+b

def divider(a,b):
    return a/b

if __name__ == '__main__':
    print(adder(10,10),divider(10,10))


# 메인함수에 넣지 않으면 다른 파일에서 이 파일을 호출했을때 print가 바로 실행되어 버린다.
# print(adder(10,10),divider(10,10))
