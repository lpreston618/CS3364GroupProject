import matplotlib.pyplot as plt
from collections import defaultdict

data = defaultdict(list)  # n -> list of (k, time)

with open("part1data.txt", "r") as f:
    next(f)  # skip header
    for line in f:
        line = line.strip()
        if not line:
            continue
        n, k, t = line.split(",")
        data[int(n)].append((int(k), float(t)))

colors = [
    "#e6194b", "#3cb44b", "#4363d8", "#f58231",
    "#911eb4", "#42d4f4", "#f032e6", "#bfef45",
    "#fabed4", "#469990",
]

fig, ax = plt.subplots(figsize=(10, 6))

for i, n in enumerate(sorted(data.keys())):
    pairs = sorted(data[n], key=lambda x: x[0])
    ks = [p[0] for p in pairs]
    times = [p[1] for p in pairs]
    ax.plot(ks, times, marker="o", color=colors[i % len(colors)], label=f"n={n}")

ax.set_xlabel("Threshold k")
ax.set_ylabel("Average Time (seconds)")
ax.set_title("Hybrid Quicksort Runtime: Time vs. Threshold k (by array size n)")
ax.legend(title="Array size")
ax.set_xscale("log")
ax.set_yscale("log")
ax.grid(True, which="both", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("part1_plot.png", dpi=150)
plt.show()
print("Plot saved to part1_plot.png")
