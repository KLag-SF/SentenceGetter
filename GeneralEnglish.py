from bs4 import BeautifulSoup as bs
import requests as req
import random
from googletrans import Translator

def print_sentence(sentence, japanese):
    delimiter = "-*-" * 25
    print("\n" + delimiter)
    for i in range(len(sentence)):
        print(f"・{sentence[i]}\n({japanese[i]})\n")
    print(delimiter + "\n")


def random_util():
    ls = list(range(1, 36))
    sel = random.sample(ls, 15)
    sel.sort()
    print(str(sel) + "\n")


def translate(sentence):
    trans = Translator()
    res = []
    for i in sentence:
        ja = trans.translate(i, dest="ja")
        res.append(ja.text)
    return res
        

def terminate():
    print("\nProgram was Terminated\n")


def main_routine(word):
    url = "https://ldoceonline.com/jp/dictionary/" + word
    html = req.get(url)
    page = bs(html.content, "html.parser")

    ls_sentence = page.find_all("span", attrs={"class", "cexa1g1 exa"})
    sentence = []

    for i in ls_sentence:
        content = i.get_text()
        if content[2].isupper() and content[-1] == ".":
            sentence.append(content[2::])

    japanese = translate(sentence)

    if len(sentence) == 0:
        print("\nNot Found.\n")
    else:
        print_sentence(sentence, japanese)


print("\n" + "-*-" * 5 + "LDOCE Example Sentence Getter Version 0.9" + "-*-" * 5)
print("・Press Ctrl+C to Exit.")
print('・Type "/ran" to select 15 numbers from 1 - 35\n')

try:
    while 1:
        word = input("word? > ")
        if word == "/ran":
            random_util()
        else:
            main_routine(word)

except (KeyboardInterrupt, EOFError):
    terminate()