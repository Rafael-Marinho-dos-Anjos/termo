
from random import choice


def new_word() -> str:
    with open(r"model\5letters.txt", "r", encoding="utf8") as words:
        return choice(words.readlines())[:5]


def fix_letters(word) -> str:
    word = list(word)
    for i in range(5):
        if word[i] in "áãâ":
            word[i] = "a"
        elif word[i] in "éê":
            word[i] = "e"
        elif word[i] in "í":
            word[i] = "i"
        elif word[i] in "óôõ":
            word[i] = "o"
        elif word[i] in "ú":
            word[i] = "u"
        elif word[i] in "ç":
            word[i] = "c"
    return "".join(word)


def verify_word(wrd) -> bool:
    with open(r"model\5letters.txt", "r", encoding="utf8") as words:
        for word in words.readlines():
            if wrd == fix_letters(word[:5]):
                return True
        
    return False
