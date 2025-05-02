
from typing import Tuple


class Environment:
    low_point: float
    high_point: float

    def is_ok(self, behavior) -> bool:
        return self.low_point <= behavior <= self.high_point
