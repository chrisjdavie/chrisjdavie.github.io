from pathlib import Path
from html.parser import HTMLParser

from spellchecker import SpellChecker


CUSTOM_DICTIONARY = [
    "wayhome", "website", "websites", "aggregators", "tutorfair", "carpooling", "prototyped", "singaporean", "cookit", "tdd", "yagni", "speechmatics",
    "sqlalchemy", "matplotlib", "redis", "pytest", "scipy", "numpy", "rabbitmq", "postgresql", "visualisations", "davila", "zarate", "mathworks",
    "google"
]

class WebpageParser(HTMLParser):

    def __init__(self, words):
        super().__init__()

        self._spell = spell
        self._in_checkable = False

    def handle_starttag(self, tag, attrs):
        if tag in ["p", "h1", "h2", "h3"]:
            self._in_checkable = True

    def handle_endtag(self, tag):
        if tag == ["p", "h1", "h2", "h3"]:
            self._in_checkable = False

    def handle_data(self, data):
        if "Commerical" in data:
            print("FOOOOOOOOOOOM", self._in_checkable)
            misspelled = self._spell.unknown(["Commerical"])
            print(misspelled)
        strip_data = data.strip()
        if strip_data:
            raw_words = strip_data.split()
            things_to_remove = [".", "'", ",", "-", "(", ")", "!", "’", "/"]
            # clean_words = set([
            #     sec
            #     for word in raw_words
            #     for thing in things_to_split_on
            #     for sec in word.split(thing)
            #     if len(sec) > 1])

            clean_words = set()
            for word in raw_words:
                new_word = word
                for thing in things_to_remove:
                    new_word = new_word.replace(thing, " ")
                for sec in new_word.split():
                    if len(sec) > 1:
                        clean_words.add(sec)

            misspelled = self._spell.unknown(clean_words)
            for word in misspelled:
                print(word, self._spell.correction(word))

if __name__ == "__main__":
    run_spellcheck()
