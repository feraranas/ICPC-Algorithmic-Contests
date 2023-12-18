def fib_with_tabulation(N):
    table = [0] * (N + 1)
    table[1] = 1

    for i in range(len(table)):
        current_value = table[i]
        if i + 1 < len(table):
            table[i + 1] += current_value
        if i + 2 < len(table):
            table[i + 2] += current_value

    return table[N]

result = fib_with_tabulation(6)
print(result)
