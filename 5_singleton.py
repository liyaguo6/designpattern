# coding : utf-8
# create by ztypl on 2017/5/25

from abc import abstractmethod, ABCMeta
"""
 （1）单例模式：保证一个类只有一个实例，并提供一个访问它的全局访问点。
    （2）适用场景  当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时

"""
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            print(12)
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance



class MyClass(Singleton):
    def __init__(self, name):
            print(13)
            self.name = name


# class MyClass:
#     def __init__(self, name):
#             self.name = name

a = MyClass("a")
print(14)
print(a)
print(a.name)
#
b = MyClass('b')
# #
print(b)
print(b.name)
b.name = 'xxx'
#
print(a)
print(a.name)


