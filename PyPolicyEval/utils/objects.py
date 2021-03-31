from typing import Any, Dict

class ValidatedDict:
    def __init__(self, d: Dict[str, Any]):
        for key in d:
            val = d[key]
            if type(d[key]) is dict:
                val = ValidatedDict(d[key])

            setattr(self, key, val)
