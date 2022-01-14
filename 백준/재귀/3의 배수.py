num = int(input())
count = 0


def check(num):
    global count
    if num < 10:
        print(count)
        print("YES" if num % 3 == 0 else "NO")
        return
    else:
        count += 1
        check(sum(list(map(int, str(num)))))


check(num)
