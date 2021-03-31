from copy import copy
import numpy as np
from typing import Any
from PyRlEnvs.BaseEnvironment import BaseEnvironment
from PyPolicyEval.utils.objects import ValidatedDict
from PyPolicyEval.utils.policies import Policy

class MonteCarloOptions(ValidatedDict):
    steps: int
    samples: int

def isMaxSteps(step: int, max_steps: int):
    if max_steps == 0:
        return False

    return step >= max_steps

def evaluateState(state: Any, policy: Policy, gamma: float, env: BaseEnvironment, opts: MonteCarloOptions):
    return_samples = np.zeros(opts.samples)

    for sample in range(opts.samples):
        inner_env = copy(env)

        ret = 0.
        step = 0
        t = False
        while not t and not isMaxSteps(step, opts.steps):
            pass

        return_samples[sample] = ret

    return return_samples.mean()



def evaluateV(policy: Policy, gamma: float, env: BaseEnvironment):
    pass
