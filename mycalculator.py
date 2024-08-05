


class Calculator:
    
    
    
    #init함수의 역할
    #클래스 객체 생성 시 호출되는 함수
    def __init__(self):
        self.result = 0
        self.op1 = 0
        self.op2 = 0
        self.operation = "+"
        print("__init__이 호출되었습니다.")     
        
    
    
    #클래스의 멤버함수의 첫번째 인수는 무조건 self로 적어주자.
    #클래스 안에 멤버변수는 직접 변수값을 설정할 수 없으므로 
    #멤버 함수를 통해 값을 설정해야 한다.
    def inputValue(self,op1,op2):
        self.op1 = op1
        self.op2 = op2

        
    def add(self):
        self.result = self.op1 + self.op2
        return self.result
    
    def sub(self):
        self.result = self.op1 - self.op2
        return self.result
    
    def directadd(self,op1,op2):
        self.op1 = op1
        self.op2 = op2
        self.result = self.op1 + self.op2
        print(self.result)
        
        
        
#클래스의 객체 cal1을 생성
#생성시 __init__함수를 호출
cal1 = Calculator()
cal2 = Calculator()


cal1.inputValue(3,7)
print(cal1.op1)
result1 = cal1.add()
result2 = cal1.sub()
print(f'a = {cal1.op1}, b = {cal1.op2} / 더하기 : {result1}, 빼기 : {result2}')
cal1.directadd(2,5)



