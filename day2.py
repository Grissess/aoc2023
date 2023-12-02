import sys

MAXPOP = {
        'red': 12,
        'green': 13,
        'blue': 14,
}

def intoset(s):
    elems = [i.strip() for i in s.split(',')]
    pops = {}
    for elem in elems:
        card, _, col = elem.partition(' ')
        pops[col] = int(card)
    return pops

run = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    game, _, draws = line.partition(': ')
    _, _, gameno = game.partition(' ')
    gameno = int(gameno)

    draws = [intoset(i.strip()) for i in draws.split(';')]
    possible = True
    for pop in draws:
        for col, card in MAXPOP.items():
            if pop.get(col, 0) > card:
                possible = False
                break
    if possible:
        run += gameno

print(run)
