# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

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
    else:
        for i in range(n):
            joke_lst = list(zip([choice(nouns)], [choice(adverbs)], [choice(adjectives)]))
            rslt_lst += list(map(' '.join, joke_lst))
    return rslt_lst[:n]


print(f'5 шуток без повторения элементов:\n{get_jokes(5,True)}\n\n'
      f'3 шутки с повторением элементов:\n{get_jokes(3)}')
