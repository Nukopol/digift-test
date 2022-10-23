from typing import List


def parser(text: str, sublist: List[int], result: List[List[int]]) -> None:
    if len(text) == 0:
        result.append(sublist)
        return None

    if len(text) == 1:
        sublist.append(int(text))
        result.append(sublist)
        return None

    if int(text[:2]) > 27:
        # пара символов НЕ эквивалентна букве
        # первый символ добавляется в субрезультату, остальное кидается обратно в парсер
        new_sublist = sublist + [int(text[0])]
        parser(text[1:], new_sublist, result)
    else:
        # пара символов эквивалентна букве
        # добавить в субрезультат первый элемент пары
        if int(text[0]) != 0 and int(text[1]) != 0:
            new_sublist = sublist + [int(text[0])]
            parser(text[1:], new_sublist, result)

        # добавить в субрезультат пару целиком
        new_sublist = sublist + [int(text[:2])]
        parser(text[2:], new_sublist, result)

    return None


def get_count(text: str) -> int:
    """Counting the number of combinations
    which the source string can be decomposed according to the mapping the alphabet.
    """
    result = []
    parser(text, [], result)
    return len(result)
