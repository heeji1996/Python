
# 함수

# 함수 선언 및 정의
def add(a,b) :
    return a+b

# 호출1
result = add(10,20)
print(result)
# 호출2
print(add(30,40))
# 호출3
a=100
b=200
print(add(a,b))

# return의 활용
def say_nick(nick):
    if nick == '바보':
        return  # 바보일 때 출력 x
    print("나의 별명은 %s" %nick)

say_nick("천재")
say_nick("바보")
#-------------------------------------------

# 인자(입력값) 없는 함수
def say():
    return'Hi'
print(say())
#-------------------------------------------

# return 값이 없는 함수 : 대부분의 경우 자체 출력 명령을 포함하고 있음
def say2():
    print("Hi~~~")

# 매개변수를 지정해서 전달하기
def add(a,b):
    print("a인자는: %d" %a)
    print("b인자는: %d" %b)
add(a=10,b=20)
# 인자의 순서에 상관없이 인자를 지정할 수 있다
# 인자의 갯수가 많아 순서가 혼동될 때 사용하면 좋다
add(b=20,a=10)
#-------------------------------------------

# 인자의 갯수를 모를 때 : *변수명
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)
print(add_many(1,2,3,4,5,6,7,8,9,10)) # 인자가 여러개
#-------------------------------------------

# 인자가 리스트인 함수
def add_many2(args):
    result = 0
    for i in args:
        result = result + i
    return result

myNum = [1,2,3,4,5,6,7,8,9]
print(add_many2(myNum))
#-------------------------------------------

# 리턴이 여러개인 함수
def myMulti(a,b):
    return a+b, a*b

rt1, rt2 = myMulti(10,20)
print(rt1)
print(rt2)
# 한 꺼번에 받기
result = myMulti(3,4)
print(result)  # (7, 12)
#-------------------------------------------

# 인자가 여러개인 함수의 활용
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
             result = result + 1
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul("add", 1,2,3,4,5,6))
print(add_mul("mul", 1,2,3,4,5,6))
#-------------------------------------------

# 키워드 인자를 받는 함수 : **변수명
def print_kwargs(**kwargs):
    print(kwargs)

# 변수인자와 값을 모두 주고 호출
print_kwargs(a=1)    # {'a': 1}
print_kwargs(a=1,b=1,c='hi')  # {'a': 1, 'b': 1, 'c': 'hi'}
#-------------------------------------------

# 함수의 가인자가 초기값을 미리 가지고 있는 경우
# 기본 값을 가지고 있는 파라메터는 생략 가능
# 주의 : 기본값을 가지고 있는 파라메터는 항상 마지막에 위치 시킨다.
def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다" %name)
    print("나의 나이는 %d입니다" %old)
    # 세번째 인자가 없는 경우 디폴트값이 적용
    if man:
        print("남자")
    else:
        print("여자")

say_myself("홍길동",30)
say_myself("홍길순",24,False)
#-------------------------------------------

# 함수 안에서 선언한 변수의 효력범위
# : 함수 안에서 선언한 매개변수는 함수 밖에서는 사용x

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return사용
a = 1
def vartest(a): # 지역변수
    a = a + 1
    return a
# 전역변수 출력
a = vartest(a)
print(a)

# 2. global 명령어 사용
a = 1
def vartest(): # 전역변수
    global a
    a = a + 1
# 전역변수 출력
vartest()
print(a)
#-------------------------------------------

# lambda 함수 : 람다는 함수처럼 복잡하지 않은 간단한 처리식 일 때 사용
# 표현) lambda 인자,인자,,, : 인자처리식
# add 함수를 f람다식으로 선언 정의
add = lambda a,b : a+b
result = add(3,4)
print(result)
#-------------------------------------------


#-------------------------------------------


#-------------------------------------------