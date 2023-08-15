data = [
    ["0001", "Male", "YAmada", "Tarou", "25", "Tokyo"],
    ["0002", "MAle", "Satou", "Takesho", "27", "kanagawa"],
    ["0003", "famale", "kaiki", "arihara", "29", "oosaka"],
    ["0004", "Male", "miyazato", "haibara", "33", "okayama"],
]
print(data)
member_information = {}
for record in data:
    key = record[0]
    info = record[1:]
    member_information[key] = info
print("number", "infomation", sep="\t")
for key, info in member_information.items():
    print(key, info)

