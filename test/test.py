def equality_operator():
    a = 5
    str = "5"
    print(not a == 5)
    print(a > 4 and a%2==1)
    print(a > 4 or not a.is_integer())
    print(str.isalnum() or str.isalpha() or str.isdecimal())

import os
def file_system():
    dirpath = os.getcwd()
    print(dirpath)
    with open("text.txt", "w") as file:
        file.write("data\nherih\nhufew")
    print(file.closed)

    file = open("text.txt")
    print(file.read())
    print("\n~~~~~~~~\n")
    file.seek(2)
    print(file.read())
    print("\n~~~~~~~~\n")
    file.seek(0)
    list = file.readlines()
    print(list)
    print("\n~~~~~~~~\n")
    print(file.closed)
    file.close()
    print(file.closed)
    print("\n~~~~~~~~\n")
    with open("text.txt", mode="w") as flr:
        #data = flr.read() error
        flr.write("fff")
        #r \ w \ a \ r+ \ w+
    print("\n~~~~~~~~\n")
    with open("text.txt", mode="r+") as flall:
        flall.seek(0, 2)
        flall.write("\nHello last")
        flall.seek(0)
        print(flall.read())
    print("\n~~~~~~~~\n")
    with open("datasets/img.txt", "r+b") as imgread:
        data = imgread.read()
        for i in data.split(): print(int(i))

from collections import OrderedDict
from collections import namedtuple
def list_dict():
    ls1 = list([1, 2, 3])
    ls2 = [1, 2, 3, 4]
    print(ls1)
    print(ls2)

    dc = dict()
    dc["l1"] = 1
    dc["l2"] = 2
    print(dc.values(), dc.get("l2"), dc.items())

    dcord = OrderedDict()
    dcord["l1"] = 1
    dcord["l2"] = 2
    print(dcord.values(), dcord.get("l2"), dcord.items())

    cort = ("John", "Silver", 22)
    print(*cort)

    player = namedtuple("Player", "name age rating")
    players = [player("Misha", 12, 123), player("Olya", "ten", 126)]
    print(players[1].age)

def truefalse():
    if True: print("true")
    elif a > 4: print("false")
    else: print()

def alltr():
    arr = [("oleg", 270),("anna",300),("misha", 1050)]
    bl = all(rating > 200 for _, rating in arr)
    print(bl)

def zipA():
    arr1 = [1,2,3,4]
    str = "abc"
    lsf = zip(arr1, str)
    print(list)
    zipped_list = list(lsf)
    print(zipped_list)

def codeAskii():
    char = "a"
    num = 97
    print(ord(char))
    print(chr(num))

def helpF():
    '''
    DOCSTRING: Information about the function
    INPUT: no inputs
    OUTPUT: help
    :return:
    '''
    print(help(helpF))

def Args(name = "default"):
    return name

def manyArgs(*args):
    print(args)

def pairArgs(**pair):
    for i,j in pair.items():
        print(i, j) #pairArgs(carl=1, olya=2)

def square(n):
    return n*n
def mapping():
    print(list(map(square, [1,2,3,4,5])))

def is_adult(age):
    return age > 16
lamb = lambda age: age > 18
def filtering():
    print(list(filter(is_adult,[12,23,34,45,1])))
    print(list(filter(lamb, [12,23,34,45,1])))
    print(list(filter(lambda age: age > 18, [12,23,34,45,1])))

glob_greeting = "hello"
def globF():
    global glob_greeting
    print(glob_greeting)
    glob_greeting = "hi"
    print(glob_greeting)
    # wrong ex

def funct(func):
    print("start func")
    def hello():
        print(func)
        print(f"hello {func()}")
    return hello

#@funct
def hello_Jane(name):
    print("start hello_jane")
    return "Jane"

from timeit import default_timer as timer
import math
import time
def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print(f"function {func.__name__} took {end-start} for execution")
    return inner
@measure_time # декоратор
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))
    # вызов factorial(100)

from functools import wraps
def log_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f"calling func {func}")
        func(*args, **kwargs)
        print(f"func {func} finished")
    return wrap
@log_decorator
def hello():
    print("hello")
def start_wraps_decorator():
    hello()
    help(hello)

file = None
def exception():
    try:
        file = open(r"blabla.txt")
        data = file.read()

        res = 10 / 0
        print("yea")
        return
    except ZeroDivisionError as ex:
        print(f"error: {ex}")
    except:
        print("unknown error")
    finally:
        print("finally")
        if file:
            file.close()

def raiser():
    a = 20
    if a == 10:
        raise ValueError("a = 10")
    else: raise InvalidException("a != 10")

class InvalidException(Exception):
    """Raised"""

class Character():
    DEATH_HEALTH = 100 # const
    MAX_SPEED = 100

    def __init__(self, race, damage=10, weapon="knife"):
        self.__ch_race = race # private
        self.ch_damage = damage
        self.ch_weapon = weapon
        self._health = 100 # protected

        self._current_speed = 20

    @property
    def health(self, ):
        return self._health

    @property
    def race(self):
        return self.__ch_race

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if (current_speed > 100): self._current_speed = 100
        elif current_speed < 0: self._current_speed = 0
        else: self._current_speed = current_speed

    def hit(self, damage):
        self.DEATH_HEALTH -= damage

    def is_dead(self):
        return self._health == Character.DEATH_HEALTH

def init_Character():
    unit = Character("Elf")
    print(unit.ch_weapon)
    print(type(unit))
    unit._Character__race = "Ork"
    print(unit._Character__race)
    unit._health = 10
    print(unit._health)
    print(unit._health)
    unit.current_speed = 1000
    print(unit.current_speed)

class StaticClass:
    x = 1

def changeStaticClass():
    StaticClass.x = 2
    cl = StaticClass()
    cl.x = 5
    print(f"via instance {cl.x}")
    print(f"via class {StaticClass.x}")

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f"{self.month}-{self.day}-{self.year}"

    @classmethod
    def millenium_c(cls, month, day): # factory method
        return cls(month, day, 2000)

    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)

def init_Date():
    d1 = Date.millenium_c(2, 20)
    d2 = Date.millenium_s(2, 20)
    print(d1.display())
    print(d2.display())

class DateTime(Date):
    def display(self):
        return f"{self.month}-{self.day}-{self.year} - 00:00:00pm"

def init_DateTime():
    dt1 = DateTime(10, 10, 1990)
    dt2 = DateTime.millenium_c(10, 10)
    dt3 = DateTime.millenium_s(10, 10)
    print(isinstance(dt1, DateTime))
    print(isinstance(dt2, DateTime))
    print(isinstance(dt3, DateTime))
    print(dt1.display())
    print(dt2.display())
    print(dt3.display())

class StrConverter:
    @staticmethod
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode("utf-8")
        else:
            value = bytes_or_str
        return value

    @staticmethod
    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode("utf-8")
        else:
            value = bytes_or_str
        return value

def init_strConverter():
    print(StrConverter.to_str("\x41"))
    print(StrConverter.to_str("A"))

    print(StrConverter.to_bytes("\x41"))
    print(StrConverter.to_bytes("A"))

class Shape:
    def __init__(self):
        print("shape created")

    def area(self):
        raise NotImplementedError("cant instantiate an abstract class")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    def draw(self):
        print("draw rectangle")

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    def draw(self):
        print("draw triangle")

def init_Shapes():
    sh = Shape()
    rectangle = Rectangle(10, 5)
    triangle = Triangle(3, 3, 3)

    #print(sh.area())
    print(rectangle.area())
    print(triangle.area())

    for shape in [rectangle, triangle]:
        shape.draw()

class Animal:
    famine = 10
    def __init__(self):
        super().__init__()
        self.health = 100

    def eat(self):
        self.health += self.famine

class Mammol():
    def __init__(self):
        super().__init__()
        self.speed = 20

class Carnivour(Animal, Mammol):
    def __init__(self):
        super().__init__()
        self.damage = 20

    def self_hit(self):
        self.health -= self.damage

def init_Cranivour():
    wolf = Carnivour()
    wolf.self_hit()
    print(wolf.health)
    print(wolf.speed)

class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

class BinaryTree(ToDictMixin):
    def __init__(self, value,
                 left = None,
                 right = None):
        self.value = value
        self.left = left
        self.right = right

def init_tree():
    tree = BinaryTree(10,
                      left=BinaryTree(100, right=BinaryTree(1)),
                      right=BinaryTree(12, left=BinaryTree(6)))
    print(tree.to_dict())

from abc import ABC
from abc import abstractmethod
class Shape_Abs(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        pass

    def perimeter(self):
        print("calc per")

    def drag(self):
        print("drag func")

class Triangle_Abc(Shape_Abs):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f"draw {self.a}")

    def perimeter(self):
        super().perimeter()
        return self.a + self.b + self.c

    def drag(self):
        super().drag()
        print("additional act")

def init_Abc_Shape():
    t = Triangle_Abc(10, 10, 10)
    print(t.perimeter())
    t.drag()

class Road:
    def __init__(self, length):
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self):
        return f"a road of length {self.length}"

    def __del__(self):
        print(f"the road has been destroyed")

def init_road():
    road = Road(20)
    print(road)
    print(len(road))
    del road

class RecSar():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.race = "Demon"

# singletone
def init_RecSar():
    recsar = RecSar()
    NONrecsar = RecSar()
    NONrecsar.race = "NON Demon"
    print(recsar.race)
    print(NONrecsar.race)

import random
from string import digits
from string import punctuation
from string import ascii_letters
def password():
    symbols = ascii_letters + digits + punctuation
    secure_random = random.SystemRandom()
    password = "".join(secure_random.choice(symbols)
                       for i in range(20))
    print(password)

# thunder методы ___...___
# декораторы
#

class Character_serialisation():
    def __init__(self, race, armor = 20, damage = 10):
        self.race = race
        self.armor = armor
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == 0

    # def __getstate__(self):

    def __setstate__(self, state):
        self.race = state.get("race", "Elf")
        self.damage = state.get("damage", 10)
        self.armor = state.get("armor", 20)
        self.health = state.get("health", 100)

def init_Char_serialisation():
    c = Character_serialisation("Elf")
    c.hit(10)
    print(c.health)

    import pickle
    with open(r"datasets/game_state.bin", "w+b") as f:
        pickle.dump(c, f)

    c = None
    print(c)

    with open(r"datasets/game_state.bin", "rb") as f:
        c = pickle.load(f)
    print(c.health)
    print(c.__dict__)

def repr():
    class character:
        def __init__(self, race, armor=20, damage=10):
            self.race = race
            self.armor = armor
            self.damage = damage
            self.health = 100
        def __repr__(self):
            return f"character(character {self.race} with {self.armor})"
        def __str__(self):
            return f"character {self.race} with {self.armor}"
        def __eq__(self, other):
            if isinstance(other, character):
                return self.race == other.race
            return False
        def __ne__(self, other):
            print("ne is compile")
            return not self.__eq__(other)

    eval("print(\"hello\")")
    char1 = character("elf")
    print(char1)
    # d = eval(repr(char1))
    # print(type(d))
    char2 = character("elf")
    print(char1 == char2)

import copy
def copy_deepcopy():
    list1 = [1, 2, 3, [1, 2, 3]]
    list2 = list1.copy()
    list1.append(2222)
    print(list1, "~~~~", list2)
    list2.append(55)
    print(list1, "~~~~", list2)

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Line:
        def __init__(self, x : Point, y : Point):
            self.pt1= x
            self.pt2 = y
        def __copy__(self):
            pass
        def __deepcopy__(self, memo):
            pass

    pt1 = Point(12, 66)
    pt2 = copy.copy(pt1)
    print(pt1.x, pt1.y, "~~~~", pt2.x, pt2.y)

    ln1 = Line(pt1, pt2)
    ln2 = copy.copy(ln1)
    ln1.pt1.x = 100
    ln2.pt1 = Point(22, 2222)
    print(ln1.pt1.x, ln1.pt2.y, "~~~~", ln2.pt1.x, ln2.pt2.y)

def typet():
    type Point = tuple[float, float]
    return 0

from collections import Counter
def counter_list():
    list = [1,1,1,2,3,3,4,4,4,4,4,4,0,0,0]
    print(Counter(list))
    str = "aabacccda"
    print(Counter(str))

def title_str():
    str = "hello world"
    print(str.title())

def numOfBytes():
    str = "hello world"
    print(len(str.encode("utf8")))

from itertools import islice
def generator():
    list = ['a', 'b', 'c', 'd', 'e']
    print(*islice(list, 0, None, 2))

    # expensive_ads = (a for a in ads_list if a["bid"] > 600)
    # expensive_in_interval = (a for a in expensive_ads if a["date"] > date_start and a["date"])

def conv_dict_to_list():
    dict = {"Nick":22, "Bob":12, "Olya": 30}
    li = list(dict.items())
    print(li)

def stepTask1():
    X = np.array([[1, 60],
                  [1, 50],
                  [1, 75]])
    y = np.array([10, 7, 12])
    print(np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y))

def stepTask2():
    import urllib
    from urllib import request
    import numpy as np

    # fname = input()  # read file name from stdin
    fname = "https://stepik.org/media/attachments/lesson/16462/boston_houses.csv"
    f = urllib.request.urlopen(fname)  # open file from URL
    data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

    X = np.copy(data)
    X[:, 0] = 1
    y = np.copy(data)[:, 0]

    print(np.round(np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y), 4))

def meshgrid():
    x = [1, 2, 3]  # Размеры по оси X
    y = [1, 2, 3]  # Размеры по оси Y

    X, Y = np.meshgrid(x, y)
    print(X, Y)

import numpy as np
if __name__ == '__main__':
    x = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
    w = np.array([[1], [2], [3]])
    print(x.dot(w))