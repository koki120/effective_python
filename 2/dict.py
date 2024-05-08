from collections.abc import MutableMapping
from typing import Dict
from collections import defaultdict

"""
辞書について
"""

"""
python3.6以降の仕様として、辞書は挿入順を保持するようになった。その前はランダムだった。
"""
baby_names = {"dog": "puppy", "cat": "kitten"}
reversed_baby_names = {"cat": "kitten", "dog": "puppy"}
assert list(baby_names.keys()) == ["dog", "cat"]
assert list(reversed_baby_names.keys()) == ["cat", "dog"]
assert list(baby_names.values()) == ["puppy", "kitten"]
assert list(reversed_baby_names.values()) == ["kitten", "puppy"]
assert list(baby_names.items()) == [("dog", "puppy"), ("cat", "kitten")]
assert list(reversed_baby_names.items()) == [("cat", "kitten"), ("dog", "puppy")]
assert baby_names.popitem() == ("cat", "kitten")
assert reversed_baby_names.popitem() == ("dog", "puppy")


# キーワード引数も順序を保持する。
def func(**kwargs):
    return list(kwargs.items())


assert func(dog="puppy", cat="kitten") == [("dog", "puppy"), ("cat", "kitten")]
assert func(cat="kitten", dog="puppy") == [("cat", "kitten"), ("dog", "puppy")]


# classのインスタンス辞書もdict型なので代入順序を保持する。
class C:
    def __init__(self) -> None:
        self.nix = "cool"
        self.arch = "excellent"


class ReversedC:
    def __init__(self) -> None:
        self.arch = "excellent"
        self.nix = "cool"


assert list(C().__dict__.items()) == [("nix", "cool"), ("arch", "excellent")]
assert list(ReversedC().__dict__.items()) == [("arch", "excellent"), ("nix", "cool")]


"""
辞書の挿入順序に依存するコードを書くときは注意する。
"""


class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    return next(iter(ranks))


votes = {"otter": 1234, "polar": 587, "fox": 863}
ranks = {}
populate_ranks(votes, ranks)
sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)

assert ranks == {"otter": 1, "fox": 2, "polar": 3} == sorted_ranks
assert get_winner(ranks) == "otter"
assert get_winner(sorted_ranks) == "fox"  # 英字順で最初の"fox"がくる


# get_winnerでバグを取り除く対処法
# 1. イテレートの順番が正しいと仮定しない。
def get_winner(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name


# 2. 実行時に型チェックをする。
def get_winner(ranks):
    if not isinstance(ranks, dict):
        raise TypeError("must provide a dict instance")
    return next(iter(ranks))


# 3. 静的ツールで型チェックをする。以下はmypyのstrictモードでエラーが出る。
def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks: Dict[str, int]):
    return next(iter(ranks))


"""
辞書の欠損キーの処理はgetを使う
"""

pan_counter = {
    "White Bread": 5,
    "Croissant": 10,
    "Melon Pan": 7,
    "French Bread": 3,
    "Ciabatta": 8,
}

# NG
key = "Bagel"
if key in pan_counter:
    count = pan_counter[key]
else:
    count = 0
pan_counter[key] = count + 1
assert pan_counter["Bagel"] == 1

# NG
key = "Focaccia"
try:
    count = pan_counter[key]
except KeyError:
    count = 0
pan_counter[key] = count + 1
assert pan_counter["Focaccia"] == 1

# OK
key = "Pretzel"
count = pan_counter.get(key, 0)
pan_counter[key] = count + 1
assert pan_counter["Pretzel"] == 1

# 複雑な型の場合
pan_votes = {
    "White Bread": {"Mike"},
    "Croissant": {"Bob"},
    "Ciabatta": {"Alex", "Brett"},
}

# OK
key = "Pretzel"
if (names := pan_votes.get(key)) is None:
    pan_votes[key] = names = set()
names.add("Duz")
assert pan_votes["Pretzel"] == {"Duz"}


# 自分で辞書が作成できる場合は、defaultdictを使用する。
class PanVotes:
    def __init__(self) -> None:
        self.data = defaultdict(set)

    def add(self, pan, person):
        self.data[pan].add(person)


pan_votes2 = PanVotes()
pan_votes2.add("Pretzel", "Duz")
assert pan_votes2.data["Pretzel"] == {"Duz"}
