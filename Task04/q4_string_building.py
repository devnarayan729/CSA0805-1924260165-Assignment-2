import time


def build_plus(parts):
    text = ""
    for part in parts:
        text += part + ";"
    return text


def build_join(parts):
    return "".join(part + ";" for part in parts)


def build_f_string(parts):
    return "".join(f"{part};" for part in parts)


sizes = (1_000, 10_000, 200_000)
repeats = 3

for size in sizes:
    items = [f"Item{i}:Rs{i % 50}" for i in range(size)]
    times = {"+=": [], "join": [], "f-string": []}
    results = {}

    for label, builder in (
        ("+=", build_plus),
        ("join", build_join),
        ("f-string", build_f_string),
    ):
        for _ in range(repeats):
            start = time.perf_counter()
            results[label] = builder(items)
            times[label].append(time.perf_counter() - start)

    same_text = results["+="] == results["join"] == results["f-string"]
    print(f"lines: {size}, same text: {same_text}, length: {len(results['join'])}")
    for label in times:
        average = sum(times[label]) / repeats
        raw = ", ".join(f"{value:.6f}" for value in times[label])
        print(f"{label}: runs=[{raw}] average={average:.6f} s")
