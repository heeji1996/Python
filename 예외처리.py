
# 예외처리

# 아래 명령을 실해하면 예외발생
f = open("없는파일.txt",'r')
'''
Traceback (most recent call last):
  File "<input>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '없는파일.txt'
'''

# 상기 명령을 실행하면 예외발생
4/0
'''
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ZeroDivisionError: division by zero
'''

# [ 오류 예외처리 기법 ]
'''
  try:
      처리문 ~~~
  except [발생오류[as 오류메세지 변수]]:
'''
# 1)예외처리 1 try ~ except
try:
    4/0
except ZeroDivisionError as e:
    print(e)  # division by zero

# 2)예외처리 2 try ~ finally
f = open("foo.txt",'w')
try:
    print("파일 저장 실행")
finally:  # 예외 발생 상과없이 무조건 실행되는 블럭
    f.close()  # 자동으로 파일 닫는다

# 예외처리 3 다중처리
'''
try:
    ...
except 발생 오류 1:
    ...
except 발생 오류 2:
    ...
'''
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except IndexError:
    print("인덱싱 할 수 없습니다")
# 결과 : 인덱싱 할 수 없습니다 --> 한개만 처리 되었다,
#  --> 한개만 처리 되었다,
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError,IndexError) as e:
    print(e)
#-------------------------------------------

# [ 오류 회피하기 ]
try:
    f = open("나없는파일.txt",'r')
except FileNotFoundError:
    pass  # 예외가 발생해도 통과 시키기
#-------------------------------------------

# [ 오류 일부러 발생시키기 ]
# raise 명령어를 사용하면 오류 강제 발생시킨다
# Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle() # 인스턴스 생성
eagle.fly() # 상속 받은 메서드를 호출
# fly() 메서드가 싱핼되다 예외가 발생

class Bird:
    def fly(self):
        print("bird~~~")

class Eagle(Bird):
    pass

eagle = Eagle()  # 인스턴스 생성
eagle.fly()  # 상속 받은 메서드를 호출
# bird~~가 출력된다

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle = Eagle()  # 인스턴스 생성
eagle.fly()  # very fast 출력
# 이 경우는 하위클래스의 인스턴스 이므로 하위 구현된 fly() 실행되고
# 호출되고 상위 fly()는 은닉화 되므로 정상 실행된다.
#-------------------------------------------

# [ 사용자 정의의 예외처리 ]
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()  # 예외발생할 때 사용자정의 예외처리 클래스 호출
    print(nick)

say_nick("천사")
say_nick("바보")
'''
say_nick("천사")
천사
say_nick("바보")
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 4, in say_nick
NameError: name 'MyError' is not defined
# 천사 출력 후 MyError 발생
'''

# 예외처리 1
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다")
'''
실행결과 :
천사
허용되지 않는 별명입니다
'''

# 예외처리 2
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다"
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)  # 변경전 클래스 때: 내용이 없음 --> 내용을 출력하려면 MyError에 함수 __str__(self)를 정의해준다
'''
실행결과 :
천사
허용되지 않는 별명입니다
'''


