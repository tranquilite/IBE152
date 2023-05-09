
def find_last_common(list1: list[int], list2: list[int]) -> dict[int, tuple[int, int]]:
    output_dict = {key: None for key in list1 if key in list2}
    list1, list2 = list1[::-1], list2[::-1]

    for num in list1:
        if num in list2:
            output_dict[num] = (len(list1) - list1.index(num) -1,
                                len(list2) - list2.index(num) -1)

    return output_dict


# Ignorer testoppsettet! :)))))
if __name__ == '__main__':
    testcases = [
        [ [int(e) for e in '103453'], [int(e) for e in '345']],
        [ [int(e) for e in '10345'], [30, 40, 50]]
    ]

    for case in testcases:
        print(
            f'>> {find_last_common(case[0], case[1])}'
        )
