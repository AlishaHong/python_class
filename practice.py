# [실습2] myeditor.py 프로그램 작성
# python myeditor.py 실행시 파일명을 아래 문자열을
# 저장할 파일명 : [파일명 입력]
# [저장할 내용 입력]
import os

fileNames = os.listdir()
print(fileNames)

# import sys

# filename = sys.argv[1]

# f = open(filename, 'w', encoding="utf-8")
# f.write('''
# import os

# fileNames = os.listdir()
# print(fileNames) 
# ''')
# f.close()

# f = open(filename, 'r', encoding="utf-8")
# fileContent = f.readlines()
# print(fileContent)
# f.close()
