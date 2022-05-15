from django.test import TestCase

from api.usecases import return_coins


class TestReturnCoins(TestCase):

    def test_func(self):
        table = [
            {'input': (1.23, 1.23), 'expected_output': {}},
            {'input': (1.23, 2.24), 'expected_output': {1: 1.0, 0.01: 1.0}},
            {'input': (10, 20), 'expected_output': {10: 1.0}},
            {'input': (1.23, 5), 'expected_output': {2: 1.0, 1: 1.0, 0.5: 1.0, 0.2: 1.0, 0.05: 1.0, 0.02: 1.0}},
            {'input': (1.23, 500.0), 'expected_output': {100: 4.0, 50: 1.0, 20: 2.0, 5: 1.0, 2: 1.0, 1: 1.0, 0.5: 1.0, 0.2: 1.0, 0.05: 1.0, 0.02: 1.0}},
        ]
        for item in table:
            self.assertEqual(return_coins(*item['input']), item['expected_output'])
