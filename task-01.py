from pytrie import StringTrie as Trie

class Homework(Trie):
    def __init__(self):
        super().__init__()

    def count_words_with_suffix(self, pattern) -> int:
        """
        Підрахунок кількості слів, що закінчуються заданим суфіксом (pattern).
        """
        if not isinstance(pattern, str):
            raise ValueError("Параметр pattern має бути рядком")

        count = 0
        for word in self.keys():
            if word.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix) -> bool:
        """
        Перевірка наявності слів із заданим префіксом (prefix).
        """
        if not isinstance(prefix, str):
            raise ValueError("Параметр prefix має бути рядком")

        for word in self.keys():
            if word.startswith(prefix):
                return True
        return False

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie[word] = i  # Додавання слів у Trie через синтаксис ключ-значення

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    print("Усі тести пройдено успішно!")
