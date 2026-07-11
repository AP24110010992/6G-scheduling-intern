import matplotlib.pyplot as plt

baseline = {
    "Average Risk": 0.872,
    "Compromised Ratio": 1.000,
    "Protected Nodes": 0
}

proposed = {
    "Average Risk": 0.574,
    "Compromised Ratio": 0.624,
    "Protected Nodes": 7.6
}

metrics = list(baseline.keys())

baseline_values = list(baseline.values())
proposed_values = list(proposed.values())

x = range(len(metrics))
width = 0.35

plt.figure(figsize=(8,5))

plt.bar(
    [i - width/2 for i in x],
    baseline_values,
    width,
    label="Baseline"
)

plt.bar(
    [i + width/2 for i in x],
    proposed_values,
    width,
    label="Proposed"
)

plt.xticks(x, metrics)
plt.ylabel("Value")
plt.title("Baseline vs Proposed IoT Security System")
plt.legend()

plt.tight_layout()
plt.savefig("results/baseline_vs_proposed.png", dpi=300)
plt.show()

print("Saved: results/baseline_vs_proposed.png")