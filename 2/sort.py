"""
ソートについて
"""

# listのsortメソッドはほとんどの組み込み型で提供されている。
numbers = [324, 45423, 563, 21, 45, 534643]
numbers.sort()
assert numbers == [21, 45, 324, 563, 45423, 534643]

strings = ["🗻", "🐡", "🍖"]
strings.sort()
assert strings == ["🍖", "🐡", "🗻"]

# tupleはデフォルトで比較可能。tuple同士では、tupleの各位置の要素を順に比較していく。
tuples = [(123, "🍖", "🐄"), (123, "🐡"), (23, "🗻")]
tuples.sort()
assert tuples == [(23, "🗻"), (123, "🍖", "🐄"), (123, "🐡")]


# classは比較を定義しないとsortを呼び出すことはできない。以下のtoolsに対して、sortを呼び出すとエラーになる。
class Tool:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f"Tool({self.name}, {self.weight})"

tools = [
    Tool("level", 3.5),
    Tool("hammer", 1.55),
    Tool("screwdriver", 0.5),
    Tool("chisel", 0.25),
]


# クラスをソートしたい場合は、keyパラメータを使用する。key関数の第一引数はリストの要素が渡され、戻り値は比較可能な値である必要がある。
tools.sort(
    key=lambda x: (-x.weight, x.name)
)  # [Tool(level, 3.5), Tool(hammer, 1.55), Tool(screwdriver, 0.5), Tool(chisel, 0.25)]

# TIPS: pythonのソートは安定ソートアルゴリズムが使われているので、同じ値の場合は順番は変わらない。
# この性質を利用して、sort(key=lambda x:(x.weight, -x.name))を下のように実現できる。文字列（x.name）にマイナス演算子(-)は使えないので、注意。

tools2 = [
    Tool("circular saw", 5),
    Tool("jackhammer", 40),
    Tool("drill", 4),
    Tool("sander", 4),
]

tools2.sort(key=lambda x: x.name, reverse=True)
tools2.sort(
    key=lambda x: x.weight
)  # [Tool(sander, 4), Tool(drill, 4), Tool(circular saw, 5), Tool(jackhammer, 40)]
