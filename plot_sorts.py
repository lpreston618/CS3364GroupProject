import matplotlib.pyplot as plt

nvals = []
ins_times = []
qclassic_times = []
qhybrid_times = []

with open("part1output2.txt", "r") as f:
    next(f)  # skip header
    for line in f:
        line = line.strip()
        if not line:
            continue
        n, insertion, classic, hybrid = line.split(",")
        nvals.append(int(n))
        ins_times.append(float(insertion))
        qclassic_times.append(float(classic))
        qhybrid_times.append(float(hybrid))

colors = [
    "#e6194b",
    "#3cb44b",
    "#4363d8",
    "#f58231",
    "#911eb4",
    "#42d4f4",
    "#f032e6",
    "#bfef45",
    "#fabed4",
    "#469990",
]

print(nvals)
print(ins_times)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(nvals, ins_times, marker="o", color=colors[0], label="Insertion sort")
ax.plot(nvals, qclassic_times, marker="o", color=colors[1], label="Quicksort")
ax.plot(nvals, qhybrid_times, marker="o", color=colors[2], label="Hybrid sort (k=10)")

ax.set_xlabel("Array Size (n)")
ax.set_ylabel("Time (seconds)")
ax.set_title("Comparison of Insertion, Quick, and QuickHybrid Sorts vs. Array Size")
ax.legend(title="Sorting Algorithms")
ax.set_xscale("log")
ax.set_yscale("log")
ax.grid(True, which="both", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("part1_sorts.png", dpi=150)
plt.show()
print("Plot saved to part1_sorts.png")
