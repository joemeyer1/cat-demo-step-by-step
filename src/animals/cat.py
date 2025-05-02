

from src.environments.environment import Environment


class Cat:

    def behave(self, environment: Environment):
        return self.generate_random_restricted_behavior(environment)

    def train(self, environment: Environment):
        pass

    def test(self, environment: Environment):
        pass
