#함수: 특정한 입력을 받아서 처리를 한 이후에 특정한 출력을 하는 모듈을 의미
#함수를 이용하면 특정한 소스코드의 반복을 줄일 수 있다는 특징
#가변인자 : 함수의 매개변수가 가변적일 수 있을 때 사용

def add(a,b):
    sum = a+b
    return sum

print(add(3,4))

#가변인자 사용 : 다수의 매개변수를 넣는 경우, 가변인자로 들어갔을 때 함수내에서 데이타가 튜플형태로 처리된다는 특징이 있다.
def function(*data):
    print(data)

function(1,2,4)

# 전역변수 : 소스코드 전체 어디에서든지 사용 가능한 변수
# 지역변수 : 특정한 함수(블록) 안에서만 사용할 수 있는 변수
# 파이썬의 함수는 반환값이 여러개일 수 있음.
def add(a):
    a = a + 5  # 지역변수

a = 2    # 전역변수
add(2)
print(a)

def add(a):
    a = a + 5  # 지역변수
    return a
a = 2    # 전역변수
add(2)
print(a)

# 전역변수를 함수 내에서 사용하여 함수에서 처리된 값을 반영하고 싶을 때
def add():
    global a
    a = a + 5

add()
print(a)

#
def function():
    a=5
    b=[1,2,3]
    return a,b

a, b = function()
print(a)
print(b)