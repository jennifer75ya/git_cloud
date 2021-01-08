# index(원소) : 리스트 내 특정한 원소의 인덱스를 찾기
list1 = ['나동빈', '강종구', '박진경', '박지훈']
print(list1.index('박진경'))
#print(list.index('이태일'))

#reverse() : 리스트의 원소를 뒤집기/그 함수를 불러오자 마자 자동으로 해당 변수의 값이 바로 뒤집혀짐
# 슬라이싱 기법 : 슬라이싱으로 변경된 list를 기존의 리스트에 다시 담아줘야 변경된 결과가 출력됨
list1 = [1,2,3]
list1.reverse()
print(list1)

list1 = list1[::-1]
print(list1)  # 슬라이싱 기법으로 뒤집기

# sum(리스트 자료형) : 리스트의 모든 원소의 합
list1 = [1,2,3]
print(sum(list1))

''' 문자는 숫자와 함께 더해질 수 없으므로 오류 발생
list = [1,2, "133"]
print(sum(list))
'''

# range(시작, 끝) : 특정 범위를 지정, 끝-1 값까지 실제 지정된 값임.
# list(특정 범위) : 특정 범위의 원소를 가지는 리스트를 반환
my_range = range(5, 10)
print(my_range)
list = list(my_range)  # 왜 에러가 발생하는지 확인?
print(list)

# all()/ any() : 리스트의 모든 원소가 참인지 판별 / 하나라도 참인지 판별
list1 = [True, False, True]
print(all(list1))
print(any(list1))


