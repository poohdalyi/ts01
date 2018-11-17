class MyStatic:
    def reset(self):  # 파이썬 메소드 선언 방식
        self.x = 0
        self.y = 0

a = MyStatic()
MyStatic.reset(a)     # 클래스 메소드
# a.reset()    인스턴스 메소드

print('x의 값', a.x)
print('y의 값', a.y)


