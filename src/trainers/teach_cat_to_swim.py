

from src.animals.cat import Cat
from src.environments.water_body import WaterBody
from src.trainers.teach_cat_to_navigate_environment import teach_cat_to_navigate_environment


def teach_cat_to_swim(cat: Cat, body_of_water: WaterBody) -> Cat:
    return teach_cat_to_navigate_environment(cat=cat, environment=body_of_water)
