# 반복문

## for와 range
'''
* 반복문 : 특정한 규칙에 맞춰서 특정한 코드를 반복적으로 실행.
# for ... in : 반복문을 위한 문법
for 변수명 in range(횟수): # range 안에 (in) 있는 요소들을 '변수명'으로 하나씩 꺼내와서 들여쓰기 안에 사용해주겠다.
    반복할 코드 (들여쓰기)
'''
for i in range(10): # 0~9
    print("자니? ",  i) # range에서 요소들을 하나씩 꺼내서 1에 넣고 사용.
    # 인덱스 0 ~ N-1 : 총 반복되는 홋수 -> 꺼내서 사용하는 횟수

'''
반복문의 변수 i: 루프 인덱스 -> loop index -> i
'''

# for in + range 반복
# range의 특성?: range(끝점), range(시작점, 끝점), range(start, stop, step)
# for 변수명(i) in range(시작점, 끝점):
#     반복할 코드
# 5붙터 10까지 합해주는 코드
a = 0
for i in range(5, 11):
    print(i) # 5~10 <- 순서대로 대입
    a += i # a= a + i
    print(i, a)
print("sum = ", a)

a = 0
for i in range(5, 11):
    # print(i) # 5~10 <- 순서대로 대입
    if i % 2: # if i % 2 == 1:
        a += i
    #print(i, a)
print("홀수합 = ", a)

# 증가폭
# for i in range(0,10,2):
for i in range(1, 10, 2):
    print(i)

# 뒤집기
for i in range(9, 0, -1):
    print(i)







