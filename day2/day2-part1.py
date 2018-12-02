from collections import Counter

def checksum(id):
    counter = Counter()
    for char in id:
        counter[char] += 1
    
    exactly_two = 0
    exactly_three = 0

    for key in counter:
        if (counter[key] == 2):
            exactly_two = 1
        if (counter[key] == 3):
            exactly_three = 1

    return [exactly_two, exactly_three]

twos = 0
threes = 0
for line in open('input-day2.txt'):
    c = checksum(line)
    twos += c[0]
    threes += c[1]

print(twos * threes)