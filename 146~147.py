# Q1. # 결과 : shirt
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt") # shirt
elif "need" in a: print("need")
else: print("none")


# Q2. # 결과 : i % 3 == 0:
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)  # 166833


# Q3. # 결과 : i > 5 :  ,  ("*"*(i-1))
i = 0
while True:
    i += 1
    if i > 5 :break
    print("*"*(i-1))
'''
*
**
***
****
'''


# Q4. 결과 : range(1,101):
for i in range(1,101):
    print(i) # 1 부터 100세기


# Q5. 결과 : total += score  ,  total / len(A)
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)  # 79.0


#Q6. 결과 : [n*2 for n in numbers if n % 2 == 1]
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

# 리스트 내포 하기
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)  # [2, 6, 10]