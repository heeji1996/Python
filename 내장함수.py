
# 내장함수

# abs : 절대값을 돌려주는 함수
abs(3)  # 3
abs(-3) # 3

# all(x) : x가 모두 참이면 True, 거짓이 하나라도 있으면 False
all([1,2,3])  # True
all(([1,2,3,0]))  # False

# any(x) : x중 하나라도 참이면 True, 모두 거짓이면 False
any([1,2,3,0])  # True
any([0,""])  # False

# chr : 아스키코드 문자를 출력
chr(97)  # 'a'
chr(48)  # '0'

# dir : 내장 변수나 함수를 보여준다
dir([1,2,3])
dir()

# divmod(a,b) : a / b 로 나눈 몫과 나머지를 튜플형으로 반환
divmod(7,3)  # (2,1) 몫은 2, 나머지는 3

# enumerate : 열거형, 순서가 있는 자료형을 입력받아 인덱스값을 포함하는 enumerate객체를 돌려준다
for i, name, in enumerate(['body', 'foo', 'bar']):
    print(i, name)
'''
0 body
1 foo
2 bar
'''

# eval(expressioin) : 실행 가능한 문자열을 입력받아 실행결과 값 반환
eval('1+2')  # 3
eval("'hi' + 'a'")  # 'hia'
eval('divmod(4,3)')  # (1, 1)

# filter
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result
print(positive([1,-3,2,0,-5,6]))  # [1, 2, 6]

# 위으 ㅣ코드를 더 간단하게 : lambda
list(filter(lambda x: x>0,[1,-3,2,0,-5,6]))  # [1, 2, 6]

# hex(x) : 16진수로 반환
hex(234)  # '0xea'

# id : 객체의 고유주소 값 반환
a = 3
id(3) # 8791332659664
id(a) # 8791332659664

# input() : 콘솔 입력값 받기

# int() : 정수로 캐스팅
# int('값',진수) : 진수 ==> 10진수로
int('11',2)  # 3
int('1A',16) # 26

# isinstance(객체,클래스) : 인스턴스가 해당 클래스의 인스턴스인지 판단, 참일경우 True
class Person:
    pass # 내용이 없는 클래스입니다

a = Person() # 인스턴스 생성
b = 3
isinstance(a,Person)  # a가 Person클래스의 인스턴스인지 확인 : True
isinstance(b,Person)  # False

# len(s) : s의 길이의 갯수 반환
len("python") # 6
len([1,2,3])  # 3

# list(s) : s를 입력받아 리스트로 만들어 반환
list("pyrhon") # ['p', 'y', 'r', 'h', 'o', 'n']

# map(함수, 반복자료) : 자료의 갯수만큼 함수 실행 후 그 결과를 묶어서 반환
# 본래 코드
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return  result

result = two_times([1,2,3,4])
print(result)  # [2, 4, 6, 8]
# map함수 이용
def two_times(x): return x*2
list(map(two_times, [1,2,3,4])) # [2, 4, 6, 8]
# map과 lambda함수 이용
list(map(lambda a: a*2, [1,2,3,4]))  # [2, 4, 6, 8]

# max() : 최댓값
max([1,2,3]) # 3

# min() : 최솟값
min([1,2,3]) # 1

# oct() : 8진수 반환
oct(34) # '0o42'
oct(12345) # '0o30071'

# open(파일이름, [읽기방법]) : 파일객체 반환 / 읽기방법 생략 시 기본값 r

# ord(c) : 문자의 아스키코드 값 반환
ord('a')  # 97
ord('0')  # 48

# pow(x,y) : x의 y제곱 결과 값 반환
pow(2,4)  # 16

# range([start],stop,[step]) :
list(range(5))  # [0, 1, 2, 3, 4]
list(range(5,10))  # [5, 6, 7, 8, 9]
list(range(1,10,2))  # [1, 3, 5, 7, 9]

# round(숫자,[소수점자리])  : 반올림
round(4.6)  # 5
round(5.678,2)  # 5.68

# sorted() : 입력값을 정렬 후 리스트 형태로 반환
sorted([3,1,2])  # [1, 2, 3]
sorted(['a','c','b'])  # ['a', 'b', 'c']
sorted("zero")  # ['e', 'o', 'r', 'z']
sorted((3,2,1))  # [1, 2, 3]

# str() : 문자열로 반환
str(3)  # '3'
str('hi'.upper())  # 'HI'

# sum() : 입력받은 리스트나, 튜플의 모든 요소의 합 반환
sum([1,2,3])  # 6
sum((4,5,6))  # 15

# tuple() : 튜플형태로 반환
tuple("abc")  # ('a', 'b', 'c')
tuple([1,2,3])  # (1, 2, 3)

# type() : 입력값의 자료형 반환
type("abc")  # <class 'str'>
type([])  # <class 'list'>

# zip() : 동일한 개수로 이루어진 자료형을 묶어주는 역할
list(zip([1,2,3], [4,5,6]))  # [(1, 4), (2, 5), (3, 6)]
list(zip([1,2,3], [4,5,6], [7,8,9]))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]














