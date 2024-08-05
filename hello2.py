# from myop import adder,divider
from myop import adder,divider

if __name__ == "__main__":
    a = 10
    b = 20
    print("hello")
    print(adder(a,b))
    print(divider(a,b))    
    

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



