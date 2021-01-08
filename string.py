# 문자열 자료형의 뒤집기 : 슬라이싱 활용
str = "helloworld"
print(str[::-1])

# len() : 문자열의 길이를 출력
print(len(str))

# isalpha() : 특정한 문자열이 문자로만 이루어져 있는지 확인
print(str.isalpha())

# isdigit() : 특정한 문자열이 숫자로만 이루어져 있는지 확인
print(str.isdigit())  #공백이 포함되어 있으면 false

# isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
str = "abc123"
print(str.isalnum())

# join(리스트 자료형) : 여러 개의 문자열을 구분자와 함께 합치는 함수
list = ['hello', 'world', '홍길동']
print(','.join(list))

# sorted(문자열 자료형) : 각 문자를 정렬하는 함수
str = "helloworld"
list = sorted(str)
print(list)
print(''.join(list))
list=sorted(str, reverse=True)
print(''.join(list))

# split(토큰) : 문자열을 토큰에 따라서 분리하는 함수
str = "I wanna watch a movie"
list = str.split(' ')
print(list)

# 특정 문자열이 포함되어 있는지 여부 확인
str = 'i like you'
print(str.find('like'))  # 인덱스 2가 출력
print(str.find('want'))  # 없으면 -1 출력

# find(서브 문자열) : 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
# 특정 문자열이 여러번 들어가 있는 경우 찾고자 하는 인덱스를 표기해서 찾는다
str = "i like like like you"
print(str.find('like', 5))

# upper(), lower() : 문자열을 대문자로, 소문자로
str  = "Hello World"
print(str.upper())
print(str.lower())

# strip() : 데이타 정제 / 좌우로 특정한 문자열을 제거하는 함수 (벗겨내다 의미)
str = " Hello world "
print(str.strip())
print(str.lstrip())
print(str.rstrip())
print(str.strip('t')) # 특정문자 제거

# eval() : 문자열 수식 계산해주는 함수
exp = "(203+705)*3-(30/6)"
print(eval(exp))


