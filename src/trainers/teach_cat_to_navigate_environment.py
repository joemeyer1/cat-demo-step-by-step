

from src.animals.cat import Cat
from src.environments.environment import Environment
from src.utils.environment_data import EnvironmentData


def teach_cat_to_navigate_environment(cat: Cat, environment: Environment) -> Cat:

	environment_data = EnvironmentData(environment=environment, train_test_proportion=0.8)  # use 80% of data for training, 20% for testing
	cat.train(environment_data.train_environment)
	cat.test(environment_data.test_environment)
	return cat
