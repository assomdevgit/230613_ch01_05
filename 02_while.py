# while문
# 조건문 + 반복문
# -> 조건식을 만족시키는 (True) 동안에 계속적으로 반복하는 코드
'''
while 조건식: # 조건식이 불변이면? -> 계속 만족시킨다. -> 계속 반복됨.
    실행할 코드 *
    변화식 *
'''

money = 1000
# 100원씩 쓰다가, 0원이 되면 더 이상 스지 못하는.
while money > 0:
    print(money)
    money -= 100 # 100을 차감하고 그 값을 대입(변화식)
print("돈 다씀")
"""
while 반복문의 실행 과정입니다. 먼저 초기식부터 시작하여 조건식을 판별합니다.
이때 조건식이 참(True)이면 반복할 코드와 변화식을 함께 수행합니다.
그리고 다시 조건식을 판별하여 참(True)이면 코드를 계속 반복하고,
거짓(False)이면 반복문을 끝낸 뒤 다음 코드를 실행합니다.
여기서는 조건식 → 반복할 코드 및 변화식 → 조건식으로 순환하는 부분이 루프(loop)입니다.
"""

"""
초기식 (변수에 값을 저장)
while 조건식 (변수의 현재 상황을 감시):
    1. 반복할 코드(...)
    2. 변화식 (초기식에 넣은 변수를 변화)
"""

w = 0
while w < 100:
    print("반복~반복~", w)
    w += 2
    print("변화가 발생", w)
print("while에 종속되지 않는 코드")
# 자주 쓰이는 형태는 아님...왜? for문이 더 쉬우니까...
# 반복회수가 정해져있거나, 구조가 명확한 경우

## 반복 횟수가 정해져있지 않은 경우 (while)

# random 모듈
import random # random 기능을 가져오겠다.
# 무작위의 수나 조합들을 가져오는(만둘어주는) 기능

print(random.random()) # 0 ~ 1 사이의 숫자
# random.randint(a, b) : a와 b 사이의 정수를 1개 호출 (a와 b 둘다 포함)
print(random.randint(1, 6))

w = 0
while w != 3:
    w = random.randint(1, 6)
    print(str(w) + "가 나왔습니다.")

# 무한루프
# while True: # while 1
#     print("헤헤헤헤")
# break, continue
'''
break는 for와 while 문법에서 제어흐름을 벗어나기 위해 사용합니다.
즉, 루프를 완전히 중단하죠. continue는 break와 비슷하지만 약간 다른 점이 있습니다.
break는 제어흐름을 중단하고 빠져 나오지만,
continue는 제어흐름(반복)을 유지한 상태에서 코드의 실행만 건너뛰는 역할을 합니다.
마치 카드 게임을 할 때 패가 안 좋으면 판을 포기하고 다음 기회를 노리는 것과 비슷합니다.

* break: 제어흐름 중단
* continue: 제어흐름 유지, 코드 실행만 건너뜀
'''

# break -> 반복문 정지

i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        break
# 반복문 안에서 break를 실행하면 반복문은 바로 끝난다

# for -> break
for i in range(10):
    print("for:", i)
    if i % 5:
        break

# continue - 코드 실행 건너뛰기

## for - continue
for i in range(1, 100):
    # 2의 배수는 print 하고 싶지 않아
    if i % 3 != 0: # if not i % 2:
        continue
    print(i)

actors = ["송강호", "송중기", "백윤식"]
for a in actors:
    # 소씨 배우만 print할래
    if a[0] == "송":
        # print(a)
        continue
    print(a)

# while 문 - continue
w = 0
while w != 3:
    w = random.randint(1, 6)
    if w == 6:
        continue
    print(str(w) + "가 나왔습니다!")





# n = int(input())
# for i in range(1,10):
#     print(str(n) + " * " + str(i) + " = " + str(n*i))


# while True:
#     A, B = map(int, input().split())
#     if A == 0 and B == 0:
#         break
#     print(A+B)



a = 5500
b = divmod(a, 5500)
print (b)






