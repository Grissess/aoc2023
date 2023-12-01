import re, sys

NAMES = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
}
def intoi(x):
    return str(NAMES.get(x, x))

DIG = re.compile('|'.join(['\\d'] + list(NAMES.keys())))

run = 0
for line in sys.stdin:
    #digits = list(m.group() for m in DIG.finditer(line))
    digits = []
    for ix in range(len(line)):
        mo = DIG.match(line[ix:])
        if mo:
            digits.append(mo.group())
    val = int(intoi(digits[0]) + intoi(digits[-1]))
    print(val)
    run += val

print(run)
