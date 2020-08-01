""""
一回合制游戏，每个角色都有hp和power
hp代表血量，power代表攻击力，hp的初始值为1000
power的吃食值为200
定义一个fight方法：
my_hp=hp-enemy_power
eney_final_hp=enemy_hp-my_power
两个hp进行对比，血量剩余多的人获胜
"""
#定义了一个fight 函数
def fight():
    #定义四个变量，存放你和我的，血量还有攻击力
    my_hp=1000
    my_power=200
    your_hp=1000
    your_power=199
    #一轮对打过后，我的血量和敌人的血量
    my_final_hp=my_hp-your_power
    your_final_hp=your_hp-my_power
    if my_final_hp>your_final_hp:
        print("我赢了")
    elif my_final_hp<your_final_hp:
        print("你赢了")
    else:
        print("平局")
        ###调用fight 函数
fight()

