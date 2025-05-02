
from src.animals.cat import Cat
from src.environments.jump_rope import JumpRope
from src.environments.water_body import WaterBody
from src.trainers.teach_cat_to_swim import teach_cat_to_swim
from src.trainers.teach_cat_to_jump_rope import teach_cat_to_jump_rope


def birth_a_skilled_cat() -> Cat:
    """Creates a cat and teaches it to do stuff."""

    cat = Cat()
    body_of_water = WaterBody()
    jump_rope = JumpRope()

    cat = teach_cat_to_swim(cat=cat, body_of_water=body_of_water)
    cat = teach_cat_to_jump_rope(cat=cat, jump_rope=jump_rope)

    cat.test(body_of_water)
    cat.test(jump_rope)
    return cat


if __name__ == '__main__':
    birth_a_skilled_cat()
