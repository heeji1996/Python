
# 클래스

# 절차지향
result1 = 0
result2 = 0
def add1(num):
    global result1 # 전역변수 호출
    result1 += num # 전역변수를 지역변수에 누적
    return result1

def add2(num):
    global result2 # 전역변수 호출
    result2 += num # 전역변수를 지역변수에 누적
    return result2

print(add1(3)) # result1에 누적
print(add1(4))
print(add2(3)) # result2에 누적
print(add2(7))
#-------------------------------------------

# 객체지향
# 위에 함수들을 클래스형태로 바꾸기
class Calculator:
    def __init__(self):  # 생성자
        self.result = 0  # 전역변수

    def add(self, num):  # self는 인자로 취급X
        self.result += num
        return self.result

    def sub(self,num):   # class안에서는 전역변수 앞에 self를 붙인다
        self.result -= num
        return self.result

# 클래스를 사용하려면 인스턴스화를 시킨다.
cal1 = Calculator() #__init__(self): 영역실행  /  인스턴스 생성
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(10))
print(cal2.sub(5))
#-------------------------------------------

# 인자 2개를 받아 가감승제를 하여 결과를 돌려주는(return) 계산기를 만들고 실행하기
class Calculator2:
    def __init__(self):
        self.result = 0

    def sum(self,num1,num2):
        self.result = num1 + num2
        return self.result

    def sub(self,num1,num2):
        self.result = num1 - num2
        return self.result

    def multiply(self,num1,num2):
        self.result = num1 * num2
        return self.result

    def division(self,num1,num2):
        self.result = num1 / num2
        return self.result

cal3 = Calculator2()

print(cal3.sum(10,20))
print(cal3.sub(50,20))
print(cal3.multiply(6,5))
print(cal3.division(60,2))
#-------------------------------------------

# 기존 결과에 가감승제를 하여 리턴하기
# 인자가 1개 일때나 2개일 때 동작
class Calculator3:
    def __init__(self):
        self.result = 0

    def sum(self,num, num2 = None):  # 메서드 오버로딩 개념대신 이렇게 활용가능
        if num2 == None:
            self.result += num
            return self.result
        else:
            self.result = num + num2
            return self.result

    def sub(self,num,num2 = None):  # 메서드 오버로딩 개념
        if num2 == None:
            self.result -= num
            return self.result
        else:
            self.result = num - num2
            return self.result

    def mul(self,num,num2 = None):  # 메서드 오버로딩 개념
        if num2 == None:
            self.result *= num
            return self.result
        else:
            self.result = num * num2
            return self.result

    def div(self,num,num2 = None): # 메서드 오버로딩 개념
        if num2 == None:
            self.result /= num
            return self.result
        else:
            self.result = num / num2
            return self.result

cal4 = Calculator3()

print(cal4.sum(5))
print(cal4.sub(1))
print(cal4.mul(3))
print(cal4.div(6))
#-------------------------------------------

# 변수, 함수 --> 클래스 --> 파일저장(모듈) --> 단계별 폴더저장(패키지)

# 모듈화 되었을 때 참조하는 법
from python_Ex import mycal, mod1

mc = mycal.Calculator3()  # 2순위 : 클래스가 정의 되어있다면 인스턴스화
print(mc.sum(3,4))  # 3순위 :객체.메서드, 객체.변수 등등 활용
print(mc.sub(8,4))
print(mc.mul(10,4))
print(mc.div(40,4))

type(mc)  # <class 'mycal.Calculator3'>
#-------------------------------------------

class FourCal:
    def __init__(self,first,second):  # 생성자 / 인스턴스 생성할 때 인자를 줘서 초기화한다
        self.first = first
        self.second = second

    # self 해당 인스턴스
    def setdata(self,first,second):
        self.first = first   # self.first는 전역변수가 된다
        self.second = second # self.second는 전역변수가 된다

    def div(self):  # 하위클래스의 오버라이딩에 의하여 은닉화 된다
            return self.first / self.second

# 생성자에 인자가 없는 경우
fc = FourCal() # TypeError: 생성자(__init__)의 인자가 2개가 있기 때문에 인자없이 인스턴스 생성하면 오류발생
fc.setdata(1,2)

# 생성자에 인자가 있는 경우
fc = FourCal(3,4)

print(fc.first)  # self = fc --> 즉, self.first가 출력된다.
print(fc.second)

fc2 = FourCal()
id(fc)   # 69241416  fc 와 fc2 의 id 값이 다르다
id(fc2)  # 69241608  두 인스턴스는 다른 메모리를 가르킨다.

id(fc)       # 69241416
id(fc.first) # 8791132774800
#-------------------------------------------

# 클래스의 상속
class SubFourCal(FourCal): # 상속의 표현 : SubFourCal은 FourCa를 상속받았다
    def pow(self): # 확장메소드 정의
        result = self.first ** self.second
        return result

    def div(self):  # 하위 오버라이딩 재정의
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

subCal = SubFourCal(3,4)  # 상위 클래스의 인자 2개짜리 생성자를 사용한다
subCal.pow()  # 3의 4제곱을 리턴
#-------------------------------------------

# 메서드 오버라이딩

a = SubFourCal(4,0)  # 하위 클래스에서 오버라이딩된 메소드를 호출
a.div()
#-------------------------------------------

# 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)
a = Family()
print(a.lastname)  # 김
b = Family()
print(b.lastname)  # 김

Family.lastname = "박"
print(a.lastname)  # 박
print(b.lastname)  # 박
# ===> 상기 코드에서 알 수 있는 내용은 lastname 변수는 모든 인스턴스에서 공유된다
# 자바에 비유하면 static이 붙은 클래스와 유사하다.

class MyClass:
    aaa = "aaa"   # class변수를 선언하는 위치
   #self.bbb = "bbb"  --> class변수 선언 위치에서 self를 사용할 수 없다.
   #즉, self는 자바의 this처럼 객체를 생성하기 전에 사용할 수 없다(인스턴스가 생성되고 난 후에 쓸 수 있다)
    def __init__(self,first):
        self.first = first  # 전역변수(인스턴스 변수)

print(MyClass.aaa)  # aaa

mc = MyClass(1234)
print(MyClass.first)  # Error : 호출 불가
print(mc.first)  # 1234
print(mc.aaa)  #--> 이렇게 호출하는 것은 좋지 않음 (클래스.변수)라고 부르기

mc2 = MyClass(5678)
print(mc2.first)
print(mc2.aaa)  # 비추천 --> 해당 인스턴스의 전역변수인지, 클래스변수인지 혼동될 우려가 있음
# 결론 --> 클래스변수는 (클래스.변수) 처럼 호출하기
MyClass.aaa = 'bbb'
print(mc.first)  # 1234
print(mc.aaa)  # bbb
print(mc2.first)  # 5678
print(mc2.aaa)  # bbb
#-------------------------------------------

# 모듈
# 모듈이란? 함수나 변수 또는 클래스를 모아 놓은 파일이다.

# [ mod1.py 모듈 사용하기 ]
'''
# mod1.py
def add(a,b):
    return a + b

def sub(a,b):
    return a - b
'''
# mod1.py 모듈 사용하기 1
result = mod1.add(100, 200)  # 2함수호출
print(result)
# mod1.py 모듈 사용하기 2
from python_Ex.mod1 import add # 모듈아래 함수까지 참조
result = add(300,400)
print(result)
# mod1.py 모듈 사용하기 3  복수의 함수 참조
from python_Ex.mod1 import add

result = add(300,400)
print(result)
# mod1.py 모듈 사용하기 4  모든 함수 참조
result = add(300,400)
print(result)
#-------------------------------------------

#모듈에 함수가 정의 되어있다.
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
# 모듈에 함수를 실행하는 명령이 포함되어있다.
if __name__ == "__main":
    print(add(1,4))
    print(add(4,2))
'''
 (second) C:\Users\Soldesk\PycharmProjects\first>python mod1.py
 위의 명령은 mod1.py를 직접 실행한 것임, 따라서 당연히 결과 출력되어야한다
 import mod1  <---- 실행이 아닌 모듈을 참조하겠다. 그런데 실행결과가 화면에 뜬다
 결론 : 모듈안에 실행을 참조할 때 작동하지 못하게 하려면 
 if__name__ == "__main__"을 먼저 기술하고 하단에 실행문을 적으면
 실행할 때는 실행되고, 참조할 때는 실행문이 작동하지 않는다.
'''
#-------------------------------------------
'''
# mod2.py
# 모듈 안에 class와 class변수, 메소드가 정의 되어있는 경우
PI = 3.141592  # 클래스 변수  : 모둘명.PI
class Math:
    def solv(self,r):  # 클래스 내부 메소드
        return PI * (r**2) # 면적

def add(a,b):  # 모듈 메소드  : 모둘명.메소드
    return a + b
''
[ 콘솔에서의 사용법 ]
>>> import mod2
>>> print(mod2.PI)
3.141592
>>> math=mod2.Math()
>>> print(math.solv(2))
12.566368
>>> print(mod2.add(mod2.PI,4.4))
7.5415920000000005
''
'''
# 210
import mod2
result = mod2.add(3,4)
print(result)









