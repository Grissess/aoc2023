import sys, functools, operator

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

games = {}
obscol = set()
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    game, _, draws = line.partition(': ')
    _, _, gameno = game.partition(' ')
    gameno = int(gameno)

    draws = [intoset(i.strip()) for i in draws.split(';')]
    games[gameno] = draws
    for pop in draws:
        obscol |= set(pop.keys())

print(obscol)

run = 0
for gno, draws in games.items():
    obsmin = {col: max(pop.get(col, 0) for pop in draws) for col in obscol}
    power = functools.reduce(operator.mul, obsmin.values(), 1)
    print(gno, power, obsmin)
    run += power

print(run)
