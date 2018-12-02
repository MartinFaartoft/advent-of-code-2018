def differs_by_one(first, second):
    differences = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            differences += 1
        if differences > 1:
            return False
    return differences == 1

def subtract_differences(first, second):
    similar = ""
    for i in range(len(first)):
        if first[i] == second[i]:
            similar += first[i]
    return similar

for first in open('input-day2.txt'):
    for second in open('input-day2.txt'): #sloppy, should start iteration at line first + 1
        if differs_by_one(first, second):
            print(subtract_differences(first, second))
            exit()
