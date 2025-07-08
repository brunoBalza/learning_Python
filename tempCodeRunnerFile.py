def sumatoria(n):
    if n == 0:
        return 0

    else:
        return n + sumatoria(n-1)

print(sumatoria(10))