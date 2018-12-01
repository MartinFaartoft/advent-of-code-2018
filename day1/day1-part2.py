intermediate_values = {0: True}

deltas = [int(line) for line in open('input-day1.txt')]

sum = 0

while(True):
    for delta in deltas:
        sum += delta
        if sum in intermediate_values:
            print(sum)
            exit()
        intermediate_values[sum] = True