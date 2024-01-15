
def trees_total(apple, peer, plum):
    '''Функція приймає кількість яблукб груш і слив, та виводить загальну кількусть дерев у саду'''
    if apple >= 0 and peer >= 0 and plum >= 0:
        return apple + peer + plum
    else:
        print("Задане значення не може бути негативним")

def space_delete(text):
    """Приймає текст і видаляє у ньому зайві пробіли"""
    if type(text) is str:
        while "  " in text:
            text = text.replace('  ', ' ')
        return text
    else:
        print("Заданий текст не є строкою")

def words_count_in_sentence(text_, sentence_number):
    """Приймає текст та номер речення, після чого виводить кількість слів у заданому реченні"""
    if type(text_) is str:
        sentence_num = sentence_number - 1 #роблю номер речення більш звичним
        text_ = text_.split(".")
        text_ = text_[sentence_num]
        text_ = text_.split()
        return len(text_)
    else:
        print("Заданий текст не є строкою")

text_ = 'sefes. fesd'
print(words_count_in_sentence(text_, 2))




