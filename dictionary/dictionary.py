dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'


def add_word(hun_word, eng_word):
    new = {hun_word:eng_word}
    dictionary.append(new)
    new[hun_word] = eng_word
    print(dictionary)


add_word("kutya","dog")

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


def translate_to_hun(eng_word):
    for item in dictionary:
        for key, value in item.items():
            if value == eng_word:
                print(key)
            
        
translate_to_hun("tree")

def translate_to_eng(hun_word):
    for item in dictionary:
        for key, value in item.items():
            if key == hun_word:
                print(value)


translate_to_eng("fa")