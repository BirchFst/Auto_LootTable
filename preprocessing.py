import os

for file in os.listdir("source"):
    text = open(f"source\\{file}", encoding="utf-8")

    data = [x.split("\t")[1] for x in text.readlines()]

    f = open(f"objects\\{file}.alt", 'w', encoding='utf-8')
    f.write("".join(data))
