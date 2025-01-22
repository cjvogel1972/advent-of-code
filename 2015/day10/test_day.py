import unittest

import day


class Test(unittest.TestCase):

    def test_look_and_say(self):
        numbers_results = {
            "1": "11",
            "11": "21",
            "21": "1211",
            "1211": "111221",
            "111221": "312211"
        }

        for number in numbers_results:
            self.assertEqual(numbers_results[number], day.look_and_say(number))
