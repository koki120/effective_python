"""
関数デコレータについて
"""

"""
関数デコレータを定義するときはfunctools.wrapsを使う。
"""


# NG
def trace(func):
    def wrapper(*args, **kwargs):
        # *argsは可変長の引数、**kwargsはキーワード引数を表す。
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args!r},{kwargs!r}) -> {result!r}")
        return result

    return wrapper


# @traceは fibonacci = trace(fibonacci) と等価である。
@trace
def fibonacci(n: int):
    """
    Return the n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


# 欠点0:名前が表示されない。
print(fibonacci)  # <function trace.<locals>.wrapper at 0x7fd4d4177a60>

# 欠点1:組み込み関数のhelpでfibonacciのdocstringが出力されなくなる。
help(fibonacci)

# 欠点2:オブジェクトシリアライザーがエラーになる。
import pickle

try:
    pickle.dumps(fibonacci)
except AttributeError as error:
    print(error)  # Can't pickle local object 'trace.<locals>.wrapper'


from functools import wraps


# OK
def trace(func):
    @wraps(func)  # 内部関数のすべてのメタデータが外部関数に複製される。
    def wrapper(*args, **kwargs):
        # *argsは可変長の引数、**kwargsはキーワード引数を表す。
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args!r},{kwargs!r}) -> {result!r}")
        return result

    return wrapper


@trace
def fibonacci(n: int):
    """
    Return the n-th Fibonacci number
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci)  # <function fibonacci at 0x7f9b92386040>
help(fibonacci)
print(pickle.dumps(fibonacci))
