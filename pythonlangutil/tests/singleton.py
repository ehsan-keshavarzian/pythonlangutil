
import unittest
from pythonlangutil.examples.singleton import SingletonTest


class Test(unittest.TestCase):

    def test_singleton(self):
        self.assertRaises(Exception, SingletonTest)
        hit1 = SingletonTest.get_instance()
        self.assertEqual(hit1.id, "1", "expected default id")
        hit2 = SingletonTest.get_instance()
        self.assertEqual(hit2.id, "1", "expected default id")
        hit1.set_id("2")
        self.assertEqual(hit1.id, "2", "expected new id")
        self.assertEqual(hit2.id, "2", "expected new id")
        hit3 = SingletonTest.get_instance()
        self.assertEqual(hit3.id, "2", "expected new id")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()