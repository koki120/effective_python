"""
bytesとstrの違い
"""

# bitesインスタンスは生の8bit値からなる。通常はASCⅡ
a = b"h\x65llo"

print(list(a))  # [104, 101, 108, 108, 111]
print(a)  # b'hello'

# strインスタンスはUnicodeポイント
b = "\u0068\u0065\u006clo"
print(list(b))  # ['h', 'e', 'l', 'l', 'o']
print(b)  # hello

# TIPS: プログラムの核心部分ではstrを使い文字の
# 符号化を一切仮定しないようにする。

"""
bytesとstrの演算
"""

# OK
assert b"one" + b"two" == b"onetwo"
assert "one" + "two" == "onetwo"


# NG
try:
    b"one" + "two"  # strとbytesは結合できない
except TypeError as error:
    print(error)  # can't concat str to bytes

# OK
assert b"a" < b"b"
assert "a" < "b"

# NG
try:
    "a" < b"b"  # bytesとstrは比較できない
except TypeError as error:
    print(error)  # '<' not supported between instances of 'str' and 'bytes'

assert (b"hello" == "hello") is False  # 同じ文字列でもbytesとstrでは一致しない。

"""
I/O
"""

# NG
try:
    with open("text.bin", "w") as f:
        f.write(b"hello")  # バイナリの書き込みモードは"wb"
except TypeError as error:
    print(error)  # write() argument must be str, not bytes

# OK
with open("text.bin", "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf4\xf6")

# NG
try:
    with open("text.bin", "r") as f:
        data = (
            f.read()
        )  # バイナリの読み込みモードは"rb"。システムのほとんどが符号化をUTF-8でするためバイナリを扱えない。
except UnicodeDecodeError as error:
    print(
        error
    )  # 'utf-8' codec can't decode byte 0xf1 in position 0: invalid continuation byte

# OK
with open("text.bin", "rb") as f:
    data = f.read()
assert data == b"\xf1\xf2\xf3\xf4\xf4\xf6"
