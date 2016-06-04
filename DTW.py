#encoding:utf-8
import sys
sys.setrecursionlimit(100000)
num0 = raw_input("请输入一组时间序列：")
num1 = num0.replace(' ','')
num2 = list(num1)
num3 = [int(i) for i in num2]
num4 = raw_input("请再输入一组时间序列：")
num5 = num4.replace(' ','')
num6 = list(num5)
num7 = [int(i) for i in num6]
print num3
print num7
print len(num3)-1
print len(num7)-1
def dtw(n,m,lj_dis = 0):
    if n == 0 and m == 0:
        lj_dis = abs(num3[0] - num7[0])
    elif n == 0 and m > 0:
        for i in range(m+1):
            lj_dis += abs(num3[0] - num7[i])
    elif n > 0 and m == 0:
        for i in range(n+1):
            lj_dis += abs(num3[i] - num7[0])
    elif n > 0 and m > 0:
        lj_dis = min(dtw(n-1,m) + abs(num3[n] - num7[m]),dtw(n,m-1) + abs(num3[n] - num7[m]),dtw(n-1,m-1) + 2*abs(num3[n] - num7[m]))
    return lj_dis
lj_dis = dtw(n = len(num3)-1,m = len(num7)-1)
print "两组时间序列的相似度为：{}".format(lj_dis)
