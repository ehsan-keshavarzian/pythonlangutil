
import unittest
from pythonlangutil.examples.access_modifiers import PrivateVariableTest, PrivateFunctionTest,\
    PrivateConstructorTest


class Test(unittest.TestCase):

    def test_private_variable(self):
        hit = PrivateVariableTest()
        self.assertEqual(hit.id, "123", "expected default id")
        def set_id():
            hit.id = 5
        self.assertRaises(Exception, set_id)
        hit.insider()
        self.assertEqual(hit.id, "321", "expected new id")
        
    def test_private_method(self):
        hit = PrivateFunctionTest()
        self.assertRaises(Exception, hit.private_method)
        self.assertEqual(hit.insider(), 'called from inside my own class', "expected allowed access")
        
    def test_private_contructor(self):
        self.assertRaises(Exception, PrivateConstructorTest)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()