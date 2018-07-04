import time
 
def foo(): # 待装饰函数
    print('in foo()')
 
def timeit(func): # 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
     
    def wrapper(): # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
        start = time.clock()
        func()
        end =time.clock()
        print ('used:', end - start)
     
    return wrapper # 将包装后的函数返回
 
foo = timeit(foo)

foo()

# --------------------------------------------------------------

import time
 
def timeit(func):
    def wrapper(a): # 此处接受带有一个参数的函数调用
        start = time.clock()
        func(a)
        end =time.clock()
        print ('used:', end - start)
    return wrapper
 
def foo(a): # 待装饰函数，并传入一个参数
    print (a)
    
foo = timeit(foo) # 此时foo所指向的函数为装饰器返回的wrapper函数
    
foo('Hello')

# 上述写法与如下写法意义相同
# @timeit
# def foo(a): 
#     print (a)
       
# foo('Hello')

# --------------------------------------------------------------

def add(num):
    def wrapper(a, b): # 此处接受带有两个参数的函数调用
        print(a + b)
    return wrapper

@add
def num(a, b): # 待装饰函数，并传入两个个参数
    pass

num(1, 3) # 运行num，调用wrapper并打印 a + b

# --------------------------------------------------------------

import functools

def log(func):
    @functools.wraps(func) # 此行代码可防止原始function函数名变为wrapper
    def wrapper(*args, **kw): # 此处接受带任意参数的函数调用
        print('Call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def function():
    print('hello')
    
function()