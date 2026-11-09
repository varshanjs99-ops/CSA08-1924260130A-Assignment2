# Q6 – Recursion and Its Limits
from functools import lru_cache
import sys
import time

naive_calls = 0
def ways_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

memo_calls = 0
@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def ways_iterative(n):
    if n <= 1:
        return 1
    previous, current = 1, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current

if __name__ == "__main__":
    print("Hand-check values:")
    for n in range(1, 7):
        print(n, ways_iterative(n))
    naive_calls = 0
    print("naive n=25:", ways_naive(25), "calls:", naive_calls)
    memo_calls = 0
    ways_memo.cache_clear()
    print("memo n=25:", ways_memo(25), "calls:", memo_calls)
    print("n=1000 iterative:", ways_iterative(1000))
    try:
        ways_memo.cache_clear()
        memo_calls = 0
        print("n=1000 memo:", ways_memo(1000))
    except RecursionError:
        print("n=1000 memo: RecursionError near Python recursion limit",
              sys.getrecursionlimit())
