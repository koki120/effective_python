"""
catch-allアンパック
"""

# catch-allアンパックが使用できるなら、スライスではなくcatch-allアンパックを使用する。
a = [0, 1, 2, 3, 4, 5, 6, 7]
# NG
b = a[:2]
# OK
first, second, *other = a
assert [first, second] == b


# catch-allアンパックは*を複数とることができない。構文エラーを起こす。以下がその例である。
# first, *middle, *second_middle, last = [1, 2, 3, 4, 5]


# 指定部は少なくとも一つは必要。以下がその例である。
# *all = [1, 2]


# アスタリスク付きの式は常にlist型を返すので、メモリを使い切らないように注意を払う必要がある。
generator = ((i, hash(str(i))) for i in range(1000))

first, *other = generator  # firstはタプル、otherはリスト

assert len(other) == 999
