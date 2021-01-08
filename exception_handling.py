# 예외처리

try:
    print(3/2)
except:
    print("0 으로는 나눌 수 없습니다")
else:
    print("예외없이 성공적으로 실행되었습니다. ")
finally:
    print("무조건 실행되도록 만드는 구문으로 예외처리를 마칩니다.")


# 프로그램이 실행되고 있을 때 오류메세지를 직접출력하고자 할때 Exception 클래스 관련 객체를 이용하면 효과적
# 파이썬에서 기본적으로 제공하는 객체로 이것을 이욯하면 어떤 오류를 발생했는지가 e라는 변수에 담겨서 출력해줄 수 있다.
# division by zero 라는 오류의 내용을 프로그램 내에서 보여주고자 할때
try:
    print(3/0)
except Exception as e:
    print(e)
