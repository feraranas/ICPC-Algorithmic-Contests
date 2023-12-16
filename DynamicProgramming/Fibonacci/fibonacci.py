def fibonacci(n):
    """

    :param n: 

    """
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(3)) # 2
# print(fibonacci(4)) # 3
# print(fibonacci(5)) # 5
# print(fibonacci(6)) # 8
# print(fibonacci(7)) # 13
# print(fibonacci(8)) # 21
# print(fibonacci(9)) # 34


def fibonacci_memo(n, memo={}):
    """

    :param n: 
    :param memo:  (Default value = {})

    """
    if memo.get(n):
        return memo[n]
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(3)) # 2
# print(fibonacci(4)) # 3
# print(fibonacci(5)) # 5
# print(fibonacci(6)) # 8
# print(fibonacci(7)) # 13
# print(fibonacci(8)) # 21
# print(fibonacci(9)) # 34
