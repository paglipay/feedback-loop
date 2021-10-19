<<<<<<< HEAD
print('app.py HERE!!!')
=======
import DTree
import json
import uuid



def do_process(flask_data, json_file, import_obj_instance):
    if '.json' in json_file:
        c = DTree.DTree(json.load(open(json_file)), name=json_file, import_obj_instance=import_obj_instance, data=flask_data)
    else:        
        c = DTree.DTree(json_file, name=uuid.uuid1(), import_obj_instance=import_obj_instance, data=flask_data)

if __name__ == "__main__":
    print('app.py HERE')
    flask_process_data = {}
    flask_process = {}
    import_obj_instance_hash = {}
    json_file = 'start.json'

    do_process(flask_process_data, json_file, import_obj_instance_hash)
>>>>>>> 0b1b5da4893b6c5d14c57c770689199dbeb90453
