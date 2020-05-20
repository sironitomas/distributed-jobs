import unittest
from tasks import add


class TestTasks(unittest.TestCase):

    def test_add(self):
        res1 = add(4, 3)
        self.assertEqual(res1, 7)

        res2 = add(1.5, 6.2)
        self.assertAlmostEqual(res2, 7.7)

        res3 = add(-34, 20.9)
        self.assertAlmostEqual(res3, -13.1)
