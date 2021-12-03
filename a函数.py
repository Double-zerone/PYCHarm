import random
def naturalGrowthSeq():#自然增长数列
    result=[0,1]
    for i in range(10):
        result.append(result[-1]+result[-2])
        print(result[i])
#naturalGrowthSeq()
#return 可一次性返回多个值如return a,b,c  (返回值以元组形式保存)
def decomposePrimeFactors():#分解质因数
    val=random.randint(1,100)
    print(val)
    bus = lambda val, i: val%i
    while val!=0:#python 使用 lambda 来创建匿名函数。lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
        for i in range(2,val+1):#range(2,,1)不可用
            if bus(val,i)==0:
                print(i)
                val=int(val/i)
                break
            else:
                pass
decomposePrimeFactors()#KeyboardInterrupt用户中断执行(通常是输入^C)