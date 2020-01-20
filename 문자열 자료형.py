# 큰따옴표(") : 문자열 안에 작은따옴표(')가 있을 경우 사용
mystr = "Python's favorite food is pelr"
print(mystr)

# 작은따옴표(') : 문자열 안에 큰따옴표(")가 있을 경우 사용
mystr1 = 'Python"s favorite food is pelr'
print(mystr1)

# 큰따옴표 3개 (""") : 멀티라인 일때 사용
mystr = """
'동해물'과
백두산이
마르고
닳도록
"""
print(mystr)

# 작은따옴표 3개 (''') : 멀티라인 일때 사용
mystr = '''
"동해물"과
백두산이
마르고
닳도록
'''
print(mystr)

# [ 문자열 연산 ]
# 더하기
head = "Python"
tail = "is fun!"
head + tail

# 곱하기
a = "홍길동"
print(a*5)

print("="*50)
print("My Program")
print("="*50)

# 문자열 길이 구하기
a = "Life is too short"
len(a) # 17

# [ 인덱싱 / 슬라이싱 ]
# 파이썬은 0부터 센다
# 마이너스(-) : 문자열 뒤에서부터 센다. (-1부터 시작)
# 문자열 인덱싱 : 무엇인가를 '가르킨다' : 한 글자
a = "Life is too short, you need Python"
print(a[0])  # 'L'
print(a[12]) # 's'
print(a[-1]) # 'n'
print(a[-5]) # 'y'

# 문자열 슬라이싱 : 무엇인가를 '잘라낸다' : 연속 글자
# a[시작번호:끝 번호] --> 끝 번호는 포함되지 않음
a = "Life is too short, you need Python"
print(a[0] + a[1] + a[2] + a[3]) # Life
print(a[0:4])  # 'Life'
print(a[0:3])  # 'Lif'  : 끝 번호는 포함되지 않음
print(a[0:5])  # 'Life '
print(a[19:])  # 끝 번호 생략 시 문자열 끝까지  출력 : 'you need Python'
print(a[:17])  # 시작번호 생략 시 처음부터 출력 : 'Life is too short'
print(a[:])  # 시작번호, 끝번호 생략 시 처음부터 끝까지 출력
print(a[19:-7])  # 'you need'
# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)  # 20010331
print(weather)  # Rainy
# 문자열 Pithon을 Python으로 바꾸기
a = "Pithon"
a[1] = 'y' # 오류발생 : 문자열 요솟값은 바꿀 수 있는 값이 아니다. (immutable한 자료형)
new_a = a[:1] + 'y' + a[2:]  # 슬라이싱 기법으로 잘라내어 새로운 값을 추가해준다.
print(new_a)  # Python


# 문자열 포매팅 : 문자열 안의 특정 값을 바꿔야 할 경우 / 문자열 안에 어떤 값을 삽입하는 방법
# 1.숫자 바로 대입 : %d
print("I eat %d apples." %3)  # I eat 3 apples.

# 2.문자열 바로 대입 : %s , 문자열 따옴표로 감싸기
print("I eat %s apples." %"five")  # I eat five apples.

# 3.숫자값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." %number)  # I eat 3 apples.

# 4.2개 이상의 값 넣기 : %(값 , 값 , ...)
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number,day))

''' < 문자열 포맷코드 >
%s : 문자열  --> 어떠한 형태의 값이든 문자열로 변환해 넣을 수 있다.
%c : 문자 1개
%d : 정수
%f : 부동 소수
%o : 8진수
%x : 16진수
%% : '%'기호자체
'''
print("Error is %d%%." %98)  # %기호를 사용하려면 똑같이 뒤에 '%%' 쓰기 : Error is 98%.

# 포맷코드와 숫자함께 사용
# 1.정렬과 공백
print("%10s" %"hi") # 길이가 10개인 문자열 공간에서 대입되는 값 오른쪽 정렬 후 나머지 공백채우기 : '        hi'
print("%-10sjane" %"hi") # 마이너스(-)왼쪽 정렬 후 공백채우기 : 'hi        jane'
# 2.소수점 표현
print("%0.4f" %3.42134234)  # 소수점 4번째 자리까지만 출력 : '3.4213'
print("%10.4f" %3.42134234) # '    3.4213'
print("%3.4f" %123546766666684.9344412435) # 넘을 때는 소숫점 이하만 제한

# 포맷함수(format)를 사용한 포매팅 : {0} .format( )
# 1.숫자 바로 대입
print("I eat {0} apples." .format(3)) # I eat 3 apples.

# 2.문자열 바로 대입
print("I eat {0} apples" .format("five"))  # I eat five apples

# 3.2개이상 값 넣기 : {0} {1} --> format()함수에 들어있는 순서대로 인덱스 번호가 작용
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days." .format(number,day)) # I ate 10 apples. so I was sick for three days.

# 4.이름으로 넣기 : 지역변수를 이용한 대입은 {변수명}처럼 기술한다.
print("I ate {number} apples. so I was sick for {day} days." .format(number=10, day=3))  #

# 5.인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I sick for {day} days." .format(10, day=3))

# 6.정렬
print("'{0:<10}'" .format("hi")) # 왼쪽정렬 (:<10) : 'hi        '
print("'{0:>10}'" .format("hi")) # 오른쪽정렬 (:>10) : '        hi'
print("'{0:^10}'" .format("hi")) # 가운데정렬 (:^10) : '    hi    '

# 7.공백채우기
print("{0:=^10}" .format("hi")) # 가운데 정렬, 빈공간 '='로 채우기 : ====hi====
print("{0:!<10}" .format("hi")) # 왼쪽 정렬, 빈공간 '!'로 채우기 : hi!!!!!!!!

# 8.소수점 표현하기
y = 3.42134234
print("{0:0.4f}" .format(y))  # 소수점 4번째 자리까지 출력 : 3.4213
print("'{0:10.4f}'" .format(y))  # '    3.4213'

# 9.{ 또는 } 문자 표현하기
print("{{ and }}".format())  # { and }

# 10. f 문자열 포매팅 : 문자열 앞에 f접두사 붙이기 (python 3.6부터 가능)
name = "홍길동"
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.") # 나의 이름은 홍길동입니다. 나이는 30입니다.
print(f"나는 내년이면 {age+1}살이 된다") # 표현식도 사용 가능하다 : 나는 내년이면 31살이 된다

d = {'name':'홍길동', 'age':'30'} # 딕셔너리 문자배열로 하여 사용하기
print(f'나의 이름음 {d["name"]}입니다. 나이는 {d["age"]}입니다.')


# 문자열 관련 함수
# count : 문자 개수 세기
str = "welcome to my python"
str.count('o')  # str문자열 안에 o가 몇번 사용되었는가 : 3

# find : 위치 알려주기
str.find('o') # o의 맨 처음 위치를 알려줌 : 4
str.find('z') # 찾는 값이 없으면 -1 반환 : -1

# index : 위치 알려주기
str.index('o') # o의 맨 처음 위치를 알려줌 : 4
str.index('z') # 찾는 값이 없으면 오류발생

# join : 문자열 삽입 --> 리스트나 튜플에서도 사용가능
# 토큰(분리된 가장 작은 단위)을 만드는 문자 삽입
print(",".join("abcdefg")) # a,b,c,d,e,f,g
print(",".join(['a','b','c','d','e']))  # a,b,c,d,e 배열 --> 토큰형태의 문자열

# upper : 소문자를 대문자로 바꾸기
a = "hi"
print(a.upper())  # HI

# lower : 대문자를 소문자로 바꾸기
a = "HI"
print(a.lower())  # hi

# lstrip : 공백제거
a = "   hi   "
print(a.lstrip())  # hi
# rstrip : 오른쪽 공백 제거
# strip : 양쪽 공백 제거

# replace : 문자열 바꾸기 ( 바뀌게 될 문자열, 바꿀 문자열)
a = "Life is too short"
print(a.replace("Life", "Your leg"))  # Your leg is too short

# split : 문자열 나누기
a = "Life is too short"
print(a.split())  # 공백 기준으로 나누기 : ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
print(b.split(':'))  # ':' 기준으로 나누기['a', 'b', 'c', 'd']
# 리스트 : ['a', 'b', 'c', 'd', 'e', 'f']
# 튜플 : t3 = (1, 2, 3)
# 딕셔너리 : dir = {'name':'pay', 'phone':'010234', 'birth':'1112'} key,value형태
# 집합 : {1, 2, 3, 4, 5, 6}





