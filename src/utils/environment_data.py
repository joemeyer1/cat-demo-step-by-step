

from typing import Tuple

from src.environments.environment import Environment


class EnvironmentData:

    def __init__(self, environment: Environment, train_test_proportion: float):
        """Dataset wrapper for environment.

        Args:
            environment: Data to wrap.
            train_test_proportion: a float between 0 and 1, the proportion of data to use for training (as opposed to testing).
        """
        assert 0 < train_test_proportion <= 1, "You don't have to set aside any data for testing, but you have to use some for training."

        self.train_environment, self.test_environment = self.split_data(environment=environment, train_test_proportion=train_test_proportion)

    def split_data(self, environment: Environment, train_test_proportion: float) -> Tuple[Environment, Environment]:
        """For now uses all data for training and testing."""

        return environment, environment
