print(3+4)
print(26500/22)

# 주석입니다.
'''
    여러 줄 주석입니다
    작은따옴표 세번 치면 만들 수 있다
    
'''

# 변수의 데이터형은 입력 값에 따라서 결정된다.
#정수
mynum = 200
younm = 300
result = mynum + younm
print(result)

# 문자열
myname = '홍길동'
yourname = '유관순'
mixname = myname + yourname
print(mixname)

mixname = myname + ' ' + yourname
print(mixname)

# 숫자 + 문자열 = 더 해지지 않는다 : TypeError: unsupported operand type(s) for +: 'int' and 'str'
mixmix = mynum + myname
print(mixmix)

