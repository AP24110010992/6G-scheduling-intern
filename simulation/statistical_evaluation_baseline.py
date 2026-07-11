import subprocess
import pandas as pd
import numpy as np
import os
import random

RUNS = 10

results = []

for run in range(1, RUNS + 1):

    print("=" * 60)
    print(f"Running Baseline {run}/{RUNS}")
    print("=" * 60)

    seed = random.randint(1, 100000)

    env = os.environ.copy()
    env["SIM_SEED"] = str(seed)

    subprocess.run(
        ["python", "simulation/baseline_demo.py"],
        check=True,
        env=env
    )

    df = pd.read_csv("results/baseline_results.csv")

    last = df.iloc[-1]

    results.append({
        "Run": run,
        "Average Risk": last["Average Risk"],
        "Compromised Ratio": last["Compromised Ratio"],
        "Protected Nodes": last["Protected Nodes"]
    })

summary = pd.DataFrame(results)

summary.to_csv(
    "results/baseline_statistics.csv",
    index=False
)

print("\nBaseline Results")

print(summary)

print("\nMean")

print(summary.mean(numeric_only=True))

print("\nStandard Deviation")

print(summary.std(numeric_only=True))