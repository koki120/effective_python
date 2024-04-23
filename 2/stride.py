"""
ストライド
"""

# some_list[start:end:stride]という形式でスライスの増分を指定できる。stride番目ごとに要素を所得する。
a = [0, 1, 2, 3, 4, 5, 6]
b = a[::2]
assert b == [0, 2, 4, 6]

# スライドとスライスの同時使用は可読性を下げるのでしない。
c = a[1::2]
assert c == [1, 3, 5]

# 文字列を逆転する場合にstrideを使用できる。
x = b"python"
y = x[::-1]
assert y == b"nohtyp"

x = "python"
y = x[::-1]
assert y == "nohtyp"

# 符号化によっては文字列を逆転した後にdecodeできないので注意が必要。

# アルファベットはできる。
x = "python".encode("utf-8")
y = x[::-1]
assert y == b"nohtyp"
z = y.decode("utf-8")
assert z == "nohtyp"

# 漢字はできない。(たぶんバイト列の長さの違い)
x = "寿司".encode("utf-8")
y = x[::-1]
assert y == b"\xb8\x8f\xe5\xbf\xaf\xe5"
try:
    z = y.decode("utf-8")
except UnicodeDecodeError as error:
    print(
        error
    )  # 'utf-8' codec can't decode byte 0xb8 in position 0: invalid start byte
