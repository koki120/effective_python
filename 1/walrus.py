"""
代入式で繰り返しを防ぐ
"""

fresh_fruit = {"apple": 10, "banana": 8, "lemon": 5}

# NG

count1 = fresh_fruit.get("apple")
if count1 >= 4:
    print(f"apple is {count1}.make 🍹")
else:
    print("out of stack")

# OK
if (count := fresh_fruit.get("apple")) > 4:
    print(f"apple is {count}. make 🍹")
else:
    print(f"apple is {count}. out of stack")

# switch文がpythonにないので、:=を使って代用する。

# NG

count2 = fresh_fruit.get("banana")
if count2 >= 2:
    print(count2)
else:
    count = fresh_fruit("apple")
    if count >= 4:
        print(count)
    else:
        count = fresh_fruit("lemon")
        if count:
            print(count)
        else:
            print("Nothing")


# OK
if (count := fresh_fruit.get("banana")) >= 2:
    print(count)
elif (count := fresh_fruit("apple")) >= 4:
    print(count)
elif count := fresh_fruit("lemon"):
    print(count)
else:
    print("Nothing")
