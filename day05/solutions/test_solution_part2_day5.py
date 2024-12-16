# Tests for Part 2

import unittest
from solution_part2 import order_updates


class TestOrderUpdates(unittest.TestCase):
    def setUp(self):
        self.order_rules = [
            (47, 53),
            (97, 13),
            (97, 61),
            (97, 47),
            (75, 29),
            (61, 13),
            (75, 53),
            (29, 13),
            (97, 29),
            (53, 29),
            (61, 53),
            (97, 53),
            (61, 29),
            (47, 13),
            (75, 47),
            (97, 75),
            (47, 61),
            (75, 61),
            (47, 29),
            (75, 13),
        ]
        self.updates = [
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47],
        ]

    def test_order_updates(self):
        ordered_invalid_updates = order_updates(
            self.updates,
            self.order_rules,
        )
        self.assertEqual(
            ordered_invalid_updates,
            [
                [97, 75, 47, 61, 53],
                [61, 29, 13],
                [97, 75, 47, 29, 13],
            ],
        )


if __name__ == "__main__":
    unittest.main()
