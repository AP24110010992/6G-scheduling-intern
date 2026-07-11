import subprocess
import pandas as pd
import numpy as np
import random
import os

RUNS = 10

results = []

for run in range(1, RUNS + 1):

    print("=" * 60)
    print(f"Running Simulation {run}/{RUNS}")
    print("=" * 60)

    seed = random.randint(1, 100000)

    env = os.environ.copy()
    env["SIM_SEED"] = str(seed)

    subprocess.run(
    ["python", "simulation/full_system_demo.py"],
    check=True,
    env=env
)

    df = pd.read_csv("results/scalability_50.csv")

    last = df.iloc[-1]

    results.append({
        "Run": run,
        "Average Risk": last["Average Risk"],
        "Compromised Ratio": last["Compromised Ratio"],
        "Protected Nodes": last["Protected Nodes"]
    })

summary = pd.DataFrame(results)

os.makedirs("results", exist_ok=True)

summary.to_csv(
    "results/statistical_results.csv",
    index=False
)

print("\nCompleted", RUNS, "runs.")

print(summary)

print("\nMean Values")

print(summary.mean(numeric_only=True))

print("\nStandard Deviations")

print(summary.std(numeric_only=True))