import math
import matplotlib.pyplot as plt
import numpy as np
from filetest import radcar, coor, coorbike, radbike, Vcar
from gjk3 import *

def recover(a, b, c, car):
    if car:
        wheelbase = 2.865
        wholelength = 4.825
        wholewidth = 1.835
    else:
        wheelbase = 1.402
        wholelength = 1.986
        wholewidth = 0.816
    def distance_to_coodinate(d, k, b, x1, y1, down):
        # 点(x1, y1)から距離dだけ離れた2点の座標を計算
        if down:
            if k < 0:
                x = x1 + d / math.sqrt(1 + k**2)
                y = k * x + b
            else:
                x = x1 - d / math.sqrt(1 + k**2)
                y = k * x + b
            x = round(x, 3)
            y = round(y, 3)
            return (x, y)
        else:
            if k < 0:
                x = x1 - d / math.sqrt(1 + k**2)
                y = k * x + b
            else:
                x = x1 + d / math.sqrt(1 + k**2)
                y = k * x + b
            x = round(x, 3)
            y = round(y, 3)
            return (x, y)
    def linear_func_b(k, x1, y1):
        b = y1 - k * x1
        return b

    def linear_func(A, B):
        k = (B[1] - A[1]) / (B[0] - A[0])
        return k

    def distance(A, B):
        d = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
        return d
    kAB = math.tan(c)
    if car:
        B = distance_to_coodinate((1/2 * (wholelength-wheelbase)), kAB, linear_func_b(kAB,A[0],A[1]), A[0], A[1],True)
        G = distance_to_coodinate(wholelength, kAB, linear_func_b(kAB,A[0], A[1]), B[0], B[1], False)
        D = distance_to_coodinate((1/2 * wholewidth), -1/kAB, linear_func_b(-1/kAB, B[0],B[1]), B[0], B[1], True)
    else:
        B = distance_to_coodinate((1/2 * (wholelength-wheelbase)), kAB, linear_func_b(kAB,A[0],A[1]), A[0], A[1],False)
        G = distance_to_coodinate(wholelength, kAB, linear_func_b(kAB,A[0], A[1]), B[0], B[1], True)
        D = distance_to_coodinate((1/2 * wholewidth), -1/kAB, linear_func_b(-1/kAB, B[0],B[1]), B[0], B[1], False)
    C = 2*B[0]-D[0],2*B[1]-D[1]
    F = G[0]-B[0]+D[0],G[1]-B[1]+D[1]
    E = G[0]-B[0]+C[0],G[1]-B[1]+C[1]
    return C, D, F, E

CAR = []
BIKE = []
minD = []
for i in range(len(radbike)):
    A = coor[i]
    c = radcar
    CAR = recover(A[0], A[1], c[i], True)
    A = coorbike[i]
    d = radbike
    BIKE = recover(A[0], A[1], d[i], False)
    x = Vcar[i]
    rect1 = np.array(CAR)
    rect2 = np.array(BIKE)
    distance, point1, point2 = closest_distance(rect1, rect2)
    minD.append(distance)
    if distance == 0:
        print("两个矩形相交")
        print(f"今の車の速度は{x}")
        
        minD.clear
        break
    else:
        print(f"两个矩形最近距离为 {distance}")
print(min(minD))
        # print(f"最近点分别为 {point1} 和 {point2}")
    

