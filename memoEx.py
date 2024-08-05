

#파일 생성하기
#open 함수에서 file mode
#w, r, a

fileName = "myMemo.txt"
fileName2 = "myMemo2.txt"
f = open(fileName,"w",encoding="utf-8")
f.write("쓰고싶은내용")
f.close()

with open(fileName2,"w",encoding="utf-8") as f:
    f.write("쓰고싶은내용22")
    

