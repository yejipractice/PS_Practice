END = 123456*2
sieve = [True] * (END+1)


def prime_list(n):
    x = int(n**0.5)
    for i in range(2, x+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                if j < END+1:
                    sieve[j] = False


while(True):
    inp = int(input())
    if inp == 0:
        break
    prime_list(inp*2)
    result = []
    for i in range(inp+1, inp*2+1):
        if i < END+1 and i != 1:
            if sieve[i] == True:
                result.append(i)
    print(len(result))
