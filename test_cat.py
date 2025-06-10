

import unittest

from src.animals.cat import Cat
from src.environments.water_body import WaterBody
from src.trainers.teach_cat_to_swim import teach_cat_to_swim


class TestCat(unittest.TestCase):
    def test_birth_cat(self):
        cat = Cat()
        self.assertIsNotNone(cat)
        self.assertEqual(cat.lower_bound_behavior_range, 0)

    def test_create_environment(self):
        water_body = WaterBody()
        self.assertEqual(water_body.density, WaterBody.density)

    def test_environment(self):
        water_body = WaterBody()
        bad_behavior = water_body.low_point - 0.1
        good_behavior = water_body.low_point
        self.assertFalse(water_body.is_ok(bad_behavior))
        self.assertTrue(water_body.is_ok(good_behavior))

    def test_cat_behave(self):
        water_body = WaterBody()
        cat = Cat()
        cat.lower_bound_behavior_range = water_body.low_point - water_body.density
        cat.upper_bound_behavior_range = water_body.high_point - water_body.density
        behavior = cat.generate_random_restricted_behavior(water_body)
        self.assertGreaterEqual(behavior, water_body.low_point)
        self.assertLessEqual(behavior, water_body.high_point)

    def test_cat_misbehave(self):
        water_body = WaterBody()
        cat = Cat()
        cat.lower_bound_behavior_range = water_body.low_point - (water_body.density + 0.5)
        cat.upper_bound_behavior_range = water_body.low_point - (water_body.density + 0.5)
        behavior = cat.generate_random_restricted_behavior(water_body)
        self.assertLess(behavior, water_body.low_point)
        self.assertFalse(water_body.is_ok(behavior))

    def test_cat_train(self):
        cat = Cat()
        water_body = WaterBody()
        cat = teach_cat_to_swim(cat=cat, body_of_water=water_body)
        behavior = cat.generate_random_restricted_behavior(water_body)
        self.assertTrue(water_body.is_ok(behavior))


if __name__ == '__main__':
    unittest.main()
