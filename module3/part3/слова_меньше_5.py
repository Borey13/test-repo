import string

my_str = """Было просто пасмурно, дуло с севера
         А к обеду насчитал сто градаций серого. 
         Так всегда первого ноль девятого
         То ли весь мир сошёл с ума, то ли я - того...
         На столе записка от неё смятая
         Недопитый виски допиваю с матами.
         Посмотрю в окно, допишу главу
         Первое сентября, дворник жжёт листву.
         Серым облакам наплевать на нас
         Если знаешь как жить - живи
         Ты хотела плыть как все - так плыви!"""


def len_word_less_five(strings):
    strings = strings.lower()

    for symbol in string.punctuation:
        if symbol in strings:
            strings = strings.replace(symbol, '')

    list_words = list(strings.split())
    only_words_less_five = []

    for word in list_words:
        if len(word) < 5:
            only_words_less_five.append(word)

    return only_words_less_five


print(len_word_less_five(my_str))
