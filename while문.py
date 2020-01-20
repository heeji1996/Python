
#  While 문

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit ==10:
        print("나무 넘어갑니다.")
#-------------------------------------------

prompt = """ 
1. ADD
2. Del
3. List
4. Quit
Enter number : """

number = 0
while number != 4: # 4 입력 시 while문 종료
    print(prompt)
    number = int(input()) # int(input()) : 사용자의 숫자입력
#-------------------------------------------

# break문 : While문 빠져나가기
# 커피자판기 1
coffee = 10
money = 300
while money: # 무한루프
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다" % coffee)
    if coffee ==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

 # 커피자판기2
 coffee = 10
 while True:
     money = int(input("돈을 넣어주세요: ")) # int(input()) : 사용자의 숫자입력
     if money == 300:
         print("커피를 줍니다")
         coffee = coffee - 1
     elif money > 300:
         coffee = coffee - 1
         print("거스름돈 %d를 주고 커피를 줍니다." % (money-300))
         print("남은 커피의 양은 %d개입니다." % coffee)
     else:
         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
         print("남은 커피의 양은 %d개입니다." % coffee)

     if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
#-------------------------------------------

# continue : while문의 맨 처음으로 돌아가게 하는 명령
# 홀수출력
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
#-------------------------------------------

# 무한루프 : 무한히 반복
# Ctrl + c 를 눌러야 while문을 탈출할 수 있다.
while True:
    print("Ctrl+c를 눌러야 while문을 빠져나올 수 있습니다")


