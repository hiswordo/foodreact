
# ----multiple inheritance super----
# @link [Python multiple inheritance 👨‍👩‍👧‍👦 - YouTube](https://www.youtube.com/watch?v=mRIeUXhIAxg&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=43) at 2021/8/31

class Animal:
    alive = True

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def eat(self):
        print(f"{self.name} is eating")


class LandMammal(Animal):
    pass


class MarineMammal(Animal):
    def __init__(self, name, age, height, swinSpeed):
        #?? 與下列與下列接近相同，為什麼呢?
        # super(MarineMammal, self).__init__(name, age, height)
        # super().__init__會去呼叫#父類別的initializer__init__
        super().__init__(name, age, height) 
        # Animal.__init__(self, name, age, height) 
        self.swinSpeed = swinSpeed

    def swin(self):
        print(f"{self.name} is swimming")

#?? 上面不需要self.name的理由是甚麼呢? 是因為繼承嗎?
class Prey:
    def __init__(self, name):
        Animal.__init__(self, name)
        self.name = name
        
    def flee(self):
        print(f"{self.name} is running away")

# class Predator
#     def flee(self):
#         print(f"{self.name} is following the prey")


dophin = MarineMammal('dophin',14,120,70)
print(dophin.alive)
print(dophin.swinSpeed)
dophin.sleep()
dophin.swin()

""" class PolorBear(LandMammal, Prey):
    pass

tedy = PolorBear('tedy',15,200)
tedy.sleep()
tedy.flee()
 """
# ----多重繼承 mro順序 isinstance issubclass確認----
# 以mro順序找到第一優先執行 (E(B(A),C(A),E))按此順序的概念，(A)有兩個那就以'後'的順序為主，如果有super同名，則向下尋找，再回頭執行

class A:
    def info_self(self):
        print('AAA')
    
    def mynameisA(self):
        print('pathA')

class B(A):
    def info_self(self):
        print("Bpath")
        super().info_self()
        print('BBB')

class C(A):
    def info_self(self):
        print("Cpath")
        super().info_self()
        print('CCC')

class D(A):
    def info_self(self):
        print('DDD')

class E(B, C, D):
    pass

# 跟繼承順序有關
print(E.__mro__)
#(<class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.A'>, <class 'object'>)

F = E()
print(isinstance(F,A)) # True
print(isinstance(F,B)) # True
print(issubclass(C,B)) # False
print(issubclass(C,A)) # True
F.info_self()

""" 包起來的概念
B
C
A
C
B

# class B 裡面有info_self()
# 但發現super()也有，判定可能在後面有，所以尋找下一順位class C
Bpath
# class C 有info_self()
# 但發現super()也有，所以尋找下一順位class A，確定找到，返回並執行完成C
Cpath
DDD
CCC
# 再執行完成B
BBB 
"""

