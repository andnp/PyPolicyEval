import numpy as np
from PyPolicyEval.utils.policies import Policy
from PyRlEnvs.FiniteDynamics import FiniteDynamics

def evaluateV(policy: Policy, gamma: float, env: FiniteDynamics):
    # get substochastic matrix P_{\pi, \gamma}
    P = env.constructTransitionMatrix(policy, gamma)
    R = env.constructRewardVector(policy)
    I = np.eye(env.num_states)

    v = np.linalg.pinv(I - P).dot(R)
    return v


def evaluateQ(policy: Policy, gamma: float, env: FiniteDynamics):
    P = env.constructTransitionMatrix(policy, gamma)
    R = env.constructRewardVector(policy)
    I = np.eye(env.num_states)

    Rs = env.Rs
    K = env.K
    v = np.linalg.pinv(I - P).dot(R)

    q = np.zeros((env.num_states, env.num_actions))
    for s in range(env.num_states):
        for a in range(env.num_actions):
            for sp in range(env.num_states):
                q[s, a] += K[s, a, sp] * (Rs[s, a, sp] + gamma * v[sp])

    return q
