def solution_station_4(num):
    if num == 1:
        return False
    for number in range(2, num):
        if num % number == 0:
            return False
    return True
