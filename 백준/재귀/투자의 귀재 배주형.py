init, year = map(int, input().split())

cases = [(1, 0.05), (3, 0.2), (5, 0.35)]
max_money = -1


def caculate(money, year):
    global max_money
    if year <= 0:
        max_money = max(money, max_money)
        return
    for case in cases:
        n, r = case
        if year >= n:
            plus = int(money*(1+r))
            caculate(plus, year-n)


caculate(init, year)
print(max_money)
