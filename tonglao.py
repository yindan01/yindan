class TongLao:
#定义童老的属性
    def __init__(self,tonglao_hp,tonglao_power):
        self.tonglao_hp = tonglao_hp
        self.tonglao_power = tonglao_power
#用def定义童老的方法,传入一个name参数
    def see_people(self,name):
        self.name=name
#如果传入"无崖子",刚打印"师弟!!!!"
        if self.name == "WYZ":
            print("师弟!!!")
#如果传入"李秋水",则打印"呸,贱人"
        elif self.name == "李秋水":
            print("呸,贱人")
#如果传入"丁春秋",则打印"叛徒!我杀了你"
        elif self. name == "丁春秋":
            print("叛徒!我杀了你")
#定义fight_zms的方法,调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，
    def fight_zms(self,tonglao_hp,tonglao_power,your_hp,your_power):
        self.tonglao_hp = tonglao_hp/2
        self.tonglao_power = tonglao_power*10
        self.your_hp = your_hp
        self.power = your_power
#进行一回合制对打,打完之后，比较双方血量。血多的一方获胜。
        self.tonglao_hp = tonglao_hp -your_hp
        self.your_hp = your_hp - tonglao_hp
        if self.tonglao_hp > your_hp:
            print("哈哈哈,你输了")
        if self.tonglao_hp < your_hp:
            print("童佬的折梅手没什么了不起的")
#定义一个xuzhu类,继承童姥
class XuZhu(TongLao):
#XuZhu只会念经"read"
    def read(self):
        print("罪过罪过")
#构造方法
    def __init__(self):
        self.read()
#童姥实例化,传童佬的血量和武力值
tonglao = TongLao(1000,100)
#see_people的方法 name参数为 李秋水
tonglao.see_people("李秋水")
#折梅手的方法传 童姥的血量和武力值,敌人的血量和武力值
tonglao.fight_zms(1000,100,1000,100)
#实例化XuZhu类
xz = XuZhu






