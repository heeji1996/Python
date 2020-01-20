
# 파이썬에서 들여쓰기는 블럭의 개념이다.
# 조건문 다음에는 콜론(:) 잊지말기

#-------------------------------------------
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")
# 택시를 타고 가라

# 비교연산자 : >  <  == !=  >=  <=
# and , or , not

#-------------------------------------------
money = 2000
card = True
if money >= 3000 or card:  # money가 3000이상이거나 card가 있다면
    print("택시를 타고 가야지")
else:
    print("걸어가야지")
# 택시를 타고 가야지

#-------------------------------------------
# x in s(리스트,튜플,문자열)  : x가 s 안에 있는가?
# x not in s(리스트,튜플,문자열)   : x가 s 안에 없는가?
1 in [1,2,3]  # True
1 not in [1,2,3]  # False

pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
# 택시를 타고가라

#-------------------------------------------
# pass : 조건문에서 아무 일도 하지 않게 설정
pocket = ['paper','cellphone','money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

#-------------------------------------------
# elif : 다양한 조건 판단
# 상황에 따라 여러번 중첩될 수 있다
pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:  # card가 True면 실행
    print("택시를 타라")
else:
    print("걸어가라")
# 택시를 타라

#-------------------------------------------
# 조건부 표현식
score = 80
message = ""
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)  # 'success'

# 간단하게 표현하기
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
message = "success" if score >= 60 else "failure"
print(message) # 'success'












































