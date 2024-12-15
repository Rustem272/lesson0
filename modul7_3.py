'''Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.

Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.
'''

class WordsFinder:

    SYMBOLS_TO_REPLACE = [',', '.', '=', '!', '?', ';', ':', ' - ']
    def __init__(self, *file_names):
        self.file_names = file_names

    def replacement(self, line):
        new_line = line.replace(WordsFinder.SYMBOLS_TO_REPLACE[0], '')
        # print('old >>', id(line))
        # print('new >>', id(new_line))
        for s in WordsFinder.SYMBOLS_TO_REPLACE[1:]:
            new_line = new_line.replace(s, '')
        return new_line

    def get_all_words(self):
        all_words = {}

        for fname in self.file_names:
            with open(fname, 'r', encoding='utf-8') as file:
                all_words[fname] = []
                for line in file:
                    line = line.lower()
                    line = self.replacement(line)
                    for word in line.split():
                        all_words[fname].append(word)
        return all_words

    def find(self, word):
        '''Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.'''
        dict_ = {}
        for fname, words in self.get_all_words().items():
            for pos, w in enumerate(words):
                if word.lower() == w.lower():
                    dict_[fname] = pos + 1
                    break
        return dict_

    def count(self, word):
        '''Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.'''
        dict_ = {}
        for fname, words in self.get_all_words().items():
            counter = 0
            for w in words:
                if word.lower() == w.lower():
                    counter += 1
            dict_[fname] = counter
        return dict_

def main():
    '''Пример выполнения программы:'''
    finder2 = WordsFinder('test_file.txt', 'test_file_b.txt')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего
    '''
    Вывод на консоль:
    {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
    {'test_file.txt': 3}
    {'test_file.txt': 4}
    '''

if __name__ == '__main__':
    main()

'''
Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

for name, words in get_all_words().items():
  # Логика методов find или count'''