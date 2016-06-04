#encoding:utf-8
import sys
sys.setrecursionlimit(1000000)
num0 = raw_input("键入：")
num1 = num0.replace(' ','')
num2 = list(num1)
num3 = [int(i) for i in num2]
num4 = raw_input("再次：")
num5 = num4.replace(' ','')
num6 = list(num5)
num7 = [int(i) for i in num6]
print num3
print num7
def dtw(n,m,lj_dis = 0):
    if n == 0 and m == 0:
        lj_dis = abs(num3[0] - num7[0])
    elif n == 0 and m > 0:
        for i in range(m):
            lj_dis += abs(num3[0] - num7[m]) 
    elif n > 0 and m == 0:
        for i in range(n):
            lj_dis += abs(num3[0] - num7[n])
    elif n > 0 and m > 0:
        if dtw(n-1,m)<dtw(n-1,m-1)+ abs(num3[n] - num7[m]):
            if dtw(n-1,m)<dtw(n,m-1):
                lj_dis = dtw(n-1,m)+ abs(num3[n] - num7[m])
            else:
                lj_dis = dtw(n,m-1)+ abs(num3[n] - num7[m])
        else:
            if dtw(n-1,m-1)+ abs(num3[n] - num7[m])>dtw(n,m-1):
                lj_dis = dtw(n,m-1)+ abs(num3[n] - num7[m])
            else:
                lj_dis = dtw(n-1,m-1)+ 2*abs(num3[n] - num7[m])
    return lj_dis
lj_dis = dtw(n=23,m=23)
print "de{}".format(lj_dis)
