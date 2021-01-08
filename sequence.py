# 시퀀스 : 문자열, 리스트, 튜플 등의 인덱스를 가지는 자료형

string = "hello world"
list = ['h','e','l','l','o',' ','w','o','r','l','d']
tuple = ['h','e','l','l','o',' ','w','o','r','l','d']
print(string)
print(list)
print(tuple)

print(string[0:5])
print(list[0:5])
print(tuple[0:5])

for i in tuple:
    print(i)

#연산자사용
string1 = "hello world1"
string2 = " python"
print(string1+string2)

# len 함수 이용해서 길이 출력
print(len(string1+string2))

#반복문 등에서 사용될수 있음
list = [1,2,3,4,5]
print(4 in list)

if 3 in list:
    print("3을 포함하고 있습니다")



