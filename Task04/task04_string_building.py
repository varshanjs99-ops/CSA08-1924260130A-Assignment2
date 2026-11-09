# Q4 – Building Long Text: += or join?
import time
import statistics

def build_plus(parts):
    text = ""
    for part in parts:
        text += part + "\\n"
    return text

def build_join(parts):
    return "\\n".join(parts) + "\\n"

def build_fstring(parts):
    return "".join(f"{part}\\n" for part in parts)

def benchmark(parts, repeats=3):
    results = {"+=": [], "join": [], "f-string": []}
    builders = [("+= ", build_plus), ("join", build_join),
                ("f-string", build_fstring)]
    for _ in range(repeats):
        for name, fn in builders:
            start = time.perf_counter()
            output = fn(parts)
            elapsed = time.perf_counter() - start
            results[name.strip()].append(elapsed)
            assert len(output) == len(build_join(parts))
    return {name: statistics.mean(times) for name, times in results.items()}

if __name__ == "__main__":
    print("Q4 benchmark (seconds; machine-dependent; average of 3 runs)")
    for size in (1_000, 10_000, 200_000):
        items = [f"Item{i}:Rs{i % 50}" for i in range(size)]
        measured = benchmark(items)
        print(f"n={size:6}: " + " | ".join(f"{k}={v:.6f}" for k, v in measured.items()))
        print("Output characters:", len(build_join(items)))
