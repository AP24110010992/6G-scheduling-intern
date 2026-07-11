import pandas as pd
from scipy.stats import wilcoxon

# Load results
baseline = pd.read_csv("results/baseline_statistics.csv")
proposed = pd.read_csv("results/statistical_results.csv")

# Compare Compromised Ratio
statistic, p_value = wilcoxon(
    baseline["Compromised Ratio"],
    proposed["Compromised Ratio"]
)

print("=" * 60)
print("Wilcoxon Signed-Rank Test")
print("=" * 60)

print(f"Statistic : {statistic:.4f}")
print(f"P-value   : {p_value:.6f}")

if p_value < 0.05:
    print("\nResult: Significant Improvement (p < 0.05)")
else:
    print("\nResult: Not Significant (p >= 0.05)")