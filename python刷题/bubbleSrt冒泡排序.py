import time

a = [5, 6, 7, 8, 2, 4, 3, 9, 1]

start = time.perf_counter()


def bubble_srt(a):
    length = len(a)
    k = length - 1  # (2)内循环终止位置
    l = 0
    for i in range(length - 1):  # 升序
        mark = 0
        '''
        (1)优化1（优化外层循环）：mark = 0

    　   若在某一趟排序中未发现气泡位置的交换，则说明待排序的无序区中所有气泡均满足轻者在上，重者在下的原则，因此，冒泡排序过程可在此趟排序后终止。
    为此，在下面给出的算法中，引入一个标签flag，在每趟排序开始前，先将其置为0。若排序过程中发生了交换，则将其置为1。各趟排序结束时检查flag，若未曾
    发生过交换则终止算法，不再进行下一趟排序。优化效果例子:5，4，3，1，2,降序
       
        '''
        for j in range(length - i - 1):
        #for j in range(k):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                mark = 1
                l = j  # 循环里最后一次交换的位置 j赋给pos

                '''
                内层优化:
                   (2)记住最后一次交换发生位置lastExchange的冒泡排序
    
        　　  在每趟扫描中，记住最后一次交换发生的位置lastExchange，（该位置之后的相邻记录均已有序）。下一趟排序开始时，R[1..lastExchange-1]是无
        序区，R[lastExchange..n]是有序区。这样，一趟排序可能使当前无序区扩充多个记录，因此记住最后一次交换发生的位置lastExchange，从而减少排序的趟数。
        
        参考资料
        https://blog.csdn.net/yanxiaolx/article/details/51622286 C语言
        https://www.cnblogs.com/jyroy/p/11248691.html Java
                '''

            #print(a)
        # print("------", a)
        k = l
        if mark == 0:  # (1)若未交换则说明j处顺序升序
            return


run_time = time.perf_counter() - start

print("原始a:", a, "运行时间:", run_time)
b = bubble_srt(a)
print(a)
