
import random
from typing import List

from src.environments.environment import Environment
from src.utils import ask_chatgpt


class Cat:
    restrict_behavior_to_range: List[float, float] = [0, 1]

    def generate_random_restricted_behavior(self, environment: Environment) -> float:
        return random.uniform(*self.restrict_behavior_to_range)

    def behave(self, environment: Environment) -> float:
        return self.generate_random_restricted_behavior(environment)

    def train(self, environment: Environment, n_epochs: int = 100):
        for i in range(n_epochs):
            behavior = self.generate_random_restricted_behavior(environment)
            if ask_chagpt.is_behavior_too_low(behavior=behavior, environment=environment):
                self.restrict_behavior_to_range[0] += 0.1
            elif ask_chagpt.is_behavior_too_high(behavior=behavior, environment=environment):
                self.restrict_behavior_to_range[1] -= 0.1

    def test(self, environment: Environment):
        behavior = self.behave(environment)
        if ask_chatgpt.is_appropriate(behavior, environment):
            print("Yay, happy cats get rats :)")
        else:
            print("Nooo, find another home kitty :(")
