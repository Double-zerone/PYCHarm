a = [5, 6, 7, 8, 2, 4, 3, 9, 1]
'''
算法可视化网站:https://visualgo.net/zh/sorting
'''

# 快速排序
def select_sort(x):
    length = len(x)
    for i in range(length - 1):  # 升序
        min_x = i
        for j in range(i + 1, length):  # 确保minx不等于j
            if x[min_x] > x[j]:
                min_x = j
        x[i], x[min_x] = x[min_x], x[i]
    return x


# b = select_sort(a)
# print(b)

# 插入排序
'''
基于基本有序最好用,是稳定排序
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
'''


def insert_sort(x):
    length = len(x)
    for i in range(1, length):
        end = i;  # 无序序列第一个值,也是要插入的值

        while end > 0:
            if a[end] < a[end-1]:
                a[end-1], a[end] = a[end], a[end-1]
            end -= 1
    return x


# b = insert_sort(a)
# print(b)

#归并排序

