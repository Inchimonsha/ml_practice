import math

import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def task1():
    v = np.array([1, 2, 3, 4])
    vz = np.zeros(4)
    print(v)
    print(vz)

def task2():
    b = np.array(input().split(), int)
    print(b)

def task3():
    # a = np.array(input().split(), int)
    # b = np.array(input().split(), int)
    # print(((a[3]-a[0])==(b[3]-b[0])).all())

    a, b = [np.array(input().split(), int) for _ in range(2)]
    print(np.all(a[3:] - a[:3] == b[3:] - b[:3]))

def task4():
    p1 = np.array([0,3,1])
    p2 = np.array([1,2,-1])
    v = p2-p1
    len_v = round(np.sqrt((v**2).sum()), 1)
    print(len_v)

def task5():
    p1 = np.array([0,0,0])
    p2 = np.array([1,1,0])
    p3 = np.array([2,-2,0])
    p4 = np.array([2,2,2])
    p5 = np.array([3,1,-1])
    arr_p = np.array([p1,p2,p3,p4,p5])
    v1 = p2-p1
    v2 = p3-p2
    v3 = p4-p3
    v4 = p5-p4
    arr_v = np.array([v1, v2, v3, v4])
    arr_v2 = arr_p[1:]-arr_p[:-1]
    len_v = round(np.sqrt((v1**2).sum()) + np.sqrt((v2**2).sum()) + np.sqrt((v3**2).sum()) + np.sqrt((v4**2).sum()), 1)
    len_v2 = round(np.sum(np.linalg.norm(arr_v2,axis=1)), 1) # 1-строки 0-столбцы axis
    print(len_v2)

    maxv5 = np.linalg.norm(p5, ord=np.inf)
    print(maxv5)

def task6():
    n = int(input())
    arr = [np.array(0.5**(i+1)) for i in range(n)]
    len = np.linalg.norm(arr,ord=1)
    print(len)

def task7():
    sarr = np.array([[1,22,3],
            [31,4,5],
            [5,6,7]])
    v_arr = np.round(sorted(np.linalg.norm(sarr, axis=1, ord=2)),1)
    print(*v_arr)

    #linear_operation_vector
def add_v1():
    v1 = np.array([1,2,3])
    v2 = np.array([4,5,6])
    v = np.add(v1, v2)
    v = v1 + v2
    print(v)

def taskv1():
    v = [np.array(input().split(), float) for _ in range(int(input()))]
    print(np.sum(v, axis=0))

def taskv2():
    # arr_v = np.zeros(2)
    # for i in range(2):
    #     vin = np.array(input().split(), dtype=float)
    #     arr_v += np.array(*[(vin[2:] - vin[:2])])
    # #arr_v = [np.array(input().split(), dtype=float) for _ in range(2)]
    # print(arr_v)
    # print(np.sum(arr_v))

    arr = sum(np.array(input().split(), dtype=float) for _ in "ab")
    print(np.linalg.norm(arr[2:]-arr[:2]))

def taskv3():
    #найти точку C, которая делит вектор AC в отношении 1/k
    a, b = [np.array(input().split(), dtype=float) for _ in "ab"]
    k = int(input())
    print(*np.round((a+b*k)/(k+1), 2))

def taskv4():
    #найти точку C и D, которые делят вектор AB в отношении 1/3
    # arr_v = [np.array(input().split(), dtype=float) for _ in "ab"]
    # print(*np.sum(arr_v, axis=0)/3)
    # print(*np.sum(arr_v, axis=0)/(3/2))

    arr_v = np.array([[3,-5,2],[5,-3,1]])
    print(*np.round(arr_v[0]+(arr_v[1]-arr_v[0]) / 3, 2))
    print(*np.round(arr_v[0]+(arr_v[1]-arr_v[0]) / (3/2),2))

def task_linear_zavisimost():
    # a*A + b*B + c*C = 0
    # (1, |1|, 2)
    # (2, |1|, 1)
    # (3, |2|, 2)
          #=0
    # 1a + 2b + 3c = 0
    # 1a + 1b + 2c = 0
    # 2a + 1b + 2c = 0
    # если a, b, c = 0, то линейно независимы
    print()

def task_angle_basis():
    arr = np.array(input().split(), dtype=float)
    #print(*np.round(arr[:3]/np.sqrt(np.sum(arr**2)), decimals=2))
    print(*np.round(arr/np.linalg.norm(arr), decimals=2))

def task_angle_module():
    #модуль и угол между Ox и вектором даны
    module = float(input())
    angle_vOx = float(input())
    print(f"{np.round(module*np.cos(angle_vOx),2)} {np.round(module*np.sin(angle_vOx), 2)}")

def task_vmany():
    a = np.array(input().split(), dtype=float)
    b = np.array(input().split(), dtype=float)
    c1 = a + b
    c2 = b - a
    c3 = -a * 2
    c4 = b / 2

    # print(*np.round([np.linalg.norm(a), np.linalg.norm(c1), np.linalg.norm(c4 + c3)], 2))
    # print(*np.round([b/np.linalg.norm(b), c2/np.linalg.norm(c2)], 2))

    print(*np.round([*map(np.linalg.norm, (a, c1, c4 + c3))], 2))
    print(*np.round([*map(lambda x: x / np.linalg.norm(x), (b, c2))], 2))

import numpy
def scal_qrt():
    v1 = numpy.array([1, 2, 3])
    v2 = numpy.array([2, 4, 6])
    a = 60
    # print(numpy.sum(v1*v2)/(numpy.linalg.norm(v1) + numpy.linalg.norm(v2)))
    # в ортонормированном базисе a = 0*
    # v1 * v2 = v1i1 * v2i1 + v1i2 * v2i2 + ...
    print(numpy.sum(v1*v2))
    print(numpy.dot(v1, v2))
    print(numpy.sum(v1*v2)*numpy.cos(a))

def projection_a_to_b():
    a = numpy.array([1, 1, 0])
    b = numpy.array([2,1,-1])
    # a* = a * b / |b|
    print(round(sum(a*b)/numpy.linalg.norm(b), 2))
    # numpy.linalg.norm(b) = sqrt(b1**2 + b2**2)

def scal_qrt_modest():
    v = np.array([1, 2, 3])
    w = np.array([4, 5, 6])
    result = np.dot(v, w)
    print("Скалярное произведение1:", result)
    result = v.dot(w)
    print("Скалярное произведение2:", result)
    result = v @ w
    print("Скалярное произведение2:", result)

def cos_vct():
    a, b = [np.array(input().split(), dtype=float) for _ in "ab"]
    a_len, b_len = map(np.linalg.norm, (a, b))
    print(a@b/(a_len*b_len))

def multiply_vectors(vc1: np.array, vc2: np.array):
    # a = a1*i + a2*j + a3*k
    # b = b1*i + b2*j + b3*k
    # a x b = (a2*b3 - a3*b2)*i + (a3*b1 - a1*b3)*j + (a1*b2 - a2*b1)*k
    mult = [(vc1[1]*vc2[2] - vc1[2]*vc2[1]), (vc1[2]*vc2[0] - vc1[0]*vc2[2]), (vc1[0]*vc2[1] - vc1[1]*vc2[0])]

    np.array([3, 2, 1]), np.array([-1, 2, 3])

    c = np.cross(vc1, vc2)
    c2 = np.cross(vc1, vc2, axisa=-1, axisb=-1, axisc=-1, axis=None)
    print("Вектор a:", vc1)
    print("Вектор b:", vc2)
    print("Векторное произведение a x b:", c)

    # Создаем одномерные массивы
    a2 = np.array([1, 2, 3])
    b2 = np.array([4, 5, 6])
    # Вычисляем векторное произведение с указанием осей
    c2 = np.cross(a, b, axisa=0, axisb=0, axisc=0)
    print("Вектор a:", a2)
    print("Вектор b:", b2)
    print("Векторное произведение a x b с указанием осей:", c2)

    return mult

def mult_multiply_vectors():
    # Создаем многомерные массивы
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8, 9], [10, 11, 12]])
    # Вычисляем векторное произведение
    c = np.cross(a, b)
    print("Массив a:\n", a)
    print("Массив b:\n", b)
    print("Массивное векторное произведение a x b:\n", c)

def multiply_vc_sin():
    a, b = [np.fromstring(input(), dtype=float, sep=' ') for _ in '12']
    a_, b_, c_ = map(np.linalg.norm, (a, b, np.cross(a, b)))
    print(np.round(c_ / (a_ * b_), 2))

def is_kolinear():
    a = np.array(input().split(), dtype=float)
    b = np.array(input().split(), dtype=float)
    print(all(np.cross(a, b) == 0))

def mixed_multiply():
    # a×(b×c⃗)
    # a×(b×c)=(a*c)×b−(a*b)×c.
    A = np.array([1, 2, 3])
    B = np.array([4, 5, 6])
    C = np.array([7, 8, 9])
    # Вычисление смешанного произведения
    result = np.dot(A, np.cross(B, C))
    # Вывод результата
    print("Смешанное произведение: ", result)

def double_cross():
    # Векторы A, B и C
    A = np.array([1, 1,0])
    B = np.array([-1,2,1])
    C = np.array([1,1,1])
    # Вычисление первого векторного произведения
    cross_product_1 = np.cross(B, C)
    # Вычисление второго векторного произведения
    double_cross_product = np.cross(A, cross_product_1)
    # Вывод результата
    print("Двойное векторное произведение: ", double_cross_product)

def t17():
    A,B,a = [np.array(input().split(), dtype=float) for _ in "abc"]
    AB = B - A
    print(AB)
    mod_AB = np.linalg.norm(AB)
    print(np.round(mod_AB, 2))
    cos_s = [np.round(np.sum(1*i)/mod_AB, 2) for i in AB]
    print(cos_s) # np.round(BA / norm_BA, 2)
    C = B + a
    print(C)

def sort():
    arr = [52, 49, 31, 53, 44, 36, 50, 50, 43, 44, 45, 43, 52, 48, 42]
    print(np.sort(arr))

if __name__ == '__main__':
    sort()
