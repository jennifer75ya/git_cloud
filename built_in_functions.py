# 내장함수
# input() : 사용자로부터 콘솔로 입력을 받는 함수
# int() : 정수 자료형으로 반환
# float() : 문자열, 정수 등의 자료형을 실수형으로 변환
# max(), min() : 시퀀스 자료형에 포함되어 있는 원소 중 최대값, 최소값
# bin(), hex() : 10진수를 2진수로 , 10진수를 16진수로 변환
# round() : 반올림


user_input = input('정수를 입력하세요:')
print('제곱:', int(user_input) **2)

a = '12344'
print(int(a))
b = 12.5
print(b)

a=10
print(float(a))

list = [5,6,7,8,10,14]
print(max(list))
print(min(list))

print(bin(128))
print(hex(230))
print(int('0xe6', 16))   # 다른 진수를 10진수로 변환할 때는 왼쪽에는 문자열이 들어가고 오른쪽에는 기존에 진수를 넣는다

print(round(123.890, 2))
print(round(123.7989,-1))

int = 1
str ="문자열"
dict={'apple'"'사과"}
print(type(str))
print(type(int))
print(type(dict))



