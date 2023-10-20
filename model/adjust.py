
with open(r"model\5letters.txt", "r", encoding="utf8") as words:
    dataset = words.read()

dataset = dataset.split(" ")
valid_letters = "aáâãbcdeéêfghijklmnoóôõpqrstuvwxyz"

with open(r"model\words.txt", "w", encoding="utf8") as words:
    text = ""
    for word in dataset:
        word = word[:5].lower()
        if len(word) != 5:
            continue
        if "-" in word:
            continue
        if "." in word:
            continue
        for letter in word:
            if letter not in valid_letters:
                continue
        text += word + "\n"
    words.write(text)