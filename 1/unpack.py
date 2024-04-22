"""
インデックスではなく複数代入アンパックを使う
"""

# NG
item = ("干将", "莫邪")
assert "干将" == item[0]
assert "莫邪" == item[1]

# OK
first, second = ("干将", "莫邪")
assert "干将" == first
assert "莫邪" == second

# アンパックを使うと1行でスワップができる
first, second = second, first
assert "干将" == second
assert "莫邪" == first


# for文などでもインデックスを使用せず、アンパックを使用する。また、rangeではなくenumerateを使う。

hamburgers = [("照り焼き", 350), ("フィッシュ", 400), ("チキン", 200)]

# NG
for i in range(len(hamburgers)):
    hamburger = hamburgers[i]
    print(f"No.{i}:{hamburger[0]}ハンバーガー {hamburger[1]}円")

# NG
for i, hamburger in enumerate(hamburgers):
    print(f"No.{i}:{hamburger[0]}ハンバーガー {hamburger[1]}円")

# OK
for i, (name, price) in enumerate(hamburgers):
    print(f"No.{i}:{name}ハンバーガー {price}円")
