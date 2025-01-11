from pytrie import StringTrie as Trie

class LongestCommonWord(Trie):
    def __init__(self):
        super().__init__()

    def find_longest_common_word(self, strings) -> str:
        """
        Знаходить найдовший спільний префікс для всіх слів у масиві strings.
        """
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Вхідні дані мають бути списком рядків")

        if not strings:
            return ""  # Порожній список

        # Знаходимо найдовший спільний префікс
        prefix = strings[0]  # Початково беремо перше слово як префікс
        for word in strings[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # Зменшуємо префікс на 1 символ
                if not prefix:
                    return ""  # Немає спільного префікса
        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()

    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    strings = []
    assert trie.find_longest_common_word(strings) == ""

    strings = ["apple"]
    assert trie.find_longest_common_word(strings) == "apple"

    print("Усі тести пройдено успішно!")
