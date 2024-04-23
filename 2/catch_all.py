"""
catch-allアンパック
"""

# スライスではなく、catch-allアンパックを使用する。
a = [0, 1, 2, 3, 4, 5, 6, 7]
# NG
b = a[:2]
# OK
first, second, *other = a
assert [first, second] == b
