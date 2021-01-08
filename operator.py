# 증감 연산자 : 기존에 사용하던 증가/감소 기능을 짧게 이용
a = 10
a += 10
print(a)

#관계 연산자 : 두 개의 값을 비교하여 관계
# A == B: 같은지 판별 => True, False
a = 3
b = 7
print(a==7)
print(a!=b)
print(a<b)

a= "ABC"
b = "ETF"
print(a==b)
print(a<b)   # 사전순으로 비교

# 논리연산자 : 여러 개의 수식을 논리적으로 연산
# A and B, A or B, not A A가 false 인지 판별
a = True
b = False
print(a and b)
print(a or b)
print(not a)

if 3>5 or 7<19:
    print("야호")