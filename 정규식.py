
import re

data = '''
park 800905-1049118
kim 700905-1059119
'''


#1. 정규식으로 풀기

pat = re.compile("(\d{6})[-](\d{7})")
print(pat.sub("\g<1>-*******",data))



#2. 문자열 replace로 풀기 
#분리된 문자열이었다면 원소하나씩 돌면서 수정 도전했을텐데.. 
a = data.find('-')
print(a)

data2 = data.replace(data[data.find('-') + 1:],'*')
print(data2)




# [] -> 문자클래스
# [abc] 와 "a","before","dude"
# "a"는 정규식과 일치하는 문자인 a가 있으므로 매치 
# "before"도 b가 있으므로 매치
# "dude"는 하나도 포함하지 않으므로 매치되지 않는다.a


# [-] 
# [a-c] = [abc]


#[a-zA-Z] 모든 알파벳 
#[0-9] 모든 숫자

#^ NOT의 의미 





