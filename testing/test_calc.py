#文件名以test_开头，类名以Test_开头，方法名以test_开头，
#注意：一定不要加__init__()方法
import pytest
import yaml

from pythoncode.calc import  Calculator
with open('./datas/calc.yml') as f:
    datas=yaml.safe_load(f)['add']
    adddatas=datas['datas']
    print(adddatas)
    myid=datas['myid']
    print(myid)
class TestCalc:
    def setup(self):
        print("开始计算")
        self.calc = Calculator()
    def teardowm(self):
        print("结束计算")
    #@pytest.mark.add
    #def test_add(self):
        # 实例化计算器
      #  self.calc=Calculator()
        #调用他的相加add（）方法
      #  result=self.calc.add(1,1)
        #断言
    #    assert 2==result
        pass
    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',adddatas,ids=myid)
    def test_add1(self,a,b,expect):
        pass
     #self.calc=Calculator()
        #调用他的相加add（）方法
        #result=self.calc.add(a,b)
        #if isinstance(result,float):
        #   result=round(result,2)
        #断言
      #  assert expect==result

    #@pytest.mark.add
    #def test_add2(self):
        # 实例化计算器
     #   self.calc=Calculator()
        #调用他的相加add（）方法

     #   result=self.calc.add(-1,-1)
        #断言
       #assert -2==result

    @pytest.mark.add
    def test_add3(self):
            # 实例化计算器
            calc = Calculator()
            # 调用他的相加add（）方法
            result = self.calc.add(0.1, 0.1)
            # 断言
            assert 0.2 == result

    @pytest.mark.div
    def test_div(self):
            self.calc= Calculator()
            r=self.calc.div(1,1)
            assert 1==r

    @pytest.mark.div
    def test_div1(self):
               self. calc = Calculator()
               r= self.calc.div(-1, 1)
               assert -1==r