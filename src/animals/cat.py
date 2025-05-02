
import random
from typing import Tuple

from src.environments.environment import Environment
from src.utils import ask_chatgpt


class Cat:
    restrict_behavior_to_range: Tuple = (0, 1)

    def generate_random_restricted_behavior(self, environment: Environment) -> float:
        return random.uniform(*self.restrict_behavior_to_range)

    def behave(self, environment: Environment) -> float:
        return self.generate_random_restricted_behavior(environment)

    def train(self, environment: Environment):
        pass

    def test(self, environment: Environment):
        behavior = self.behave(environment)
        if ask_chatgpt.is_appropriate(behavior, environment):
            print("Yay, happy cats get rats :)")
        else:
            print("Nooo, find another home kitty :(")
