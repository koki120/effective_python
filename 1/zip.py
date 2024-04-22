import itertools

"""
イテレーターを並列に処理するにはzipを使う。
"""

names = ["🍖", "🐡👹", "🥬🏠"]
counts = [len(n) for n in names]

# NG
max_count = 0
longest_name = ""
for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        max_count = count
        longest_name = names[i]
print(f"{longest_name} is the longest. The length of the string is {max_count}.")

# OK
max_count = 0
longest_name = ""
for name, count in zip(names, counts):
    if count > max_count:
        max_count = count
        longest_name = name
print(f"{longest_name} is the longest. The length of the string is {max_count}.")

# 配列の長さが最大のものに合わせる。
names = ["🍖", "🐡", "🥬", "👹"]
calories = [500, 300, 100]

for name, calory in itertools.zip_longest(names, calories):
    print(f"The calorie count for {name} is {calory} calories.")
