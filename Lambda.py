# 람다식은 함수의 형태를 더욱 짧게 쓸 수 있도록 해준다. 특징이 있는 문법
# lambda 키워드를 이용해서 매개변수를 이용해서 함수로 반환되는 값을 콜론(:) 이후에 적어주면 된다.
# 이렇게 만들어진 함수를 add 로 부르겠다고 설정한다.
# 람다식을 이용함으로써 함수의 정의 과정이 매우 짧아짐
# map(): 다수의 원소에 대한 함수의 결과를 한 번에 얻을 수 있도록 도와줌
add = lambda x, y: x + y
print(add(1,2))

list1 = [1,2,3.4]
list2 = [5,6,7,8]
my_function = lambda a,b : a*b
result = map(my_function, list1, list2)
print(list(result))




