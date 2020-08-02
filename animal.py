    ##定义类
class Dog:
    #毛色，黑色，四条腿
    #会吃，会叫，会水
    ##属性
    color="black"
    leg=4

    ##方法，在类的方法中，是使用def关键字定义
    ##def定义的在类外叫做函数function，在类内，叫做method
    def eat(self):
        print("狗在吃")
    def voice(self):
        print ("狗在叫")
    #类的实例化
print(Dog.color)
print(Dog.leg)
Dog().eat()
Dog().voice()









