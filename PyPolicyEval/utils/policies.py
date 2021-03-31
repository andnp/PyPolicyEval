import numpy as np
from typing import Any, Callable

Policy = Callable[[Any], np.ndarray]

def cachePolicy(policy: Policy) -> Policy:
    cache = {}

    def inner(state: Any):
        if state in cache:
            return cache[state]

        pi = policy(state)
        cache[state] = pi

        return pi

    return inner
