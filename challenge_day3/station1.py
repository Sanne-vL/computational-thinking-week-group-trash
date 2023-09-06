def solution_station_1(n):
    
    first = 0
    second = 1
    count = 0

    if n <= 0:
        return first
    elif n == 1:
        return second
    else:
        while count < n - 1:
            nth = first + second
            first =  second
            second = nth
            count += 1

        return second

# n = int(input())
# result = solution_station_1(n)
# print(f'The {n}-th Fibonacci number is {result}')