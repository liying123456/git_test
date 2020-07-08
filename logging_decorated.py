# 使用装饰器实现日志
from functools import wraps

def logit(f):
    @wraps(f)
    def with_logging(*args, **kwargs):
        print(f.__name__ + 'was called')
        return f(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
    return x+x


result = addition_func(4)  # output: addition_func was called