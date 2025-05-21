

class Environment:
    low_point: float
    high_point: float
    density: float

    def is_ok(self, behavior: float) -> bool:
        return self.low_point <= behavior <= self.high_point

    def is_too_low(self, behavior: float) -> bool:
        return behavior < self.low_point

    def is_too_high(self, behavior: float) -> bool:
        return behavior > self.high_point
