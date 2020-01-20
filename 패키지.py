'''
[ 패키지 안의 함수 실행방법 ]
주의 : import 참조할 때는 모듈이 있는 곳까지 참조해줘야 한다.
        패키지 단계마다  __init__ 모듈를 생성해주면 작동되지만 버전3.3부터는 상관없음
       다음 예제를 실행할 때 반드시 인터프리터 종료후 실행해야한다 ( ctrl + z )

1) echo 모듈을 import하여 실행하는 방법
>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo

2) echo모듈이 있는 디렉토리까지를 from...import하여 실해하는 방법
>>> from game.sound import echo
>>> echo.echo_test
<function echo_test at 0x0000000002E3D948>
# 단순 import보다 from ~ import를 사용하면 경로를 축약해서 사용가능함

3) echo 모듈의 echo_test함수를 직접 import하여 실행
>>> from game.sound.echo import echo_test
>>> echo_test()
echo

# __init__.py 의 용도

* __all__ : sound 디렉터리에서 * 기호를 사용하여 import할 경우 이곳에 정의된 echo 모듈만 import된다는 의미
오류발생
>>> from game.sound import *
>>> echo.echo_test
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'echo' is not defined

game/sound/__init__.py 에
 __all__ = ['echo']  라 쓰면 인식이 된다
 결과
>>> from game.sound import *
>>> echo.echo_test
echo

# relative 패키지
  graphic.reder 가 ==> sound.echo를 참조
  ''
  from game.sound.echo import echo_test # 경로 축약하여 사용가능함
  # 단순 import보다 from ~ import를 사용하면 경로를 축약해서 사용가능함
  # render.py
  def render_test():
    print("render")
    echo_test # 바로참조가 가능 
  ''
>>> from game.graphic.render import render_test
>>> render_test()
render
echo

''
# 상대적 표현 참조
from ..sound.echo import echo_test
# render.py
def render_test():
    print("render")
    echo_test()
''
>>> from game.graphic.render import render_test
>>> render_test()
render
echo





'''