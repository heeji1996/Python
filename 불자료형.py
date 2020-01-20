
# 불 자료형 : 참(TRUE) 과 거짓(FALSE) 나타내는 자료형
a = True
b = False

# 데이터형을 판별
type(a)  # <class 'bool'>

# True / False 판별하기
1 == 1  # True
2 > 1  # True
2 < 1  # False

# bool() : 참/거짓을 판별하는 함수
# 리스트,  튜플, 집합, 딕셔너리 모두 비어있으면 False, 요소가 존재하면 TRUE
bool('python')  # True
bool("")  # False
bool(([1,2,3])) # True
bool([])  # False
bool(0)  # False
bool(None)  # False

# 참,거짓으로 while문 실행하기
a = [1,2,3,4,5]
while a:     # a가 참인 동안
    a.pop()  # 리스트의 마지막 요소를 하나씩 꺼낸다
print(a)  # [1, 2, 3, 4, 5]

# 참,거짓으로 if문 실행하기
if []:  # 만약에 []가 참이면
    print("참 : 요소가 있습니다")
else:   # 만약 []가 거짓이면
    print("거짓 : 비었습니다")
#거짓 : 비었습니다
if [1,2,3]:  # 만약에 []가 참이면
    print("참 : 요소가 있습니다")
else:  # 만약 []가 거짓이면
    print("거짓 : 비었습니다")
# 참 : 요소가 있습니다











