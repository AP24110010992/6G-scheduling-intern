from defender_env import DefenderEnv

env = DefenderEnv()

state, _ = env.reset()

print("Initial State:", state)

for i in range(10):

    action = env.action_space.sample()

    state, reward, done, _, _ = env.step(action)

    print(
        f"Step {i+1:2d}",
        f"Action={action}",
        f"Reward={reward:.2f}",
        f"State={state}"
    )

    if done:
        break