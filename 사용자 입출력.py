
# 1. 콘솔로 입력받기
a = input()
a

# 2. 기본 메시지가 있는 input('메시지')
number = input('숫자를 입력하세요')
print(number)


#-------------------------------------------

# 1.print함수의 여러가지 모습
# : 자바의 메소드 오버로딩과 비슷함
a = 123
print(a)
b = 'Hello'
print(b)
c = [1,2,3]
print(c)
#
print("Hi""My""Friend")  # HiMyFriend
print("Hi"+"My"+"Friend")  # HiMyFriend
print("Hi","My","Friend")  # Hi My Friend

for i in range(10):
    print(i, end=' ')

#-------------------------------------------

# 파일 읽고 쓰기
# 파일을 열 때 'w'옵션을 주면 기존의 내용이 삭제된다.
# 기존의 내용을 유지하려면 'a' 옵션을 줘야한다.

# 쓰기
f = open("../새파일.txt", 'w')  # 쓰기모드로 열기 / w(쓰기) r(읽기) a(추가)
f.close()

f = open("D:\\파일쓰기.txt",'w')
for i in range(1,11):
    data = "%d번째 줄 입니다 \n" % i
    print(data)
    f.write()
f.close()

# 읽기1
f = open('D:\\파일쓰기.txt', 'r')
while True:
    line = f.readline() # 한줄 씩 읽기
    if not line: break # 읽을 것이 없으면 빠져나오기
    print(line)
f.close()

# 읽기2
f = open('D:\\파일쓰기.txt', 'r')
lines = f.readlines() # 모든 줄 읽기
for line in lines:
    print(line)
f.close()

# 읽기3
f = open('D:\\파일쓰기.txt', 'r')
line = f.read() # 모든 줄 읽기
print(line)
f.close()
#-------------------------------------------

# add 데이터 : 파일에 새로운 내용추가
f = open('D:\\파일쓰기.txt','a')
for i in range(1,11):
    data = "%d번째 줄입니다" %i
    f.write(data)
f.close()
#-------------------------------------------

# with 문장
# 파일처리 문장에서 open하면 반드시 close 해야한다.
# whit는 블럭이 끝날 때 자동으로 close해준다.

#기본
f = open("foo.txt",'w')
f.write("Life is too short, you need python")
f.close()
# with 문장으로
with open("foo.txt",'w') as f :
    f.write("Life is too short, you need python")
# f는 with 영역을 빠져 나오면 자동 close된다
#-------------------------------------------

# sys1.py
# sys 모듈 : 매개변수를 직접받아 사용하기

import sys  # 외부모듈을 사용하려면 import 해야한다.
args = sys.argv[1:]   # 프로그램을 실행하면 주어진 인자들 받아서
for i in args:  # [1:] 파일명을 제외한 두번째 인자부터 저장한다
    print(i)
'''
(second) C:\Users\Soldesk\PycharmProjects\first>python sys1.py aaa bbb ccc
aaa
bbb
ccc
'''