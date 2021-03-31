from typing import List
from PyPolicyEval.utils.objects import ValidatedDict
import unittest

class TestObjects(unittest.TestCase):
    def test_ValidatedDict(self):
        d = {
            'hi': 2,
            'there': 'friend',
        }

        class TestDict(ValidatedDict):
            hi: int
            there: str

        vd = TestDict(d)

        self.assertEqual(vd.hi, 2)
        self.assertEqual(vd.there, 'friend')

        d = {
            'test': {
                'hi': 2,
                'there': 'friend',
            },
            'other': [1, 2, 3],
        }

        class OtherDict(ValidatedDict):
            test: TestDict
            other: List[int]

        vd = OtherDict(d)

        self.assertEqual(vd.test.hi, 2)
        self.assertEqual(vd.test.there, 'friend')
        self.assertEqual(vd.other, [1, 2, 3])
