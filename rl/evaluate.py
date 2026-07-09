from stable_baselines3 import DQN
from defender_env import DefenderEnv

env = DefenderEnv()

model = DQN.load("rl/dqn_defender")

state, _ = env.reset()

total_reward = 0

done = False

while not done:

    action, _ = model.predict(state)

    state, reward, done, _, _ = env.step(action)

    total_reward += reward

print("Evaluation Complete")
print("Total Reward:", total_reward)