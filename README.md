# Deep Q-Network (DQN) Atari Agent using Stable Baselines3 and Gymnasium

## Project Overview

This project implements a Deep Q-Network (DQN) reinforcement learning agent using **Stable Baselines3** and **Gymnasium Atari environments**.

The objective was to train an agent to play an Atari game, evaluate its performance, and analyze how different hyperparameter configurations affect learning performance.

The project includes:

- Training DQN agents using CNN and MLP policies
- Hyperparameter tuning experiments
- Evaluation of trained agents
- Real-time gameplay visualization using `play.py`
- Documentation of individual contributions and experiment results

---

# Environment Used

## Atari Environment

The selected Atari environment for this project was:
```
ALE/Pong-v5
```

The environment was chosen because it provides a challenging visual reinforcement learning task where the agent must learn decision-making strategies directly from image observations.

The agent receives game frames as input and learns optimal actions through interaction with the environment.

---

# Technologies Used

The project was developed using:

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Gymnasium | Atari simulation environment |
| Stable Baselines3 | Reinforcement learning framework |
| PyTorch | Deep learning backend |
| CUDA GPU | Accelerated training |
| TensorBoard | Training monitoring |

---

# Repository Structure

The repository is organized according to individual group contributions.

```
DQN-Atari-Project
│
├── README.md
│
├── play.py
├── requirements.py
├── models/
│ └── best_model.zip
│
├── Mike/
│ ├── train.py
│ └── hyperparameter_documentation.pdf
│
├── Melissa/
│ ├── train.py
│ ├── models
│ └── hyperparameter_Experiments_Melissa.pdf
│
└── Emmanuella/
├── train.py
└── hyperparameter_documentation.pdf
```

---

# Group Contributions

Each group member independently performed:

- 10 DQN training experiments
- Hyperparameter tuning
- Performance analysis
- Documentation of observations

The experiments focused on understanding how different configurations affect:

- Learning stability
- Reward improvement
- Exploration-exploitation balance
- Policy performance

The individual experiment reports are available below:

---

## Member Experiment Documentation

### Mike

Hyperparameter tuning experiments:

[View Mike's Experiment Documentation](./mike experiments/Hyperparameter Tuning Experiments - Ntwari Mike Chris Kevin.pdf)


---

### Mellisa

Hyperparameter tuning experiments:

[View Melissa's Experiment Documentation](./models-bella-mellisa-ineza/hyperparameter_experiments_Melissa.pdf)


---

### Emmanuella

Hyperparameter tuning experiments:

[View Emmanuella's Experiment Documentation](./Kevin/hyperparameter_documentation.pdf)


---

# Deep Q-Network (DQN) Implementation

The agent was implemented using Stable Baselines3 DQN.

The training process involved:

1. Creating the Atari environment
2. Defining the DQN architecture
3. Training through environment interaction
4. Saving the trained policy
5. Evaluating performance

---

# Policy Architecture Comparison

Two policy architectures were tested:

## CNN Policy

The CNN policy was designed for image-based observations.

Advantages:

- Extracts spatial features from game frames
- Better suited for Atari environments
- Learns visual patterns automatically


## MLP Policy

The MLP policy was also tested for comparison.

However, since Atari observations are image-based, MLP policies performed worse because they do not efficiently capture spatial information.

---

# Hyperparameter Tuning

The following hyperparameters were investigated:

| Parameter | Description |
|-----------|-------------|
| Learning Rate | Controls the size of neural network updates |
| Gamma | Discount factor for future rewards |
| Batch Size | Number of experiences used per update |
| Epsilon Start | Initial exploration rate |
| Epsilon End | Final exploration rate |
| Epsilon Decay | Rate at which exploration decreases |


Each group member tested 10 different hyperparameter combinations.

The complete results and observations are available in the individual documentation files.

---

# Best Performing Configuration

After comparing the experimental results, the best performing model achieved:

Policy:
CnnPolicy

Learning Rate:
0.0005

Gamma:
0.99

Batch Size:
64

Epsilon Start:
1.0

Epsilon End:
0.05

Epsilon Decay:
0.1


The model achieved the highest evaluation reward among the tested configurations.

---

# Key Hyperparameter Findings

## Learning Rate

Lower learning rates produced more stable training.

Very high learning rates caused unstable updates and reduced performance.

---

## Batch Size

Increasing the batch size improved performance.

A batch size of 64 produced better results than 32 because it provided more stable gradient updates.

---

## Gamma

Increasing gamma allowed the agent to consider future rewards more strongly.

However, extremely high gamma values combined with unstable learning rates reduced performance.

---

## Exploration

Higher exploration values helped the agent discover better strategies.

However, excessive exploration delayed convergence.

---

# Model Evaluation

The trained model was evaluated using:

play.py


The script:

1. Loads the trained `.zip` DQN model
2. Creates the same Atari environment
3. Uses deterministic action selection (Greedy Q-policy)
4. Runs multiple gameplay episodes
5. Displays the agent playing in real time

---

# Gameplay Demonstration

The trained agent interacting with the Atari environment can be viewed below:

## Gameplay Video

[Watch Agent Gameplay Demonstration](./[video/gameplay_demo.mp](https://drive.google.com/file/d/1L_tWxhXTX5NpN4Q4HfHzeLmH_3p2apww/view?usp=sharing))


The video demonstrates:

- Model loading
- Environment rendering
- Agent decision-making
- Real-time gameplay performance

---

# Running the Project

## 1. Install Dependencies

Create a Python environment:

```bash
python -m venv rl_env

Activate environment:

Windows:

rl_env\Scripts\activate

Linux/Mac:

source rl_env/bin/activate

Install requirements:

pip install -r requirements.txt
Training the Agent
```
Run:

python train.py

The training process will:

Train the DQN agent
Save the model
Record evaluation metrics

The trained model is saved as:

dqn_model.zip
Running the Agent

To watch the trained agent:

python play.py

The game window will open and display the agent playing the Atari environment.

Conclusion

This project successfully implemented and evaluated a DQN agent for an Atari environment.

Through systematic hyperparameter tuning, policy comparison, and evaluation, the project demonstrated how reinforcement learning agents improve through optimization of learning parameters and neural network architectures.
