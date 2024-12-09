
def single_root_words(root_word, *other_words):
    same_word = []
    r_w = root_word.lower()
    for word in other_words:
        w_l = word.lower()
        if r_w in w_l:
            same_word.append(word)
    return same_word

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)



