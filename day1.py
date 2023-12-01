import re, sys

DIG = re.compile(r'\d')

run = 0
for line in sys.stdin:
    digits = list(m.group() for m in DIG.finditer(line))
    val = int(digits[0] + digits[-1])
    print(val)
    run += val

print(run)
