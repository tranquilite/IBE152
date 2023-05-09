
def find_last_common(list1: list[int], list2: list[int]) -> dict[int, tuple[int, int]]:
    result = {key: None for key in list1 if key in list2}
    list1, list2 = list1[::-1], list2[::-1]

    for num in result.keys():
        result[num] = (len(list1) - list1.index(num) - 1,
                       len(list2) - list2.index(num) - 1)

    return result


if __name__ == '__main__':
    testcases = [
        [[1, 0, 3, 4, 5, 3], [3, 4, 5]],
        [[1, 0, 3, 4, 5], [30, 40, 50]]
    ]

    for case in testcases:
        print(
            f'>> {find_last_common(case[0], case[1])}'
        )
