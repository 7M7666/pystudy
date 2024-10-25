def count(n, numbers, maxsum=1000000):
    number_set = set(numbers)
    count = 0
    for a in numbers:
        for b in number_set:
            
            if a - b in number_set and a <= maxsum and a != b:
                count += 1
                
    return count

n = int(input())
numbers = list(map(int, input().split()))
result = count(n, numbers)
print( result)
