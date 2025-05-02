

from src.environments.environment import Environment


class Cat:
    restrict_behavior_to_range = (0, 1)

    def generate_random_restricted_behavior(self, environment) -> float:
        pass

    def behave(self, environment: Environment) -> float:
        return self.generate_random_restricted_behavior(environment)

    def train(self, environment: Environment):
        pass

    def test(self, environment: Environment):
        pass
