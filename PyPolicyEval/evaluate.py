from PyRlEnvs.BaseEnvironment import BaseEnvironment
from PyRlEnvs.FiniteDynamics import FiniteDynamics

import PyPolicyEval.closed_forms as closed_forms

from PyPolicyEval.utils.policies import Policy

# an opinionated default method that tries to find the "best" evaluation algorithm
# given some knowledge of the environment dynamics
def evaluateV(policy: Policy, gamma: float, env: BaseEnvironment):
    if isinstance(env, FiniteDynamics):
        return closed_forms.evaluateV(policy, gamma, env)


def evaluateQ(policy: Policy, gamma: float, env: BaseEnvironment):
    if isinstance(env, FiniteDynamics):
        return closed_forms.evaluateQ(policy, gamma, env)
