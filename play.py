"""
play.py

Loads a trained DQN model and watches it play an Atari game.
"""
import time
import gymnasium as gym
import ale_py
from stable_baselines3 import DQN
from stable_baselines3.common.atari_wrappers import AtariWrapper

gym.register_envs(ale_py)   # explicitly register ALE/* environments

# ==========================================================
# Configuration
# ==========================================================

MODEL_PATH = "models/dqn_model.zip"
ENV_NAME = "ALE/Pong-v5"

NUM_EPISODES = 10


# ==========================================================
# Create Environment
# ==========================================================

env = gym.make(
    ENV_NAME,
    render_mode="human"
)

env = AtariWrapper(env)


# ==========================================================
# Load Model
# ==========================================================

print("Loading model...")

model = DQN.load(MODEL_PATH)


model.set_env(env)

print("Model loaded successfully!")

print("\nStarting gameplay...\n")


# ==========================================================
# Play Episodes
# ==========================================================

for episode in range(NUM_EPISODES):

    observation, info = env.reset()

    done = False
    truncated = False

    total_reward = 0

    time.sleep(0.01)

    while not done and not truncated:

        # Greedy policy
        action, _ = model.predict(
            observation,
            deterministic=True
        )

        observation, reward, done, truncated, info = env.step(action)

        total_reward += reward

        env.render()

    print("=" * 50)
    print(f"Episode {episode + 1} Finished")
    print(f"Total Reward : {total_reward}")
    print("=" * 50)

env.close()

print("\nFinished!")