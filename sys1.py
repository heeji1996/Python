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

