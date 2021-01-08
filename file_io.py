# 파이썬 파일과 읽고자 하는 txt 파일이 동일한 위치에 존재할 때는 바로 읽을 수 있다.

# open() :  파일을 특정한 모드로 여는 함수입니다. 읽을 때는 r, 쓸 때는 w

f = open("input.txt", "r", encoding="UTF-8")

# read() : 파일 객체로부터 모든 내용을 읽는 함수
data = f.read()   # 파일에 있는 모든 내용을 즉시 읽는다.
print(data)
f.close()     # 해당 파일에 대한 리소스를 정리

# 파일을 읽을 때는 특정한 바이트 부터 읽을 수도 있다.  위치설정
# 한글이 3byte 차지
f = open("input.txt", "r", encoding="UTF-8")
f.seek(9)
data = f.read()
print(data)
f.close()

# readline() : 파일 객체로부터 한 줄씩 문자열을 읽는 함수
f = open("input.txt", "r", encoding="UTF-8")
count = 0
while count < 3:
    data = f.readline()
    count = count + 1
    print("%d번째 줄 : %s" %(count,data), end='')
f.close()

# readlines() : 전체 내용을 한 번에 리스트에 담는 함수 줄바꿈 기호가 포함
f = open("input.txt", "r", encoding="UTF-8")
list = f.readlines()
print(list)

for i , data in enumerate(list):
    print("%d번째 줄 : %s" %(i+1, data), end='')
f.close()

# with구문 : with 구문을 나오면 리소스가 해제된다. 오픈하는 부분과 클로스 부분 생략
with open("input.txt", "r", encoding="UTF-8" ) as f:
    list = f.readlines()
    for i, data in enumerate(list):
        print("%d번째 줄 : %s" %(i+1, data), end='')

# dict변수에 빈도수 데이타를 넣는다.
def process(filename):
    with open(filename, "r") as f:
        # 키 : 알파벳, 값: 빈도수
        dict = {}
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict

dict = process("input.txt")
# 빈도수를 기준으로 내림차순 정렬을 수행합니다. a[1] -> 값을 기준으로 정렬을 하겠다고 키를 설정
#가장 출현한 문자를 기준으로
dict = sorted(dict.items(), key=lambda a:a[1], reverse=True)
# data 문자, count 빈도수
for data, count in dict:
    if data == '\n' or data ==' ' :
        continue
    print("%d번 출현: [%c]" %(count, data))



