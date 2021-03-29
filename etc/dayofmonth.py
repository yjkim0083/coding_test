def test(day: int, k: int):
    answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if day == 0:
        days = [1, 0, 0, 0, 0, 0, 1]
    elif day == 1:
        days = [0, 0, 0, 0, 0, 1, 1]
    elif day == 2:
        days = [0, 0, 0, 0, 1, 1, 0]
    elif day == 3:
        days = [0, 0, 0, 1, 1, 0, 0]
    elif day == 4:
        days = [0, 0, 1, 1, 0, 0, 0]
    elif day == 5:
        days = [0, 1, 1, 0, 0, 0, 0]
    else:
        days = [1, 1, 0, 0, 0, 0, 0]

    # if day == 0:
    #     days = ["일", "월", "화", "수", "목", "금", "토"]
    # elif day == 1:
    #     days = ["월", "화", "수", "목", "금", "토", "일"]
    # elif day == 2:
    #     days = ["화", "수", "목", "금", "토", "일", "월"]
    # elif day == 3:
    #     days = ["수", "목", "금", "토", "일", "월", "화"]
    # elif day == 4:
    #     days = ["목", "금", "토", "일", "월", "화", "수"]
    # elif day == 5:
    #     days = ["금", "토", "일", "월", "화", "수", "목"]
    # else:
    #     days = ["토", "일", "월", "화", "수", "목", "금"]

    months = [31,28,31,30,31,30,31,31,30,31,30,31]

    answer[0] = days[(k % 7)]

    _total_day = 0

    _idx = 1
    for month in months:
        _total_day += month
        answer[_idx] = days[(_total_day + k) % 7]
        _idx += 1
        if _idx == 12:
            break


    return answer





print(test(6, 1))

