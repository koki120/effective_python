"""
関数について
"""

"""
戻り値が4つ以上の変数ならアンパックを決してしない。
"""


def get_stats(numbers):
    minimum = min(numbers)

    maximum = max(numbers)

    count = len(numbers)

    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        median = sorted_numbers[middle]

    return minimum, maximum, count, average, median


# 順序が入れ替わる可能性がありバグの温床になる
minimum, maximum, average, count, median = get_stats([1, 2, 3, 4, 5, 6, 7])

# TODO:軽量クラスやnamedtupleで代替


"""
Noneを返さずに例外を送出する。
"""


def careful_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return None


result = careful_divide(0, 9)

# Noneだけでなく、結果が０のときもif文が反応する。Falseと等価な戻り値はNoneだけでないのでバグの温床になる。
if not result:
    print("Invalid input")


def careful_divide(x, y):
    try:
        return True, x / y
    except ZeroDivisionError:
        return False, None


# 呼び出し元で握りつぶされる可能性があり、戻り値をtupleにしても完全には解決できない。
_, result = careful_divide(5, 0)


# pythonは関数のインターフェースで例外についての情報を提供してないので適切なドキュメント化が必要。
def careful_divide(x, y):
    """
    Divide x by y.

    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return x / y
    except ZeroDivisionError:
        return None


"""
クロージャが変数スコープとどうかかわるかを把握する。
"""


# クロージャとは下の関数のように自身が定義されたスコープの変数を参照する関数である。
# ここでは、スコープ:sort_priorityの変数groupを参照している関数:helperである。helperはスコープ:sort_priorityで定義されている。
def sort_priority(numbers, group):
    def helper(x):
        if x in group:
            return (0, x)
        else:
            return (1, x)

    numbers.sort(key=helper)


# pythonでは変数が現在のスコープにないときは代入を変数定義として扱う。したがって、helper内でfoundをTrueにしているが返り値はFalseである。
def sort_priority2(numbers, group):
    found = False

    def helper(x):
        if x in group:
            found = True
            return (0, x)
        else:
            return (1, x)

    numbers.sort(key=helper)
    return found


# nonlocalを使えば変数をクロージャの外に持っていくことができる。
def sort_priority2(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        else:
            return (1, x)

    numbers.sort(key=helper)
    return found


# nonlocalを使うのはグローバル変数を使うぐらいの弊害がある。次のように変えるのが良い。
class Sorter:
    def __init__(self, group) -> None:
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        else:
            return (1, x)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorter = Sorter([2, 3, 4, 5])
numbers.sort(key=sorter)
assert sorter.found is True


"""
可変長位置引数を使って、見た目をすっきりさせる。
"""


# *argsという記法を使うと可変長の引数をとることができる。
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(value) for value in values)
        print(f"{message}: {values_str}")


# 値がなくても書く必要がない。
log("hello world")
# *を使うことでシーケンスの要素ごとに位置引数を渡すことができる。
log("number", *numbers)


"""
キーワード引数にオプションの振る舞いを与える
"""


def remainder(number, divisor, is_logging=False):
    result = number % divisor
    if is_logging:
        print(f"{number} % {divisor} = {result}")
    return result


# 利点1:関数呼び出しを初めて読む人でもわかりやすい。
# 利点2:関数定義でデフォルト値を持つことができる。
assert remainder(number=50, divisor=9) == 5
assert remainder(number=50, divisor=9, is_logging=True) == 5


# 利点3:後方互換性を保ちながら関数の引数の拡張ができる。
def remainder(number, divisor, is_logging=False, message=None):
    result = number % divisor
    if is_logging:
        print(f"{message}:{number} % {divisor} = {result}")
    return result


"""
動的なデフォルト引数を指定するときにはNoneとdocstringを使う。
"""
from datetime import datetime
from time import sleep


# NG
# デフォルト引数は関数が定義されたときだけに評価されるのでwhenはいつも同じ時刻になる。
def log(message, when=datetime.now()):
    print(f"{when}:{message}")


log("Hi there!")
sleep(0.1)
log("Hi again!")


# OK
# デフォルト値はNoneにしてdocstringに実際の振る舞いを記述する。
def log(message, when=None):
    """
    whenはデフォルトで現在時刻を出力する。
    """
    if when is None:
        when = datetime.now()
    print(f"{when}:{message}")


log("Hi there!")
sleep(0.1)
log("Hi again!")

import json


# NG
# デフォルト値をNoneにしてないと、予期しない挙動を起こす。
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


# 下記のようにデフォルト値にNoneを指定しないと共有することになる。
foo = decode("bad data")
bar = decode("also bad")
bar["mep"] = 1
assert foo == bar == {"mep": 1}


"""
キーワード専用引数と位置専用引数で明確さを高める。
"""


# *記号で位置引数の終わりとキーワード引数の始まりを表す。呼び出し元にキーワード引数を強制することで可読性を上げることができる。
def safe_division(number, divisor, *, is_logging=False, message=None):
    result = number % divisor
    if is_logging:
        print(f"{message}:{number} % {divisor} = {result}")
    return result


# NG
try:
    safe_division(3, 2, False)
except TypeError as error:
    # safe_division() takes 2 positional arguments but 3 were given
    # 呼び出し元にキーワード引数を強制するのでないとエラーになる。
    print(error)

# OK
safe_division(5, 3, is_logging=True)
