
# for문

test_list = ['one', 'two', 'three']
for i in test_list:  # test_list 요소가 i에 대입
    print(i)
#-------------------------------------------

# 리스트의 튜플
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:  # 리스트 안의 튜플 대입
    print(first + last)
#-------------------------------------------

# 학생점수 합겹/불합격 보기
marks = [90, 25, 67, 45, 80]  # 학생들 점수
number = 0  # 학생에게 붙여줄 번호
for mark in marks: # marks 요소를 mark에 순서대로 대입
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다" % number)
    else:
        print("%d번 학생은 불합격입니다" % number)
#-------------------------------------------

# continue : for문 맨 처음으로 돌아가기
marks = [90, 25,67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 합격입니다" % number)
#-------------------------------------------

# range()함수 : 숫자 리스트 자동으로 만들어주는 함수
# range(시작숫자, 끝숫자) 끝 숫자는 포함X
a = range(10) # 0 ~ 9
a  # range(0, 10)

# 예
marks = [90, 25,67, 45, 80]
for number in range(len(marks)): # range(0,5) 0 ~ 4
    if marks[number] < 60: continue
    print("%d번 학생 합격입니다" % (number+1))
#-------------------------------------------

# range를 사용한 구구단
for i in range(2,10): # 2 ~ 9
    for j in range(1,10): # 1 ~ 9
        print(i*j, end=" ")  # end = " " 그 줄에 계속 출력하기 위함
    print(' ')
#-------------------------------------------

# 리스트 내포1
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)  # [3, 6, 9, 12]

# 리스트 내포2
a = [1,2,3,4]
result = [num*3 for num in a] # a리스트 요소를 하나씩 num에 담고 num*3해서 result에 담기
print(result)  # [3, 6, 9, 12]

# 리스트 내포3
a = [1,2,3,4]
result = [num*3 for num in a if num % 2 == 0] # a리스트 요소를 하나씩 num에 담고 num이 짝수이면 num*3해서 result에 담기
print(result)   # [6, 12]
#-------------------------------------------

# 리스트와 range() 구구단
result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)