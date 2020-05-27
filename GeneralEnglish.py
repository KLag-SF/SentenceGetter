from bs4 import BeautifulSoup as bs
import requests as req

def print_sentence(sentence):
    delimiter = "-*-" * 25
    print("\n" + delimiter)
    for i in sentence:
        print(i)
    print(delimiter + "\n")


def main_routine(word):
    url = "https://ldoceonline.com/jp/dictionary/" + word
    html = req.get(url)
    page = bs(html.content, "html.parser")

    ls_sentence = page.find_all("span", attrs={"class", "cexa1g1 exa"})
    sentence = []

    for i in ls_sentence:
        sentence.append(i.get_text())

    if len(sentence) == 0:
        print("\nNot Found.\n")
    else:
        print_sentence(sentence)


print("LDOCE Example Sentence Getter    Version-Beta.1")
print("Press Ctrl+C to Exit.\n")

try:
    while 1:
        main_routine(input("Word? > "))
except KeyboardInterrupt:
    print("\nProgram was terminated.")
