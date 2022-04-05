import json
from textwrap import indent
from exception.ExceptionHandler import JsonNotFound, JsonNotCorrect


class JsonManipulation:

    def __init__(self, json_path):
        self.json_path = json_path

    def createMindMap(self, json_data):
        with open(self.json_path, "w") as json_file:
            if json_data['id']:
                dictionnary = {json_data['id']: {}}
                json_file.write(json.dumps(dictionnary))
            else:
                raise JsonNotFound

    def addLeaf(self, json_data):
        with open(self.json_path, "r", encoding='utf-8') as json_file:
            if all(x in json_data for x in ["text", "path"]):
                data = dict(json.load(json_file))
                data['my-map'][json_data['path']] = json_data['text']
                print(data)
            else:
                raise JsonNotCorrect

        with open(self.json_path, "w") as json_file:
            print(data)
            return json.dump(data, json_file)

    def readLeaf(self):
        with open(self.json_path, "r", encoding='utf-8') as json_file:
            data = json.load(json_file)
            return json.dumps(dict(data['my-map']))

    def prettyLeaf(self):
        with open(self.json_path, "r", encoding='utf-8') as json_file:
            data = dict(json.load(json_file))
            list_path = list(data['my-map'].keys())
            list_path_combined = json.dumps(list_path, indent=4)
            return list_path_combined
