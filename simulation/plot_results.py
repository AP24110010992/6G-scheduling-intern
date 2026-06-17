import matplotlib.pyplot as plt

# ---------------------------
# Figure 1: Infection Spread
# ---------------------------

rounds = [0, 1, 2, 3, 4, 5]
infected_devices = [1, 2, 3, 5, 7, 9]   # Replace with your actual values

plt.figure(figsize=(6, 4))

plt.plot(rounds, infected_devices, marker="o")

plt.title("Infection Spread Over Time")
plt.xlabel("Round")
plt.ylabel("Number of Infected Devices")
plt.grid(True)

plt.savefig("results/infection_spread.png")

plt.show()

print("Saved: results/infection_spread.png")


# ---------------------------
# Figure 2: Attack Outcomes
# ---------------------------

detected = 36      # Replace with your actual value
successful = 64   # Replace with your actual value

labels = ["Detected", "Successful"]
values = [detected, successful]

plt.figure(figsize=(6, 4))

plt.bar(labels, values)

plt.title("Attack Outcomes")
plt.ylabel("Number of Attacks")

plt.savefig("results/attack_outcomes.png")

plt.show()

print("Saved: results/attack_outcomes.png")