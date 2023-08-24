a = "out_txtf"
s = "hellow out_txtr"
with open(a, "w") as f:
    f.write(s)
with open(a, "r") as f:
    for line in f:
        print(line, end="")
