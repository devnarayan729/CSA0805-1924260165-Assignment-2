import sys
from functools import lru_cache


calls = 0


def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_loop(n):
    if n <= 1:
        return 1, 0
    one_step_back = 1
    two_steps_back = 1
    additions = 0
    for _ in range(2, n + 1):
        current = one_step_back + two_steps_back
        two_steps_back = one_step_back
        one_step_back = current
        additions += 1
    return one_step_back, additions


for n in range(1, 7):
    print(f"steps {n}: {ways_loop(n)[0]}")

for n in (10, 20, 25, 30):
    calls = 0
    naive_answer = ways_naive(n)
    naive_calls = calls
    calls = 0
    ways_memo.cache_clear()
    memo_answer = ways_memo(n)
    memo_calls = calls
    loop_answer, loop_additions = ways_loop(n)
    print(
        f"n={n}: naive={naive_answer} calls={naive_calls}; "
        f"memo={memo_answer} calls={memo_calls}; "
        f"loop={loop_answer} additions={loop_additions}"
    )

print("Default recursion limit:", sys.getrecursionlimit())
ways_memo.cache_clear()
calls = 0
try:
    print("Memoised n=1000:", ways_memo(1000))
except RecursionError as error:
    print(f"Memoised n=1000: {type(error).__name__}")

loop_answer, loop_additions = ways_loop(1000)
print("Loop n=1000:", loop_answer)
print("Loop additions:", loop_additions)
