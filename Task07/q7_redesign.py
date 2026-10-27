import time


naive_calls = 0


def ways_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


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


for n in (10, 20, 25, 30):
    naive_calls = 0
    start = time.perf_counter()
    original_answer = ways_naive(n)
    original_time = time.perf_counter() - start
    start = time.perf_counter()
    redesigned_answer, additions = ways_loop(n)
    redesigned_time = time.perf_counter() - start
    print(
        f"n={n}: same answer={original_answer == redesigned_answer}, "
        f"answer={original_answer}, naive calls={naive_calls}, "
        f"loop additions={additions}, naive time={original_time:.6f} s, "
        f"loop time={redesigned_time:.6f} s"
    )

large_answer, large_additions = ways_loop(1000)
print(f"n=1000: loop answer={large_answer}, additions={large_additions}")
