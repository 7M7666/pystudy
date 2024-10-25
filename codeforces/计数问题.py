def count(n, x):
    count = 0
    for i in range(len(str(n))):
        weight = 10 ** i
        currentdigit = (n // weight) % 10
        nexthigherdigit = (n // (weight * 10)) % 10
        if currentdigit > x:
            count += weight
        elif currentdigit == x:
            count += n % weight + 1
        else:
            count += nexthigherdigit * weight

    return count
n=eval(input())
x=eval(input())
count(n, x)
