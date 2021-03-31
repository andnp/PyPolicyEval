from PyPolicyEval.utils.policies import cachePolicy
import unittest
import numpy as np

np.random.seed(0)

def fakePolicy(s):
    pi = np.random.rand(4)
    return pi / pi.sum()

class TestPolicies(unittest.TestCase):
    def test_cachePolicy(self):
        cached = cachePolicy(fakePolicy)

        pi1 = cached(0)
        pi2 = cached(1)

        pi11 = cached(0)
        pi21 = cached(1)

        # if I call cached policy with same state
        # I get the same result
        self.assertTrue(np.allclose(pi1, pi11))
        self.assertTrue(np.allclose(pi2, pi21))

        # but calling the original policy results in
        # two different policies
        self.assertFalse(np.allclose(pi1, fakePolicy(0)))
