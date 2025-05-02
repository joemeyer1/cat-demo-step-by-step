

from src.animals.cat import Cat
from src.environments.jump_rope import JumpRope
from src.trainers.teach_cat_to_navigate_environment import teach_cat_to_navigate_environment


def teach_cat_to_jump_rope(cat: Cat, jump_rope: JumpRope) -> Cat:
    return teach_cat_to_navigate_environment(cat=cat, environment=jump_rope)
