from stable_baselines3 import DQN
from defender_env import DefenderEnv

# Create environment
env = DefenderEnv()

# Create DQN model
model = DQN(
    policy="MlpPolicy",
    env=env,
    learning_rate=0.001,
    buffer_size=10000,
    learning_starts=100,
    batch_size=32,
    gamma=0.99,
    verbose=1,
)

print("Training started...")

# Train
model.learn(total_timesteps=10000)

# Save model
model.save("rl/dqn_defender")

print("Training Complete!")
print("Model saved as rl/dqn_defender.zip")