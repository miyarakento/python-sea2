color_reference = {1: "red", 2: "blue", 3: "yellowF", 4: "green", 5: "popu"}


class MyDictkeyError(Exception):
    def __init__(self, key):
        self.key = key

        def __str__(self):
            return "dobokega{0}".format(self.key)


def get_dict_value(dict_tbl, key):
    if key not in dict_tbl:
        raise MyDictkeyError(key)
    else:
        return dict_tbl[key]


my_dict = {1: "red", 2: "blue", 3: "yellowF"}
try:
    my_color = get_dict_value(my_dict, 5)
except MyDictkeyError as err:
    print(err)
    key = err.args[0]
    my_dict[key] = color_reference[key]
    print(key, color_reference[key], "hikini-to")
    my_color = color_reference[key]
print(my_color)
