# -*- coding:utf-8 -*-
__author__ = 'Missionary'
__time__ = '2019/4/28 0028 12:42'
import math

points = [(2,3), (10, 1), (3, 25), (23,15),(18,3), (8,9), (12,30), (25,30),(9,2), (13,10), (3,4), (5,6), (22,32), (5,32), (23,9), (19,25),(14,1), (11,25), (26,26), (12,9),(18,9), (27,13), (32,13)]



def colsest(P,n):
    X=list(P)
    Y=list(P)
    X.sort() #预处理,按照X轴进行排序
    Y=sort_y(Y) #预处理,按照Y轴进行排序
    return closest_pair(X,Y,n)





def closest_pair(X, Y, n):
    if n<=3:
        return brute_force(X,n)
    mid=n//2
    Y_Left=[]
    Y_Right=[]
    for p in Y:
        if p in X[:mid]:
            Y_Left.append(p) #Y_left中为直线L左边的所有点且其Y轴坐标值依次增大
        else:
            Y_Right.append(p) #Y_Right中为直线R右边的所有点且其Y轴坐标值依次增大
    dis_left=closest_pair(X[:mid],Y_Left,mid) #递归处理PL
    dis_right=closest_pair(X[mid:],Y_Right,n-mid) # 得到PL和PR中的最小距离
    min_dis=min(dis_left,dis_right)
    strip=[]
    for(x,y) in Y:
        if abs(x-X[mid][0])<min_dis: #只有L+/-min_dis之间 的点才考虑
            strip.append((x,y))
        return min(min_dis,strip_closest(strip,min_dis))



#按照y轴坐标排序
def sort_y(Y):
    return sorted(Y,key=lambda last:last[-1])

# 处理边界内最近点对
def strip_closest(strip, min_dis):
    min_d=min_dis
    for i,(x,y) in enumerate(strip):
        for j in range(i+1, 8): # 只需要考虑最多7个点
            if i+j<len(strip):
                temdis=distance(strip[i],strip[j])
                if temdis<min_d:
                    min_d=temdis
    return min_d
#计算两点之间的欧拉距离
def distance(a,b):
    return math.sqrt(math.pow((a[0] - b[0]), 2) + math.pow((a[1] - b[1]), 2))

# 当点数小于3时, 直接计算最小距离
def brute_force(X,n):
    min_d=distance(X[0],X[1])
    for i,(x,y) in enumerate(X):
        for j in range(i+1,n):
            if distance(X[i],X[j])<min_d:
                min_d=distance(X[i],X[j])
    return min_d

print(colsest(points,len(points)))