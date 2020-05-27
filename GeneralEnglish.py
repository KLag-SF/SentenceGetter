from bs4 import BeautifulSoup as bs
import requests as req
import random

def print_sentence(sentence):
    delimiter = "-*-" * 25
    print("\n" + delimiter)
    for i in sentence:
        print(i)
    print(delimiter + "\n")


def random_util():
    ls = list(range(1, 36))
    sel = random.sample(ls, 15)
    sel.sort()
    print(sel + "\n")


def main_routine(word):
    url = "https://ldoceonline.com/jp/dictionary/" + word
    html = req.get(url)
    page = bs(html.content, "html.parser")

    ls_sentence = page.find_all("span", attrs={"class", "cexa1g1 exa"})
    sentence = []

    for i in ls_sentence:
        content = i.get_text()
        if content[2].isupper() and content[-1] == ".":
            sentence.append(content)

    if len(sentence) == 0:
        print("\nNot Found.\n")
    else:
        print_sentence(sentence)


print("\n" + "-*-" * 5 + "LDOCE Example Sentence Getter Version Beta.4" + "-*-" * 5)
print("Press Ctrl+C to Exit.")
print('Type "/ran" to select 15 numbers from 1 - 35\n')

try:
    while 1:
        word = input("word? > ")

        if word == "/ran":
            random_util()
        else:
            main_routine(word)

except KeyboardInterrupt:
    print("\nProgram was terminated.")