# TASK 6
# def my_decorator(func):
#     def wrapper():
#         print("this is the content of decorator")
#         func()
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello ")

# say_hello()

# TASK 7

# def try_decorator(func):
#     def wrapper(*args,**kwargs):
#         print('start to try')

#         func()
#     return wrapper

# @try_decorator
# def hello():
#     print("Hello")

# hello()

import random
# retry 装饰器：当被装饰函数抛出异常时，最多重试 3 次
def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                result = func(*args, **kwargs)
                print(f'Success! on attempt {i + 1}') 
                return result #return 可以结束def，这样不会继续try
            except Exception as e:
                print(f"Attempt {i + 1} failed with exception:{e}")
        print("All 3 attempts failed")
    return wrapper  #返回包装后的函数

@retry
def random_error():
    return 10/random.choice([0,2])
     
random_error()

@retry
def sum(a,b):
    return a+b

sum(10,13)