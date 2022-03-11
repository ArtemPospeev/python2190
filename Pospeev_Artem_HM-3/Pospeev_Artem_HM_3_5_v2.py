from random import shuffle, choice


def get_jokes(n, no_rep=False):
    """ generates n random jokes """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    rslt_lst = []

    if no_rep:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        rslt_lst = list(zip(nouns, adverbs, adjectives))
        rslt_lst = list(map(' '.join, rslt_lst))
        rslt_lst = rslt_lst[:n]
    else:
        for i in range(n):
            joke_str = ' '.join([choice(nouns), choice(adverbs), choice(adjectives)])
            rslt_lst.append(joke_str)
    return rslt_lst


print(f'5 шуток без повторения элементов:\n{get_jokes(5, True)}\n\n'
      f'3 шутки с повторением элементов:\n{get_jokes(3)}')
