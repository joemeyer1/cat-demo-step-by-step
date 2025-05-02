

from src.animals.cat import Cat
from src.environments.water_body import WaterBody
from src.utils.environment_data import EnvironmentData


def teach_cat_to_swim(cat: Cat, body_of_water: WaterBody) -> Cat:

	water_body_data = EnvironmentData(environment=body_of_water, train_test_proportion=0.8)  # use 80% of data for training, 20% for testing
	cat.train(water_body_data.train_environment)
	cat.test(water_body_data.test_environment)
	return cat
