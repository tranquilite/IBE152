def budget_OK(budget: int, participants: int) -> bool:
    entrance_fee = 100 if participants <= 12 else 120 if participants <= 50 else 130
    lane_fee = 200 * (participants // 4 + ( 1 if participants % 4 else 0) )
    # lane_fee = 200 * ((participants + 3) // 4)
    cost = entrance_fee + lane_fee

    return cost <= budget


tests = [
    (0, 1, False),
    (700, 12, True),
    (699, 12, False),
    (2721, 50, True),
    (2719, 50, False)
]

for b1, p1, r1 in tests:
    if budget_OK(b1, p1) == r1:
        print('.', end='')
    else:
        print('F', end='')