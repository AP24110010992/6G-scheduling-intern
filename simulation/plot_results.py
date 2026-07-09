import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("results", exist_ok=True)

# Load simulation results
df = pd.read_csv("results/simulation_results.csv")

# -------------------------------
# Average Risk
# -------------------------------

plt.figure(figsize=(8,5))
plt.plot(df["Round"], df["Average Risk"], linewidth=2)
plt.title("Average Risk Over Time")
plt.xlabel("Round")
plt.ylabel("Average Risk")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/average_risk.png")
plt.close()

# -------------------------------
# Compromised Ratio
# -------------------------------

plt.figure(figsize=(8,5))
plt.plot(df["Round"], df["Compromised Ratio"], linewidth=2)
plt.title("Compromised Ratio Over Time")
plt.xlabel("Round")
plt.ylabel("Compromised Ratio")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/compromised_ratio.png")
plt.close()

# -------------------------------
# Protected Nodes
# -------------------------------

plt.figure(figsize=(8,5))
plt.plot(df["Round"], df["Protected Nodes"], linewidth=2)
plt.title("Protected Nodes Over Time")
plt.xlabel("Round")
plt.ylabel("Protected Nodes")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/protected_nodes.png")
plt.close()

print("Graphs saved in results folder.")