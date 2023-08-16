a = {"fuji": 3776, "kitadake": 3193, "okuhodake": 3190, "dummy": 0}
a_sorted = sorted(a.items(), key=lambda x: x[1], reverse=True)
for key, val in a_sorted:
    print(a_sorted)
