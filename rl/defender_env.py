import os
import sys
import numpy as np
import gymnasium as gym
from gymnasium import spaces

# Access simulation folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from simulation.iot_network import create_iot_network
from simulation.attack_engine import (
    attack_random,
    attack_targeted,
    attack_burst
)
from simulation.defender_engine import (
    select_monitor_nodes,
    defend_network,
    network_stats
)


class DefenderEnv(gym.Env):

    def __init__(self):

        super().__init__()

        # State:
        # [average risk,
        # compromised ratio,
        # protected nodes,
        # current round]

        self.observation_space = spaces.Box(
            low=0,
            high=1,
            shape=(4,),
            dtype=np.float32
        )

        # Five possible defender strategies
        self.action_space = spaces.Discrete(5)

        self.max_rounds = 100

        self.round = 0

        self.network = create_iot_network()

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.round = 0

        self.network = create_iot_network()

        state = np.array(
            [0.5, 0.0, 0.0, 0.0],
            dtype=np.float32
        )

        return state, {}

    def step(self, action):

        self.round += 1

        # -----------------------------
        # Defender strategy
        # -----------------------------

        if action == 0:

            monitored = select_monitor_nodes(
                self.network,
                top_k=5
            )

        elif action == 1:

            monitored = sorted(
                self.network.nodes(),
                key=lambda n:
                self.network.nodes[n]["vulnerability"],
                reverse=True
            )[:5]

        elif action == 2:

            monitored = sorted(
                self.network.nodes(),
                key=lambda n:
                self.network.nodes[n]["risk_score"],
                reverse=True
            )[:5]

        elif action == 3:

            monitored = list(
                np.random.choice(
                    list(self.network.nodes()),
                    5,
                    replace=False
                )
            )

        else:

            risk_nodes = sorted(
                self.network.nodes(),
                key=lambda n:
                self.network.nodes[n]["risk_score"],
                reverse=True
            )[:3]

            vuln_nodes = sorted(
                self.network.nodes(),
                key=lambda n:
                self.network.nodes[n]["vulnerability"],
                reverse=True
            )[:2]

            monitored = list(
                dict.fromkeys(
                    risk_nodes + vuln_nodes
                )
            )

        # -----------------------------
        # Attack
        # -----------------------------

        if self.round % 15 == 0:

            attack_burst(
                self.network,
                self.round
            )

        elif self.round % 5 == 0:

            attack_targeted(
                self.network,
                self.round
            )

        else:

            attack_random(
                self.network,
                self.round
            )

        # -----------------------------
        # Defender reacts
        # -----------------------------

        defend_network(
            self.network,
            monitored
        )

        stats = network_stats(
            self.network
        )

        state = np.array([
            stats["avg_risk"],
            stats["compromised_ratio"],
            stats["protected_nodes"] / 50,
            self.round / self.max_rounds
        ], dtype=np.float32)

        reward = (
            5 * stats["protected_nodes"]
            - 10 * stats["compromised_ratio"]
            - stats["avg_risk"]
        )

        terminated = (
            self.round >= self.max_rounds
        )

        truncated = False

        return (
            state,
            reward,
            terminated,
            truncated,
            {}
        )