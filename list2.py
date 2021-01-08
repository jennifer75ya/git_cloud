# enumerate() : 리스트에서 인덱스와 원소를 함께 추출
my_list = ['나동빈', '강종구', '이태일', '박한울', '이상욱']
result = list(enumerate(my_list))
print(result)

# for문에서 활용
for i, k in enumerate(my_list):
    print("인덱스: ", i, "/원쇠 ", k )

# sort() : 리스트의 원소를 정렬
my_list = ['나동빈', '강종구', '이태일', '이태일','박한울', '이상욱']
my_list.sort()
print(my_list)

# count(): 특정한 원소의 개수를 추출
print(my_list.count('이태일'))

# del : 리스트의 특정 원소를 제거
my_list = ['123', '456', '789']
del my_list[1:3]
print(my_list)

# insert() : 리스트에 특정 원소를 삽입
my_list.insert(3, '-1')
print(my_list)

# append() : 리스트의 가장 마지막 원소로서 원소를 삽입
my_list.append('-1')
print(my_list)