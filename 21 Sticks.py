def make_move(sticks):
    if sticks > 4:
        return 3
    elif sticks == 4:
        return 1
    elif sticks == 3:
        return 3
    elif sticks == 2:
        return 2
    elif sticks == 1:
        return 1
