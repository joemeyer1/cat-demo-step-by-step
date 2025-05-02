

from src.animals.cat import Cat
from src.environments.jump_rope import JumpRope
from src.utils.environment_data import EnvironmentData


def teach_cat_to_jump_rope(cat: Cat, jump_rope: JumpRope) -> Cat:

    jump_rope_data = EnvironmentData(environment=jump_rope, train_test_proportion=0.8)  # use 80% of data for training, 20% for testing
    cat.train(jump_rope_data.train_environment)
    cat.test(jump_rope_data.test_environment)
    return cat
