from collections import Counter
import re

pattern = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')

non_overlapping_claims = set() # set of id's of claims that have not yet been found to overlap any other claims
fabric = {} # stores key-value pairs: (x,y): claim_id, where (x,y) is the coordinates of the piece of fabric claimed by claim with id

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

def claim_fabric(claim, fabric):
    for x in range(claim.x, claim.x + claim.width):
        for y in range(claim.y, claim.y + claim.height):
            if (x,y) in fabric: #if square of fabric was claimed by another claim, disqualify overlapping claims
                non_overlapping_claims.discard(claim.claim_id)
                non_overlapping_claims.discard(fabric.get((x,y)))
            else:
                fabric[(x,y)] = claim.claim_id #square not yet claimed, tag with id of current claim

for line in open('input-day3.txt'):
    claim = parse_claim(line)
    non_overlapping_claims.add(claim.claim_id)
    claim_fabric(claim, fabric)

print(non_overlapping_claims.pop())