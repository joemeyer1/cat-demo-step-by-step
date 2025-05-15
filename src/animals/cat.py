
import random

from src.environments.environment import Environment
from src.utils import ask_chatgpt


class Cat:
    lower_bound_behavior_range: float
    upper_bound_behavior_range: float

    def __init__(self):
        self.lower_bound_behavior_range = 0
        self.upper_bound_behavior_range = 1

    def generate_random_restricted_behavior(self, environment: Environment) -> float:
        return random.uniform(self.lower_bound_behavior_range, self.upper_bound_behavior_range) + environment.density

    def behave(self, environment: Environment) -> float:
        return self.generate_random_restricted_behavior(environment)

    def train(self, environment: Environment, n_epochs: int = 100):
        for i in range(n_epochs):
            behavior = self.behave(environment)
            print(behavior)
            if environment.is_too_low(behavior=behavior):
                self.lower_bound_behavior_range += 0.05
            elif environment.is_too_high(behavior=behavior):
                self.upper_bound_behavior_range -= 0.05

    def test(self, environment: Environment):
        behavior = self.behave(environment)
        print(f"test: {behavior} {environment}")
        print(f"Behavior Range({self.lower_bound_behavior_range + environment.density}, {self.upper_bound_behavior_range + environment.density})")
        print(f"Environment Range({environment.low_point}, {environment.high_point})")
        if ask_chatgpt.is_appropriate(behavior, environment):
            print("Yay, happy cats get rats :)")
        else:
            print("Nooo, find another home kitty :(")
