# ; 1. 람다함수 : 간단하게 함수로 구현할 수 있는 방법
# ; plus_ten = lambda x : x + 10 

# ; def plus_ten(x):
# ;      return x+10


# ; 2. 프로세스에서 인수값을 전달받는 방법
# ; import sys 
# ; python main.py test 123
# ; sys.argv[0] ==> main.py
# ; sys.argv[1] ==> test  데이터 타입 문자열
# ; sys.argv[2] ==> 123  데이터 타입 문자열

# ; python main.py "test 123"(홑따옴표는 안됨)



# ; 3. if __name__ == '__main__':
# ; 현재 파일을 직접 실행하는 조건에서 실행되는 부분

# ; def test1():
# ;    return a+b

# ; def test2():
# ;    return a-b

# ; #암시적으로 main()을 인식하고 실행한다.
# ; test1()
# ; test2()


# ; def main()
# ; if __name__ ="__main__":

# ; 함수가 직접 실행 될때만 실행됨
# ; 예를들어 add함수를 가진 파이썬 파일을  import 할때 
# ; 함수만 가져와서 쓰고 싶으면 실행될 문장들은 메인함수에 넣으면 import해서 해당 함수만 불러올 수 있다! 

# ; 다시 정리하면 main함수는 해당 파일이 직접 실행될 때만 실행된다. 

# 4. 예외처리
# 5. 클래스 
# 6. 디버깅
