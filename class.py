#클래스 : 반복되는 불필요한 소스코드를 최소화 하면서 현실 세계의 사물을 컴퓨터 프로그래밍 상에서
# 쉽게 표현할 수 있도록 해주는 프로그래밍 기술
# 인스턴스 : 클래스로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수

# 2가지 요소
# 클래스 멤버 : 클래스 내부에 포함되는 변수
# 클래스 함수 : 클래스 내부에 포함되는 함수. 메소드라고 부릅니다.
# 생성자는 함수의 형태를 가진다 __init__(self)
# 파이썬의 메서드는 첫번째 매개변수로 self 라는 매개변수를 갖는다는 특징이있다.
class Car:
    # 클래스의 생성자
    def __init__(self, name, color):
        self.name = name    # 클래스 멤버
        self.color = color  # 클래스 멤버
    # 소멸자
    def __del__(self):
        print("인스턴스를 소멸시킵니다")
    #클래스의 메소드
    def show_info(self):
        print("이름:", self.name, "/색상:", self.color)
    # setter 메소드
    def set_name(self, name):
        self.name = name

car1 = Car("소나타", "빨간색")
car1.set_name("랜드로바")
car1.show_info()
del car1        # 해당 인스턴스를 메모리 상에서 할당 해제됨.
# car1.show_info()   # 할당해제된 후에는 에러 발생

car2 = Car("아반떼", "검은색")
car2.show_info()
del car2

# 우리만의 Car 자동차형이라는 자료형을 만든 것이다.

# 상속 : 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
# 부모와 자식 관계가 존재합니다.
# 자식 클래스 : 부모 클래스(Unit)를 상속 받은 클래스

class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, "이 공격을 수행합니다. [전투력: ", self.power, "]")

'''
unit = Unit("홍길동", 375)
unit.attack()
'''

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스터이름:", self.name, "몬스터 종류:", self.type)

monster = Monster("슬라임", 10, "초급")
monster.attack()
monster.show_info()



