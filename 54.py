with open("inputs/54_input.txt") as inputFile:
	data = inputFile.read()
hands = data.split("\n")

from enum import Enum
class Rank(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR = 7
    POKER = 8

def organizeHand(cards):
    h = cards[:]
    v = [i[0] for i in h]
    for i in range(5):
        if v[i] == 'T':
            v[i] = 10
        elif v[i] == 'J':
            v[i] = 11
        elif v[i] == 'Q':
            v[i] = 12
        elif v[i] == 'K':
            v[i] = 13
        elif v[i] == 'A':
            v[i] = 14
        else:
            v[i] = int(v[i])
    v.sort()
    s = [i[1] for i in h]

    flush = s[0] == s[1] == s[2] == s[3] == s[4]
    straight = v[4]-4 == v[3]-3 == v[2]-2 == v[1]-1 == v[0]

    count = {}
    for i in v:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    pairs = []
    three = None
    four = None
    for key,val in count.items():
        if val == 4:
            four = key
        elif val == 3:
            three = key
        elif val == 2:
            pairs.append(key)
    pairs.sort()

    rank = Rank.HIGH_CARD
    if straight and flush:
        rank = Rank.POKER
    elif four:
        rank = Rank.FOUR
    elif three and len(pairs) == 1:
        rank = Rank.FULL_HOUSE
    elif flush:
        rank = Rank.FLUSH
    elif straight:
        rank = Rank.STRAIGHT
    elif three:
        rank = Rank.THREE
    elif len(pairs) == 2:
        rank = Rank.TWO_PAIRS
    elif len(pairs) == 1:
        rank = Rank.ONE_PAIR
            
    return {
        "c": " ".join(h),
        "v": v,
        "s": s,
        "straight": straight,
        "flush": flush,
        "four": four,
        "three": three,
        "pairs": pairs,
        "rank": rank
        }


def compareHighestCard(hand1, hand2):
    # suits are irrelevant as specified in task
    # therefore assuming hand1 wins for value draws
    v1 = hand1["v"]
    v2 = hand2["v"]
    for i in range(-1,-6,-1):
        diff = v1[i] - v2[i]
        if diff > 0:
            return True
        elif diff < 0:
            return False

points = 0
for h in hands:
    cards = h.split(" ")
    hand1 = organizeHand(cards[:5])
    hand2 = organizeHand(cards[5:])
    
    rank1 = hand1["rank"]
    rank2 = hand2["rank"]
    if rank1.value > rank2.value:
        points += 1
    elif rank1 == rank2:
        if rank1 in [Rank.POKER, Rank.FLUSH, Rank.STRAIGHT, Rank.HIGH_CARD]:
            if compareHighestCard(hand1, hand2):
                points +=1
        elif rank1 == Rank.FOUR:
            if hand1["four"] > hand2["four"]:
                points += 1
        elif rank1 in [Rank.FULL_HOUSE, Rank.THREE]:
            if hand1["three"] > hand2["three"]:
                points += 1    
        elif rank1 == Rank.TWO_PAIRS:
            diff1 = hand1["pairs"][1] - hand2["pairs"][1]
            diff2 = hand1["pairs"][0] - hand2["pairs"][0]
            if diff1 > 0:
                points += 1
            elif diff1 == 0 and diff2 > 0:
                points += 1
            elif diff1 == 0 and diff2 == 0 and compareHighestCard(hand1, hand2):
                points += 1
        elif rank1 == Rank.ONE_PAIR:
            diff = hand1["pairs"][0] - hand2["pairs"][0]
            if diff > 0:
                points += 1
            elif diff == 0 and compareHighestCard(hand1, hand2):
                points += 1

print(points)
