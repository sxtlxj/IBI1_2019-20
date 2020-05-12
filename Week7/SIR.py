# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:00:36 2020

@author: DM
"""



def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists) / 2 )
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result
print(MergeSort([100, 2, 3, 4, 5, 6, 90, 7, 21, 23, 45]))

from fractions import Fraction
#Fraction用来做分数运算很好用

def oper_func(dict_x, dict_y):
    '''

    :param dict_x:上一次的计算结果的字典  key为运算过程 value是计算值
    :param dict_y:上一次的计算结果的字典  key为运算过程 value是计算值
    :return:
    '''

    def add(x, y):
        result = x + y
        oper_desc = str(x) + ' + ' + str(y) + ' = ' + str(result)
        return result, oper_desc

    def sub(x, y):
        result = x - y
        oper_desc = str(x) + ' - ' + str(y) + ' = ' + str(result)
        return result, oper_desc


    def sub_reverse(x, y):
        return sub(y, x)

    def mul(x, y):
        result = x * y
        oper_desc = str(x) + ' * ' + str(y) + ' = ' + str(result)
        return result, oper_desc

    def div(x, y):
        if y == 0:
            result = 0
            oper_desc = str(x) + ' * ' + str(y) + ' = ' + str(result)
        else:
            result =  Fraction(x, y)
            oper_desc = str(x) + ' / ' + str(y) + ' = ' + str(result)

        return result, oper_desc

    def div_reverse(x, y):
        return div(y, x)

    dict_result = {}
    opers = [add, sub, sub_reverse, mul, div, div_reverse]
    for kx in dict_x.keys():
        for ky in dict_y.keys():
            for oper in opers:
                if len(kx) != 1:
                    k1 = kx + ' | '
                else:
                    k1 = ''

                if len(ky) != 1:
                    k2 = ky + ' | '
                else:
                    k2 = ''

                result, oper_desc = oper(dict_x[kx], dict_y[ky])

                dict_result[k1 + k2 + oper_desc] = result

    return dict_result


def cal_list(dict_list, calc_result):
    in_list = dict_list.copy()

    for i in range(len(in_list)):
        for j in range(len(in_list)):
            if i < j:
                dict_result = oper_func(in_list[i], in_list[j])
                if len(in_list) == 2:
                    for k in dict_result.keys():
                        calc_result[k] = dict_result[k]
                else:
                    next_list = []
                    next_list.append(dict_result)
                    for k in range(len(in_list)):
                        if k != i and k != j:
                            next_list.append(in_list[k])
                    cal_list(next_list, calc_result)


def cal_main(*args):
    dict_list = []
    for i in range(len(args)):
        dict_list.append({str(i): args[i]})

    calc_result = {}
    cal_list(dict_list, calc_result)

    out_list = []

    for k in calc_result.keys():
         if calc_result[k] == 24:
             #下面一个语句就是用来排版的，把竖线对齐
             k = '|'.join(x.rjust(15) for x in k.split('|'))
             out_list.append(k)

    if not out_list:
        out_list.append('No!!!!!!!!!')

    return out_list


#下面是测试语句
result_list = cal_main(3, 6, 7, 1)

for i in result_list:
    print(i)
