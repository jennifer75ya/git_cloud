#반복문 : 조건에 부합하는 한 특정한 명령어를 반복
#숫자범위 표현 : range(시작, 끝)  시작은 0 부터시작하고, 끝은 -1 까지 반복함.

sum = 0
for i in range(1, 10):
    print(i)
    sum = sum + i

print("합계: ", sum )

count = 0
for i in "Hello World":
    if i == 'o':
        count = count+1
print("o의 개수는 ", count, "개 입니다")

sum = 0
list = [1,2,3,4,5]

for i in list:
    sum = sum + i
print(sum)

# continue : continue 를 만났을 때 더이상 명령어를 실행하지 않고, 다음 반복을 진행합니다.
# break : break를 만났을 때 반복문을 벗어납니다.

sum = 0
list = [1,2,3,4,5]
for i in list:
    if i%2 == 1: # 홀수일때
        break
    sum = sum + i
print("합계 : ", sum)

# while
i = 0
sum = 0
while i <= 5:
    i = i + 1
    if i % 2 == 1:
        continue
    sum = sum + 1
print("합계: ", sum)