# Q7 – Diagnose, Redesign and Validate
# Selected program: Q6 stair-counting recursion.
# Redesign: bottom-up iteration retaining only the previous two results.

def original_memoised(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = original_memoised(n - 1, cache) + original_memoised(n - 2, cache)
    return cache[n]

def redesigned_constant_space(n):
    if n <= 1:
        return 1
    one_step_before = 1
    two_steps_before = 1
    for _ in range(2, n + 1):
        current = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current
    return one_step_before

if __name__ == "__main__":
    print("n | memoised recursion | iterative redesign | match")
    for n in (1, 2, 5, 10, 25, 100, 1000):
        try:
            old = original_memoised(n)
            old_text = str(old)
            matches = old == redesigned_constant_space(n)
        except RecursionError:
            old_text = "RecursionError"
            matches = "N/A (recursive limit)"
        new = redesigned_constant_space(n)
        print(f"{n:4} | {old_text} | {new} | {matches}")
