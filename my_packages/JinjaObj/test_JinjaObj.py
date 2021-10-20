from my_packages.JinjaObj import JinjaObj
import unittest   # The test framework

class Test_JinjaObj(unittest.TestCase):
    def test_k_func(self):
        k = JinjaObj('test_k_func', {})
        self.assertEqual(k.k_func('True', '3'), True)

    def test_v_func(self):
        k = JinjaObj('test_v_func', {})
        self.assertEqual(k.v_func('hi'), True)
