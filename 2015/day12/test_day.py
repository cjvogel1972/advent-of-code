import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        docs = {
            '{"a":2,"b":4}': 6,
            '[1,2,3]': 6,
            '[[[3]]]': 3,
            '{"a":{"b":4},"c":-1}': 3,
            '{"a":[-1,1]}': 0,
            '{"a":[-1,{"a":1}]}': 0,
            '{}': 0,
            '[]': 0
        }

        for doc in docs:
            lines = [doc]

            self.assertEqual(docs[doc], day.solve_part1(lines), doc)

    def test_solve_part2(self):
        docs = {
            '[1,2,3]': 6,
            '[1,{"c":"red","b":2},3]': 4,
            '{"d":"red","e":[1,2,3,4],"f":5}': 0,
            '[1,"red",5]': 6,
        }

        for doc in docs:
            lines = [doc]

            self.assertEqual(docs[doc], day.solve_part2(lines), doc)
