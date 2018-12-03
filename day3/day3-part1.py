from collections import Counter
import re

pattern = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')

class Claim:
    def __init__(self, claim_id, x, y, width, height):
        self.claim_id = int(claim_id)
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)

def parse_claim(claim):
    match = re.search(pattern, claim)
    return Claim(match.group(1), match.group(2), match.group(3), match.group(4), match.group(5))
    

fabric = Counter()

def claim_fabric(claim, fabric):
    for x in range(claim.x, claim.x + claim.width):
        for y in range(claim.y, claim.y + claim.height):
            fabric[x,y] += 1

for line in open('input-day3.txt'):
    claim = parse_claim(line)
    claim_fabric(claim, fabric)

print(sum([1 for val in fabric.values() if val > 1 ]))