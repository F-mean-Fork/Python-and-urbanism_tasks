def get_unique_words(sentence):
    sentence = sentence.split()
    new_list = set(sentence)
    new_list = sorted(new_list)
    return new_list


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
