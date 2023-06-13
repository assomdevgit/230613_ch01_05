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
# for i in range(1, 10, -1): # range(1, 10, -1) -> 빈 range. -> 음수 증가폭 -> 시작점 > 종료점
for i in range(9, 0, -1):
    print(i)

# reversed() -> 시퀀스형태의 자료형을 뒤집어주는 기술
'''
- for 변수 in reversed(range(횟수))
'''
for i in reversed(range(10)):
    print(i, end = '')
print()
for i in range(10)[::-1]:
    print(i, end = '')
print()
for i in range(10):
    print(9-i, end = '')
print()

# 시퀀스 객체로 반복하기 (리스트, 튜플, 문자열...)
a = ["아무1", "아무2", "아무3"]
for v in a: # value -> v
    print(v)

fruits = ["banana", "orange", "mango"]
for fruit in fruits: # 리스트, 튜플 -> 시퀀스 (복수형) => for를 통해서 반복 호출하는 변수명 -> 단수
    print(fruit)

text = "작은 것들을 위한 시"
for c in text:
    print(c)

for c in reversed(text):
    print(c)

for c in text[::-1]:
    print(c)

# 인덱스를 사용한 조회
for i in range(len(text)):
    # -> texxt[i] : 반복문으로 조회를 하면...--> 요소 하나하나를 검색.
    print(i, text[i])

for t in text: # 시퀀스 안에 있는 요소들을 하나씩 호출해서 출력한 코드
    print(t)

for i in range(len(text))[::-1]:
    # -> texxt[i] : 반복문으로 조회를 하면...--> 요소 하나하나를 검색.
    print(i, text[i])

for t in text[::-1]:  # 시퀀스 안에 있는 요소들을 하나씩 호출해서 출력한 코드
    print(t)

# enumerate - 인덱스, 값 -> 튜플상을 만들어주는 함수
for i in enumerate(fruits):
    a, b = i # 튜플 -> 왼쪽에 자리수를 맞춰서 변수를 둬서 해체 => 튜플 언팩킹
    print(i) # (인덱스, 요소의 값)
    print("a", a, "b", b)

for i, v in enumerate(fruits): # for에서부터 언팩킹으로 할당이 가능.
    print("i", i, "v", v)
















