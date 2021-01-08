# 튜플 : 리스트와 비슷한 자료형
# 한번 설정된 값을 변경불가하지만, tuple원소 중에 리스트가 있으면 리스트는 값을 변경할 수 있다.
# slicing, 연산도 가능
list1 = [1,2,3]
list2 = [4,5,6]
tuple = (list1, list2)
print(tuple)
print(tuple[0][1])
tuple[0][1] = 7
print(tuple[0][1])

tuple=(1,2,3,4,5,6,7)
print(tuple[0:5] * 3)