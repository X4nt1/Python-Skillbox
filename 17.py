#1
from typing import List
from functools import reduce

if __name__ == '__main__':
    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
    new_floats: List[float] = list(map(lambda x: round(x ** 3, 3), floats))
    new_names: List[str] = list(filter(lambda x: len(x) > 4, names))
    new_numbers: List[int] = reduce(lambda x, y: x * y, numbers)

#2
from typing import List
if __name__ == '__main__':
    letters: List[str] = ['a', 'b', 'c', 'd', 'e']
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    results = list(map(lambda x, y: (x, y), letters, numbers))
    print(results)

#3
def can_be_poly(s: str) -> bool:
    char_counts = Counter(s)
    odd_count = sum(count % 2 == 1 for count in char_counts.values())
    return odd_count <= 1

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

#4
def count_unique_characters(text: str) -> int:
    res = list(filter(lambda sym: 0 < text.lower().count(sym.lower) < 2, text))
    return len(res)


if __name__ == '__main__':
    message = "Today is a beautiful day! The sun is shining and the birds are singing."
    unique_count = count_unique_characters(message)
    print("Количество уникальных символов в строке:", unique_count)
