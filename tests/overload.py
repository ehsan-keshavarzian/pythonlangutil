
import unittest
from examples.overload import OverloadTest


class Test(unittest.TestCase):


    def test_overload(self):
        hit = OverloadTest()
        self.assertEqual(hit.my_method("Joe"), "Dear Joe", "msg")
        self.assertEqual(hit.my_method("Joe", True), "Mr. Joe", "msg")
        self.assertEqual(hit.my_method(1, "Joe"), "Dear Joe", "msg")
        self.assertRaises(Exception, hit.my_method)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()