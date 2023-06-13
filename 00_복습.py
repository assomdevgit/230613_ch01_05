# 시퀀스 자료형
"""
우리가 지금까지 사용했던 리스트, 튜플, range, 문자열을 잘 보면 공통점이 있습니다. 이들 모두 값이 연속적(sequence)으로 이어져 있다는 점입니다.

파이썬에서는 리스트, 튜플, range, 문자열처럼 값이 연속적으로 이어진 자료형을 시퀀스 자료형(sequence types)라고 부릅니다.

## 시퀀스 자료형의 공통 기능 사용하기

### 특정 값이 있는지 확인하기
먼저 시퀀스 객체 안에 특정 값이 있는지 확인하는 방법부터 알아보겠습니다. 다음은 리스트 a에서 30과 100이 있는지 확인합니다.

* `값 in 시퀀스객체`
"""

a = [30, 100]
print("30 in a : ", 30 in a)
print("50 in a : ", 50 in a)



"""시퀀스 객체에 in 연산자를 사용했을 때 특정 값이 있으면 True, 없으면 False가 나옵니다. 따라서 리스트 a에 30이 있으므로 True, 100이 없으므로 False가 나옵니다.

반대로 in 앞에 not을 붙이면 특정 값이 없는지 확인합니다.

* `값 not in 시퀀스객체`
"""
print("50 not in a : ", 50 not in a)
print("not 50 in a : ", not 50 in a)
print("30 not in a : ", 30 not in a)




"""이렇게 not in은 특정 값이 없으면 True, 있으면 False가 나옵니다.

물론 튜플, range, 문자열도 같은 방법으로 활용할 수 있습니다.
"""
text = "마제소바"
print("'마' in text :", "마" in text)
print("'마제' in text :", "마제" in text)







"""### 시퀀스 객체 연결하기

시퀀스 객체는 + 연산자를 사용하여 객체를 서로 연결하여 새 객체를 만들 수 있습니다.

* `시퀀스객체1 + 시퀀스객체2`
"""
fruits = ["apple", "banana", "cherry"]
fruits2 = ["grape", "kiwi", "lemon"]
print ("fruits + fruits2", fruits + fruits2)

# 이때는 range를 리스트 또는 튜플로 만들어서 연결하면 됩니다.
print(list(range(5,12)) + list(range(10,15)))

# 문자열은 + 연산자로 여러 문자열을 연결할 수 있습니다.

"""### 문자열에 숫자 연결하기"""



"""문자열에 정수를 연결하려고 하면 에러가 발생합니다(정수를 문자열로 변환할 수 없어서 TypeError가 발생합니다). 이 문제를 해결하려면 str을 사용하여 숫자(정수, 실수)를 문자열로 변환하면 됩니다.

* `'문자열' + str(정수)`
* `'문자열' + str(실수)`

"""
print("저는 오늘부터 " + str(20) + "살 입니다.")



"""### 시퀀스 객체 반복하기

이번에는 시퀀스 객체를 반복하는 방법입니다. `*` 연산자는 시퀀스 객체를 특정 횟수만큼 반복하여 새 시퀀스 객체를 만듭니다(0 또는 음수를 곱하면 빈 객체가 나오며 실수는 곱할 수 없습니다).

* `시퀀스객체 * 정수`
* `정수 * 시퀀스객체`
"""
l = [10, 20, 30]
print(l + l + l)
print(l * 3)


# 앞에서 range는 + 연산자로 객체를 연결할 수 없었죠? 마찬가지로 range는 * 연산자를 사용하여 반복할 수 없습니다.

# 이때는 range를 리스트 또는 튜플로 만들어서 반복하면 됩니다.
print(list(range(3, 5)) * 3)


# 문자열은 * 연산자를 사용하여 반복할 수 있습니다.

"""## 시퀀스 객체의 요소 개수 구하기

시퀀스 객체에는 요소가 여러 개 들어있죠? 이 요소의 개수(길이)를 구할 때는 len 함수를 사용합니다(len은 길이를 뜻하는 length에서 따왔습니다).

* `len(시퀀스객체)`

### 리스트와 튜플의 요소 개수 구하기
"""
l = [10, 20, 30, 40, 50]
print("len(l) :", len(l))
t = (10, 20, 30, 40, 50)
print("len(t) :", len(t))




"""### range의 숫자 생성 개수 구하기"""

# range에 len 함수를 사용하면 숫자가 생성되는 개수를 구합니다.
r = range(7, 792, 15)
print ("len(r) :", len(r))
"""### 문자열의 길이 구하기"""

# 문자열도 시퀀스 자료형이므로 len 함수를 사용하면 됩니다.
s = "Hello, world!"
print("len(s) :", len(s))
"""여기서 문자열의 길이는 공백까지 포함합니다. 단, 문자열을 묶은 따옴표는 제외합니다. 이 따옴표는 문자열을 표현하는 문법일 뿐 문자열 길이에는 포함되지 않습니다(문자열 안에 포함된 작은따옴표, 큰따옴표는 포함됨)."""

# 한글 문자열의 길이도 len으로 구하면 됩니다.

"""인덱스 사용하기

이번에는 시퀀스 객체에 들어있는 요소에 접근하는 방법을 알아보겠습니다. 시퀀스 객체의 각 요소는 순서가 정해져 있으며, 이 순서를 인덱스라고 부릅니다.

다음과 같이 시퀀스 객체에 `[ ](대괄호)`를 붙이고 [ ] 안에 각 요소의 인덱스를 지정하면 해당 요소에 접근할 수 있습니다.
"""

l = list(range(1, 11))
print (l)
print("l[3]:", l[3])


"""인덱스(index, 색인)는 위치 값을 뜻하는데 국어사전 옆면에 ㄱ, ㄴ, ㄷ으로 표시해 놓은 것과 비슷합니다. 여기서 주의할 점은 시퀀스 객체의 인덱스는 항상 0부터 시작한다는 점입니다(대다수의 프로그래밍 언어는 인덱스가 0부터 시작합니다). 따라서 리스트 a의 첫 번째 요소는 a[0]이 됩니다. 꼭 기억해두세요.

튜플, range, 문자열도 [ ]에 인덱스를 지정하면 해당 요소를 가져올 수 있습니다.
"""

# 튜플 b의 첫 번째(인덱스 0) 요소를 출력합니다.

"""range도 인덱스로 접근할 수 있습니다."""

# range의 세 번째(인덱스 2) 요소를 출력합니다.

"""문자열은 요소가 문자이므로 인덱스로 접근하면 문자가 나옵니다."""

# 문자열 hello의 여덟 번째 요소를 출력합니다.
hello = "welcome to python"
print("hello[6]:", hello[6])

"""### 시퀀스 객체에 인덱스를 지정하지 않으면?

시퀀스 객체에 인덱스를 지정하지 않은 상태는 해당 객체 전체를 뜻합니다. 따라서 다음과 같이 리스트 a를 출력하면 [ ]를 포함하여 리스트 전체가 출력됩니다.
"""



"""### 음수 인덱스 지정하기

지금까지 시퀀스 객체에 인덱스를 양수만 지정했습니다. 그러면 인덱스를 음수로 지정하면 어떻게 될까요?
"""
l = [5, 8, 13, 21, 34, 55, 89]
print("l[-1]:", l[-1])


"""튜플, range, 문자열도 음수 인덱스를 지정하면 뒤에서부터 요소에 접근합니다."""
print(s)
print(s[-1])
print(s[-2])


"""### 인덱스의 범위를 벗어나면?

시퀀스 객체를 만들면 요소의 개수는 정해져 있죠? 다음과 같이 리스트를 만든 뒤 범위를 벗어난 인덱스에 접근하면 어떻게 될까요?
"""



"""리스트 a의 요소 개수는 5개인데 a[5]와 같이 지정하면 리스트의 범위를 벗어나게 되므로 에러가 발생합니다. 왜냐하면 인덱스는 0부터 시작하므로 마지막 요소의 인덱스는 4이기 때문이죠. 즉, 마지막 요소의 인덱스는 시퀀스 객체의 요소 개수보다 1 작습니다. 이 부분은 시퀀스 객체를 사용할 때 자주 틀리는 부분이므로 꼭 기억해두세요.

마찬가지로 튜플, range, 문자열도 범위를 벗어난 인덱스를 지정하면 IndexError가 발생합니다.

### 마지막 요소에 접근하기

앞에서 시퀀스 객체에 인덱스를 -1로 지정하면 뒤에서 첫 번째 요소에 접근한다고 했죠? 바로 시퀀스 객체의 마지막 요소입니다.

그러면 시퀀스 객체의 마지막 요소에 접근하는 다른 방법은 없을까요? 다음과 같이 len 함수로 리스트의 길이를 구한 뒤 이 길이를 인덱스로 지정해보면 에러가 발생합니다.
"""





"""리스트 a의 인덱스는 0부터 4까지이므로 인덱스에 a의 길이 5를 지정하면 인덱스의 범위를 벗어나게 됩니다. 따라서 5가 아닌 4를 지정해야 마지막 문자가 나옵니다."""



# 인덱스에 len(a)를 넣으면?

# len(a)는 5이므로 인덱스가 범위를 벗어납니다. 이때는 len(a)에서 1을 빼주어야 인덱스가 범위를 벗어나지 않습니다.

"""### 요소에 값 할당하기

이제 시퀀스 객체의 요소에 값을 할당하는 방법을 알아보겠습니다. 시퀀스 객체는 [ ]로 요소에 접근한 뒤 =로 값을 할당합니다.

* `시퀀스객체[인덱스] = 값`
"""

l = [0] * 5
print (l)
l[0] = 5
print(l)


# 튜플의 [ ]에 인덱스를 지정한 뒤 값을 할당하면 에러가 발생합니다.

# range와 문자열도 안에 저장된 요소를 변경할 수 없습니다.



"""### del로 요소 삭제하기

이번에는 del로 시퀀스 객체의 요소를 삭제해보겠습니다. 요소 삭제는 다음과 같이 del 뒤에 삭제할 요소를 지정해주면 됩니다.

* `del 시퀀스객체[인덱스]`
"""

# 리스트를 만들고 세 번째 요소(인덱스 2)를 삭제해보겠습니다.

# 리스트와는 달리 튜플은 요소를 삭제할 수 없습니다.

# range와 문자열도 안에 저장된 요소를 삭제할 수 없습니다.

"""## 슬라이스 사용하기

시퀀스 자료형은 슬라이스라는 기능을 자주 사용합니다. 슬라이스(slice)는 무엇인가의 일부를 잘라낸다는 뜻인데, 시퀀스 슬라이스도 말 그대로 시퀀스 객체의 일부를 잘라냅니다.

* `시퀀스객체[시작인덱스:끝인덱스]`
"""

s = "Hello World"
print("s[0:5] = ", s[:5])
print("s[1:9] = ", s[1:9])
print("s[1:9:2] = ", s[1:9:2])

"""[ ] 안에 시작 인덱스와 끝 인덱스를 지정하면 해당 범위의 리스트를 잘라서 가져올 수 있습니다. 여기서 주의할 점이 있는데, 끝 인덱스는 가져오려는 범위에 포함되지 않습니다. 따라서 끝 인덱스는 실제로 가져오려는 인덱스보다 1을 더 크게 지정해야 합니다. (끝 인덱스는 범위를 벗어난 인덱스를 지정할 수 있습니다)."""







"""슬라이스를 했을 때 실제로 가져오는 요소는 시작 인덱스부터 끝 인덱스 - 1까지입니다.

### 리스트의 중간 부분 가져오기

그럼 리스트의 중간 부분을 가져오는 방법을 자세히 알아보겠습니다.
"""





"""인덱스에서 -1은 뒤에서 첫 번째 요소를 뜻한다고 했죠? 끝 인덱스는 가져오려는 인덱스보다 1을 더 크게 지정한다고 했으므로 실제로는 뒤에서 두 번째(인덱스 -2) 요소인 80까지만 가져옵니다(음수는 숫자가 작을 수록 큰 수입니다. 그래서 -1은 -2보다 1이 더 큽니다).

### 인덱스 증가폭 사용하기

금까지 지정된 범위의 요소를 모두 가져왔죠? 슬라이스는 인덱스의 증가폭을 지정하여 범위 내에서 인덱스를 건너뛰며 요소를 가져올 수 있습니다.

다음은 인덱스를 3씩 증가시키면서 요소를 가져옵니다. 여기서 주의할 점은 인덱스의 증가폭이지 요소의 값 증가폭이 아니라는 점입니다.

* `시퀀스객체[시작인덱스:끝인덱스:인덱스증가폭]`
"""

a = list(range(5, 100, 15))
print("a[2:8:3] = ", a[2:8:3])

"""a[2:8:3]을 실행하니 [20, 50]이 나왔죠? 왜 이런 결과가 나왔을까요? 먼저 시작 인덱스가 2이므로 20부터 가져옵니다. 그리고 인덱스 증가폭을 3으로 지정했으므로 인덱스 5의 50, 인덱스 8의 80을 가져올 수 있습니다. 하지만, 끝 인덱스를 8로 지정했으므로 인덱스 7까지만 가져옵니다. 따라서 20과 50만 가져와서 [20, 50]이 나옵니다.

인덱스 증가폭을 지정하더라도 가져오려는 인덱스(끝 인덱스 - 1)를 넘어설 수 없다는 점을 꼭 기억해두세요.

만약 끝 인덱스 - 1과 증가한 인덱스가 일치한다면 해당 요소까지 가져올 수 있습니다. 다음은 끝 인덱스를 9로 지정하여 인덱스 8의 80까지 가져옵니다. 따라서 [20, 50, 80]이 나옵니다.
"""



"""### 인덱스 생략하기

슬라이스를 사용할 때 시작 인덱스와 끝 인덱스를 생략할 수도 있습니다. 인덱스를 생략하는 방법은 시퀀스 객체의 길이를 몰라도 되기 때문에 자주 쓰이는 방식입니다. 주로 시퀀스 객체의 마지막 일부분만 출력할 때 사용합니다.

리스트 a에서 a[:7]과 같이 시작 인덱스를 생략하면 리스트의 처음부터 끝 인덱스 - 1(인덱스 6)까지 가져옵니다.

* `시퀀스객체[:끝인덱스]`
"""

print("a[0:7]", a[0:7])
print("a[:7]", a[:7])

"""그리고 a[7:]과 같이 끝 인덱스를 생략하면 시작 인덱스(인덱스 7)부터 마지막 요소까지 가져옵니다.

* `시퀀스객체[시작인덱스:]`
"""



"""또는, a[:]와 같이 시작 인덱스와 끝 인덱스를 둘다 생략하면 리스트 전체를 가져옵니다.

* `시퀀스객체[:]`

"""
print("a[:]", a[:])


"""### 인덱스를 생략하면서 증가폭 사용하기

여기서 시작 인덱스 또는 끝 인덱스를 생략하면서 인덱스 증가폭을 지정하면 어떻게 될까요?

리스트 a에서 a[:7:2]와 같이 시작 인덱스를 생략하면서 인덱스 증가폭을 2로 지정하면 리스트의 처음부터 인덱스를 2씩 증가시키면서 끝 인덱스 - 1(인덱스 6)까지 요소를 가져옵니다.

* `시퀀스객체[:끝인덱스:증가폭]`
"""
print(a[:7:2])


"""그리고 a[7::2]와 같이 끝 인덱스를 생략하면서 인덱스 증가폭을 2로 지정하면 시작 인덱스(인덱스 7)부터 인덱스를 2씩 증가시키면서 리스트의 마지막 요소까지 가져옵니다.

* `시퀀스객체[시작인덱스::증가폭]`
"""



"""또는, a[::2]와 같이 시작 인덱스와 끝 인덱스를 둘다 생략하면서 인덱스 증가폭을 2로 지정하면 리스트 전체에서 인덱스 0부터 2씩 증가하면서 요소를 가져옵니다.

* `시퀀스객체[::증가폭]`
"""



"""a[:7:2]와 a[7::2]는 2씩 증가한 인덱스와 끝 인덱스 - 1이 일치하여 지정된 범위에 맞게 요소를 가져왔습니다. 하지만, a[::2]는 끝 인덱스가 9이므로 인덱스가 2씩 증가하더라도 8까지만 증가할 수 있습니다. 따라서 인덱스 0, 2, 4, 6, 8의 요소를 가져옵니다.

만약 시작 인덱스, 끝 인덱스, 인덱스 증가폭을 모두 생략하면 어떻게 될까요?

* `시퀀스객체[::]`
"""
print(a[::1])


"""### 슬라이스의 인덱스 증가폭을 음수로 지정하면?

슬라이스를 사용할 때 인덱스 증가폭을 음수로 지정하면 요소를 뒤에서부터 가져올 수 있습니다. 다음은 리스트 a에서 인덱스 5부터 2까지 1씩 감소시키면서 요소를 가져옵니다.
"""

print("a[::-1]", a[::-1])

"""여기서 주의할 점은 인덱스가 감소하므로 끝 인덱스보다 시작 인덱스를 더 크게 지정해야 한다는 점입니다. 즉, a[5:1:-1]과 같이 시작 인덱스부터 끝 인덱스까지 감소하도록 지정합니다. 그리고 끝 인덱스는 가져오려는 범위에 포함되지 않습니다

특히 다음과 같이 시작 인덱스와 끝 인덱스를 생략하면서 인덱스 증가폭을 -1로 지정하면 어떻게 될까요? 이때는 리스트 전체에서 인덱스를 1씩 감소시키면서 요소를 가져오므로 리스트를 반대로 뒤집습니다.
"""



"""물론 이 방법은 리스트뿐만 아니라 모든 시퀀스 객체에 사용할 수 있습니다.

### len 응용하기

이번에는 len을 응용하여 리스트 전체를 가져와보겠습니다.
"""



"""리스트 a의 요소는 10개입니다. 따라서 len(a)는 10이고, a[0:10]과 같습니다. 여기서 끝 인덱스는 가져오려는 인덱스보다 1을 더 크게 지정한다고 했으므로 len(a)에서 1을 빼지 않아야 합니다. 즉, 길이가 10인 리스트는 [0:10]이라야 리스트 전체를 가져옵니다.

### 튜플, range, 문자열에 슬라이스 사용하기

지금까지 리스트에서 슬라이스를 사용해봤습니다. 파이썬에서는 튜플, range, 문자열도 시퀀스 자료형이므로 리스트와 같은 방식으로 슬라이스를 사용할 수 있습니다.

먼저 튜플부터 잘라보겠습니다. 다음은 지정된 범위만큼 튜플을 잘라서 새 튜플을 만듭니다.

* `튜플[시작인덱스:끝인덱스]`
* `튜플[시작인덱스:끝인덱스:인덱스증가폭]`
"""







"""range는 연속된 숫자를 생성한다고 했죠? range에 슬라이스를 사용하면 지정된 범위의 숫자를 생성하는 range 객체를 새로 만듭니다.

* `range객체[시작인덱스:끝인덱스]`
* `range객체[시작인덱스:끝인덱스:인덱스증가폭]`
"""









"""range는 리스트, 튜플과는 달리 요소가 모두 표시되지 않고 생성 범위만 표시됩니다. 이렇게 잘라낸 range 객체를 리스트로 만들려면 list에 넣으면 되겠죠?"""



"""문자열도 시퀀스 자료형이므로 슬라이스를 사용할 수 있습니다. 특히 문자열은 문자 하나가 요소이므로 문자 단위로 잘라서 새 문자열을 만듭니다.

* `문자열[시작인덱스:끝인덱스]`
* `문자열[시작인덱스:끝인덱스:인덱스증가폭]`
"""



# 딕셔너리
"""
지금까지 살펴봤던 리스트와 튜플은 값 여러 개를 일렬로 저장할 뿐 값끼리 연관 관계가 없었습니다.
"""



"""
파이썬에서는 연관된 값을 묶어서 저장하는 용도로 딕셔너리라는 자료형을 제공합니다.
사전(dictionary)에서 단어를 찾듯이 값을 가져올 수 있다고 하여 딕셔너리라고 부릅니다.
"""

## 딕셔너리 만들기
"""
딕셔너리는 { }(중괄호) 안에 키: 값 형식으로 저장하며 각 키와 값은 ,(콤마)로 구분해줍니다.

* `딕셔너리 = {키1: 값1, 키2: 값2}`
"""

teacher = {
    "과목" : "파이썬",
    "결혼": False,
    "출근거리": 20,
}
print(teacher)

"""딕셔너리는 키를 먼저 지정하고 :(콜론)을 붙여서 값을 표현합니다. 특히 키에는 값을 하나만 지정할 수 있으며 이런 특성을 따서 키-값 쌍(key-value pair)이라 부릅니다(키-값은 1:1 대응).

### 키 이름이 중복되면?
"""
teacher = {
    "과목" : "파이썬",
    "결혼": False,
    "출근거리": 20,
    "과목" : "JAVA"
}
print(teacher)




"""### 딕셔너리 키의 자료형

딕셔너리의 키는 문자열뿐만 아니라 정수, 실수, 불도 사용할 수 있으며 자료형을 섞어서 사용해도 됩니다. 그리고 값에는 리스트, 딕셔너리 등을 포함하여 모든 자료형을 사용할 수 있습니다.
"""



# 단, 키에는 리스트와 딕셔너리를 사용할 수 없습니다.



# 근데 튜플은 됩니다.

"""### 빈 딕셔너리 만들기

빈 딕셔너리를 만들 때는 { }만 지정하거나 dict를 사용하면 됩니다. 보통은 { }를 주로 사용합니다.

* `딕셔너리 = {}`
* `딕셔너리 = dict()`
"""





"""## 딕셔너리의 키에 접근하고 값 할당하기"""

# 딕셔너리의 키에 접근할 때는 딕셔너리 뒤에 [ ](대괄호)를 사용하며 [ ] 안에 키를 지정해주면 됩니다.



"""### 딕셔너리에 키를 지정하지 않으면?"""

# 딕셔너리에 키를 지정하지 않은 상태는 해당 딕셔너리 전체를 뜻합니다.
# 따라서 다음과 같이 딕셔너리를 출력하면 { }를 포함하여 딕셔너리 전체가 출력됩니다.

"""### 딕셔너리의 키에 값 할당하기

이제 딕셔너리의 키에 값을 할당해보겠습니다. 딕셔너리는 [ ]로 키에 접근한 뒤 값을 할당합니다.
* `딕셔너리[키] = 값`
"""
d = {}
d['key'] = 'value'
print(d)
d['key'] = 'value2'
print(d)

"""딕셔너리에서 키의 값을 출력할 때와 마찬가지로 [ ]에 키를 지정한 뒤 값을 할당하면 됩니다. 특히 딕셔너리는 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당됩니다."""



# 그럼 없는 키에서 값을 가져오려고 하면 어떻게 될까요?

"""### 딕셔너리에 키가 있는지 확인하기

딕셔너리에서 키가 있는지 확인하고 싶다면 in 연산자를 사용하면 됩니다.

* `키 in 딕셔너리`
"""
'''
# print("key in d :", "key" in d)
'''


"""이처럼 딕셔너리에 특정 키가 있으면 True, 없으면 False가 나옵니다.
반대로 in 앞에 not을 붙이면 특정 키가 없는지 확인합니다.
"""



"""### 해시

딕셔너리는 해시(Hash) 기법을 이용해서 데이터를 저장합니다. 보통 딕셔너리와 같은 키-값 형태의 자료형을 해시, 해시 맵, 해시테이블 등으로 부르기도 합니다.

### 딕셔너리의 키 개수 구하기

딕셔너리를 사용하다 보면 딕셔너리의 키 개수(길이)를 구할 필요가 있습니다. 딕셔너리의 키와 값을 직접 타이핑할 때는 키의 개수를 알기가 쉽습니다. 하지만 실무에서는 함수 등을 사용해서 딕셔너리를 생성하거나 키를 추가하기 때문에 키의 개수가 눈에 보이지 않습니다. 따라서 다음과 같이 키의 개수는 len 함수를 사용하여 구합니다(키와 값은 1:1 관계이므로 키의 개수는 곧 값의 개수입니다).

* `len(딕셔너리)`
"""

"""
# 조건문

조건문은 특정 조건일 때 코드를 실행하는 문법입니다. 프로그램을 만들다 보면 여러 가지 상황을 처리해야 하는 경우가 생기죠. 이때 조건문은 다양한 상황에 대처할 때 사용합니다.

먼저 실생활의 예를 들어보겠습니다. 만약 세탁기에 빨래를 넣고 돌렸다면 다음과 같은 조건문을 만들 수 있겠죠?

```
if 세탁 완료 소리가 울리면:
    빨래를 꺼내서 말린다.
```

다음과 같이 날씨에 따라 행동할 수도 있습니다.

```
if 비가 온다면:
    우산을 가지고 나간다.

if 날씨가 춥다면:
    코트를 입고 나간다.

if 날씨가 덥다면:
    반소매에 얇은 옷을 입고 나간다.
```

즉, 조건문을 사용하면 조건에 따라 다른 코드를 실행할 수 있습니다. 이번 유닛부터는 if 조건문의 다양한 사용 방법을 알아보겠습니다.

### 의사 코드

프로그래밍이나 컴퓨터 이론을 공부하다 보면 의사 코드(pseudo code)라는 말을 접하게 됩니다. 의사 코드는 실제 프로그래밍 언어가 아닌 사람의 언어로 프로그래밍 언어를 표현한 것입니다. 보통 특정 프로그래밍 언어를 사용하지 않고 알고리즘이나 컴퓨터 명령을 기술할 때 사용합니다.

```
x = 10    # 파이썬 코드
변수 x에 10 할당    # 한글로 표현한 의사 코드
```

앞에서 if 조건문을 설명할 때 "if 비가 온다면", "우산을 가지고 나간다."도 일종의 의사 코드입니다.

## if 조건문 사용하기

if 조건문은 if에 조건식을 지정하고 :(콜론)을 붙이며 다음 줄에 실행할 코드가 옵니다. 이때 실행할 코드는 반드시 들여쓰기를 해야 합니다.

```
if 조건식:
     코드
```
"""
# order = int(input("주문량을 넣어주세요 :"))
# if order >= 10:
#     print("주문이 접수되었습니다.")
# if order < 10:
#     print("10건 이상 주문해주셔야 합니다.")


"""만약 if 다음 줄에서 들여쓰기를 하지 않으면 들여쓰기 에러가 발생합니다. 이 항상 이 부분을 주의해주세요.


"""



"""### if 조건문의 기본 형태와 실행 흐름 알아보기

이제 if 조건문을 자세히 알아보겠습니다. 파이썬에서 if 조건문은 if 조건식: 형식으로 사용하며 그다음 줄에는 들여쓰기를 한 뒤 조건식이 만족할 때 실행할 코드를 넣습니다. 특히 이 조건식이 만족할 때 실행할 코드를 if 본문(if body)이라고 부릅니다.

여기서는 변수 x에 10을 할당한 뒤 if 조건문으로 x가 10과 같은지 검사하였습니다. 조건식은 x == 10과 같은 형식으로 지정해주는데 ==은 두 값이 "같을 때" 라는 뜻입니다.

즉, if x == 10:은 x가 10과 같은지 비교한 뒤 같으면 다음에 오는 코드를 실행하라는 뜻이 됩니다. 따라서 x는 10이고 조건식을 만족하므로 그다음 줄의 print가 실행되어 '10입니다.'가 출력됩니다.

보통 if의 조건식이 만족하면 참( True), 만족하지 않으면 거짓(False)이라고 부릅니다.

### if 조건문을 사용할 때 주의할 점

if 조건문을 사용할 때 주의할 점이 있는데 파이썬에서는 =을 할당으로 사용하고 있으므로 값을 비교할 때는 =을 두 개 붙여서 ==로 사용해야 합니다. 자주 틀리는 부분이니 `if`**안에서 ==을 사용했는지 반드시 확인하세요. 다음과 같이 if에 =을 사용하면 문법 에러가 발생합니다.**
"""



"""### if 조건문에서 코드를 생략하기"""
age = 20
if age >= 20:
    pass # 들여쓰기 포맷을 유지
    # TODO : 앞으로 할 일... 주석으로 쓴다.



"""if 다음 줄에 pass라는 특별한 키워드를 넣었습니다. 여기서 pass는 아무 일도 하지 않고 그냥 넘어간다는 뜻입니다. 파이썬에서는 if 다음 줄에 아무 코드도 넣지 않으면 에러가 발생하므로 if 조건문의 형태를 유지하기 위해 pass를 사용합니다.

pass는 아무 일도 하지 않는 코드라서 의미가 없을 것 같지만 나중에 작성해야 할 코드를 표시할 때 사용할 수 있습니다. 즉, 다음과 같이 pass만 넣고 나중에 할 일은 주석으로 남겨놓는 방식입니다.
"""



## if 조건문과 들여쓰기
"""



## 중첩 if 조건문 사용하기

지금까지 if를 한 번만 사용하는 단순한 조건문을 사용했습니다. 하지만 프로그래밍을 하다 보면 if를 여러 번 사용하는 복잡한 조건도 자주 나옵니다. 이번에는 if를 여러 번 사용하는 중첩 if 조건문을 사용해보겠습니다. 다음은 변수의 값이 10 이상이면 '10 이상입니다.'를 출력한 뒤 15이면 '15입니다.', 20이면 '20입니다.'를 출력합니다.
"""
age = 15
if age < 20:
    print('어린이')
    if age == 15:
        print("중학생")


# x가 10 이상일 때 '10 이상입니다.'를 출력하는 코드

# if의 조건식에 따라 코드를 실행해야 하므로 print는 들여쓰기를 했습니다. 이제 if 안쪽의 if를 보면 들여쓰기가 되어 있습니다.

"""## 사용자가 입력한 값에 if 조건문 사용하기"""

# 이번에는 input을 사용하여 사용자가 입력한 값을 변수에 저장하고, if 조건문으로 값을 비교해보겠습니다.



"""## else

## else를 사용하여 두 방향으로 분기하기

if 조건문은 분기(branch)를 위한 문법입니다. 즉, 분기는 "둘 이상으로 갈라지다"라는 뜻으로 프로그램의 흐름을 둘 이상으로 나누는 것을 말합니다. 이는 마치 도로의 분기점과 같죠.

지금까지 if 조건문으로 조건식에 맞는 코드만 실행했습니다. if에 else를 사용하면 조건식이 만족할 때와 만족하지 않을 때 각각 다른 코드를 실행할 수 있습니다. 즉, 프로그램이 두 방향으로 분기하는 것이죠.

실생활에서 전화가 왔을 때의 예를 들면 다음과 같은 모양이 됩니다.

```
if 광고 전화인가?:
    전화를 끊고, 차단 목록에 등록한다.
else:
    계속 통화한다.
```

else는 if 조건문 뒤에 오며 단독으로 사용할 수 없습니다. 그리고 if와 마찬가지로 else도 :(콜론)을 붙이며 다음 줄에 실행할 코드가 옵니다.

```
if 조건식:
     코드1
else:
     코드2
```
"""
age = 19
if age > 20:
    print("술 주문이 가능합니다.")
else:
    print("술 주문이 가능하지 않습니다.")



"""### if와 else의 기본 형태와 실행 흐름 알아보기

else는 if의 조건식이 만족하지 않을 때 코드를 실행합니다. 여기서는 x에 5가 들어있어서 x == 10을 만족하지 않으므로 else의 print가 실행되어 '10이 아닙니다.'가 출력됩니다.

즉, 조건식이 참(True)이면 if의 코드(if 본문)가 실행되고, 거짓(False)이면 else의 코드(else 본문)가 실행됩니다.

### 변수에 값 할당을 if, else로 축약하기 (삼항연산자)
"""
number = "991111-1111111"
gender = ""
if number[7] == "1":
    gender = "남성"
else:
    gender = "여성"
print("gender = " + gender)

gender = "남성" if number[7] == "1" else "여성"
print(gender)

# 변수 x에 10이 들어있으면 y에 x를 할당하고, 아니면 y에 0을 할당하는 코드는 다음과 같이 만들 수 있습니다.

# 이렇게 if, else에서 변수에 값을 할당할 때는 변수 = 값 if 조건문 else 값 형식으로 축약할 수 있으며,
# 이런 문법을 조건부 표현식(conditional expression) 또는 삼항연산자라고 부릅니다.

"""### else와 들여쓰기

else는 if와 들여쓰기 규칙이 같습니다. 다음은 들여쓰기가 잘못된 코드입니다.
"""



# else도 코드가 여러 줄일 때는 들여쓰기 깊이가 같게 만들어주어야 합니다.

# 마찬가지로 else가 여러 줄일 때는 마지막 줄의 들여쓰기를 하지 않으면 의도치 않은 동작이 됩니다.

"""## if 조건문의 동작 방식 알아보기"""



"""당연히 True는 if의 코드가 실행되고, False는 else의 코드가 실행됩니다. 특히 None은 False로 취급되므로 else의 코드가 실행됩니다. 실제 코드를 작성할 때 변수에 들어있는 값이나 함수의 결과가 None인 경우가 많으므로 이 부분은 꼭 기억해두세요.

### if 조건문에 숫자 지정하기
"""

if 1:
    print("true로 인식")

# 숫자는 정수, 실수와 관계없이 0이면 거짓, 0이 아닌 수는 참입니다.

""" ### if 조건문에 문자열 지정하기"""

# 문자열은 내용이 있을 때 참, 빈 문자열은 거짓입니다.

"""## 조건식을 여러 개 지정하기

지금까지 if에 조건식을 하나만 지정했습니다. 만약 조건이 복잡할 때는 어떻게 해야 할까요?

예를 들어 인터넷 포털의 중고나라에 글을 올리려면 먼저 포털 사이트의 회원이면서 중고나라 카페의 회원이라야 합니다. 이 조건을 if 조건문으로 나타내면 다음과 같은 모양이 됩니다.

```
if 포털 사이트 회원인지? 그리고 중고나라 회원인지?:
    글쓰기 화면 표시
else:
    포털 사이트 또는 중고나라 회원이 아니므로 글을 쓸 수 없다는 경고 문구 표시
```
"""

# if 조건문에는 논리 연산자를 사용하여 조건식을 여러 개 지정할 수 있습니다.

"""### 중첩 if 조건문과 논리 연산자"""

# 그럼 이런 논리 연산자를 어디에 사용할까요? 보통 여러 조건을 판단할 때 if를 계속 나열해서 중첩 if 조건문으로 만드는 경우가 많습니다.

# if로 x가 0보다 큰지 검사하고(0보다 크면 양수), 다시 if로 20보다 작은지 검사했습니다. 이런 중첩 if 조건문은 and 논리 연산자를 사용해서 if 하나로 줄일 수 있습니다.

# x가 0보다 크면서 20보다 작을 때처럼 and 논리 연산자를 사용해서 두 조건을 모두 만족하면 '20보다 작은 양수입니다.'를 출력하도록 만들었습니다.
# 특히 파이썬에서는 이 조건식을 더 간단하게 만들 수 있습니다.

"""0 < x < 20처럼 부등호를 연달아서 사용했습니다. 조건식이 알아보기 쉬워졌죠? 단, 여기서는 0이 앞에 왔으므로 0보다 큰지 판단하는 부등호는 방향이 반대로 바뀌었습니다. 이처럼 조건식을 만들 때는 부등호의 방향과는 관계 없이 조건의 뜻만 만족하면 됩니다. 즉, x > 0과 0 < x의 뜻은 같습니다.

## elif 사용하기

프로그램을 만들다 보면 참, 거짓으로만 분기하는 것은 한계가 있습니다. 실제로는 두 가지 이상의 다양한 상황이 발생하죠.

여러 가지 상황을 처리하는 대표적인 예는 음료수 자판기가 있습니다.

자판기 안에는 각각 다른 종류의 음료수가 들어있고, 버튼을 누르면 해당 버튼에 해당하는 음료수가 나옵니다. 이걸 elif로 만들면 다음과 같은 모양이 됩니다.

```
if 콜라 버튼을 눌렀다면:
    콜라를 내보냄
elif 사이다 버튼을 눌렀다면:
    사이다를 내보냄
elif 환타 버튼을 눌렀다면:
    환타를 내보냄:
else:
    제공하지 않는 메뉴
```


즉, elif는 조건식을 여러 개 지정하여 각 조건 마다 다른 코드를 실행할 수 있습니다.

elif는 else인 상태에서 조건식을 지정할 때 사용하며 else if라는 뜻입니다. 물론 if, else와 마찬가지로 조건식 끝에 :(콜론)을 붙여야 하고, elif 단독으로 사용할 수 없습니다.

```
if 조건식:
     코드1
elif 조건식:
     코드2
```
"""



"""### if, elif, else를 모두 사용하기

elif와 else는 단독으로 사용할 수 없으며 if, else 형태로 사용하거나, if, elif, else 형태로 사용합니다. 이번에는 if, elif, else를 모두 사용해보겠습니다.

```
if 조건식:
    코드1
elif 조건식:
    코드2
else:
    코드3
```
"""



"""이렇게 하면 if, elif의 조건식이 모두 거짓일 때만 else의 코드가 실행됩니다. 여기서는 x가 30이라 if, elif의 조건식에 모두 만족하지 않습니다. 따라서 마지막 else의 '10도 20도 아닙니다.'가 출력됩니다.

참고로 if와 else는 한 번만 사용할 수 있지만, elif는 여러 번 사용할 수 있습니다. 그리고 elif의 들여쓰기 규칙은 if, else와 같으므로 따로 설명하지 않겠습니다.

만약 elif 앞에 else가 오면 잘못된 문법이므로 주의해야 합니다.
"""

