import re
import sys

pat = re.compile(r"^\D*(\d).*?(\d)?\D*$")

pairs = [re.match(pat, n).groups() for n in sys.stdin.read().split()]
nums = [int(n1+n2) if n2 is not None else int(n1+n1) for n1, n2 in pairs]
print(sum(nums))
