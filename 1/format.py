"""
Cスタイルフォーマット文字列やstr.formatは使わずf文字列で埋め込む。
"""

key = "my_var"
value = 1.234
formatted = f"{key} = {value}"
assert formatted == "my_var = 1.234"

# コロンの後のミニ言語も使える。
assert f"{key!r:<10} = {value:.2f}" == "'my_var'   = 1.23"

# OK
f_string = f"{key:<10} = {value:.2f}"

# NG
c_tuple = "%-10s = %.2f" % (key, value)

# NG
str_args = "{:<10} = {:.2f}".format(key, value)

# NG
str_kw = "{key:<10} = {value:.2f}".format(key=key, value=value)

# NG
c_dict = "%(key)-10s = %(value).2f" % {"key": key, "value": value}

assert f_string == c_tuple == str_args == str_kw == c_dict
