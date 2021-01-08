# 사전: key, value 한쌍을 원소로 가지는 자료형

dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'miracle'
dict['노력'] = 'effor'

print(dict)

# i index, k value
for i, k in enumerate(dict):
    print("인덱스:", i, "] 한글:", k, "/영어:", dict[k])

dict['안녕'] = 'hi'
print(dict)

del dict['기적']
print(dict)
dict.clear()
print("사전 자료형의 길이", len(dict))

dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'miracle'
dict['노력'] = 'effor'

# 사전의 키와 값만 따로
# 내장함수 keys(), values() 함수 활용
keys = dict.keys()
print("키: ", keys)
key_list = list(keys)
print("키 리스트:", key_list)

values = dict.values()
print("값: ", values)
value_list = list(values)
print("값 리스트", value_list)

# 특정 키가 존재하는지 확인
if "노력" in dict:
    print("노력이라는 키가 존재합니다")

# 정렬수행
scores ={}
scores['나동빈'] = 78
scores['이태일'] = 90
scores['박한울'] = 80

print(sorted(scores)) # 키로 정렬하기
print(sorted(scores, reverse=True)) # 키로 내림차순 정렬하기
print(sorted(scores.values())) # 값을 정렬하기