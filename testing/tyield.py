
#yield生成器 next(）来获取生成器里面的下一个值
def provider():
    for i in range(0,10):
        print("开始操作")

        yield i  #相当于return i，挺尸记录上一次的执行位置
        print("结束操作")
p=provider()
#print(next(p))
#print(next(p))
#print(next(p))
#print(next(p))

for i in p:
    print(i)
