import unittest
from eventPackage import eventCounter


class TestEvent(unittest.TestCase):

    def test_meat(self):
        eventCounter.event(16, 2, 2, 3, 8)
        result = eventCounter.return_meat()
        self.assertEqual(result, 5.4)

    def test_return_candys(self):
        eventCounter.event(16, 2, 2, 3, 8)
        result = eventCounter.return_candys()
        self.assertEqual(result, 125)

    def test_return_all(self):
        eventCounter.event(16, 2, 2, 3, 8)
        self.assertEqual(eventCounter.return_all(), (5.4, 7.4, 3.5, 125, 4.0))


if __name__ == '__main__':
    unittest.main()
