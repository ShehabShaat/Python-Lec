# created by : shehab shaat 1/10/2022
# ========================================assignment 1=============================================================
import unittest


class TestCase(unittest.TestCase):

    def test_1(self):
        self.assertTrue(10 in [5, 7, 8, 10], "Should Be True")

    def test_2(self):
        # self.assertEqual(type(10) == int, "Should Be True")
        self.assertIs(type(10), int, "Should Be True")

    def test_3(self):
        self.assertTrue(100, "Should Be True")

    def test_4(self):
        self.assertFalse([], "Should Be False")

    def test_5(self):
        self.assertGreaterEqual(100, 90, "Should Be True")


if __name__ == "__main__":
    unittest.main()

print("="*50)
# ========================================assignment 2=============================================================

import string, random

myList = []


def Generate_serial(count):
    all_char = string.ascii_letters + string.digits

    for _ in range(count):
        myList.append(all_char[random.randint(0, len(all_char) - 1)])
        if _ == 4 or _ == 9:
            myList.insert(_, "-")

    return "".join(myList)


print(Generate_serial(14))
