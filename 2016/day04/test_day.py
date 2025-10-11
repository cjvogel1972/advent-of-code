import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "aaaaa-bbb-z-y-x-123[abxyz]",
            "a-b-c-d-e-f-g-h-987[abcde]",
            "not-a-real-room-404[oarel]",
            "totally-real-room-200[decoy]"
        ]

        self.assertEqual(1514, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "",
        ]

        self.assertEqual(0, day.solve_part2(lines))

    def test_is_real_room(self):
        self.assertEqual(day.is_real_room("aaaaa-bbb-z-y-x", "abxyz"), True)
        self.assertEqual(day.is_real_room("a-b-c-d-e-f-g-h", "abcde"), True)
        self.assertEqual(day.is_real_room("not-a-real-room", "oarel"), True)
        self.assertEqual(day.is_real_room("totally-real-room", "decoy"), False)

    def test_decrypt_name(self):
        self.assertEqual(day.decrypt_name("qzmt-zixmtkozy-ivhz", 343), "very encrypted name")
