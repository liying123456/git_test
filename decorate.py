# 使用装饰器实现单例模式

from functools import wraps


def my_decorate(f):
    @wraps(f)
    def decorate(*args, **kwargs):
        print('decorated called')
        return f(*args, **kwargs)
    return my_decorate


@my_decorate
def main_func():
    print('main_func was called')


print(main_func)