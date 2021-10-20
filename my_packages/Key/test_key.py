from my_packages.Key import Key
from DTree import DTree
import json
import unittest   # The test framework

class Test_Key(unittest.TestCase):
    def test_k_func(self):
        k = Key('test_k_func', {})
        self.assertEqual(k.k_func('True', '3'), True)

    def test_v_func(self):
        k = Key('test_v_func', {})
        self.assertEqual(k.v_func('hi'), True)

    def test_Dtree(self):
        print('app.py HERE')
        flask_data = {}
        flask_process = {}
        import_obj_instance = {}
        json_file = 'my_packages/Key/tests/json/start.json'
        d = DTree(json.load(open(json_file)), name=json_file, import_obj_instance=import_obj_instance, data=flask_data)
        # print('d.data:', d.data)
        self.assertEqual(d.data, {'Key': ['Hi Key']})

