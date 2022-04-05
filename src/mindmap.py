import logging
from genericpath import exists
from exception.ExceptionHandler import JsonNotFound
from tools.JsonManipulation import JsonManipulation
from flask import Flask, request
from werkzeug.exceptions import HTTPException


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
json_file_path = "./mind_map.json"


class MindMap:

    def __init__(self):
        pass

    @app.route("/create", methods=['POST'])
    def createMindMap():
        try:
            if request.is_json:
                content = request.get_json()
                json_manipulation = JsonManipulation(json_file_path)
                json_manipulation.createMindMap(content)
                return content

        except HTTPException as httpException:
            logging.error(httpException)
            raise HTTPException(httpException)

        except Exception as e:
            logging.error(e)
            raise Exception(e)

    @app.route("/add", methods=['POST'])
    def addLeaf():
        try:
            if request.is_json and exists(json_file_path):
                content = request.get_json(json_file_path)
                json_manipulation = JsonManipulation(json_file_path)
                json_manipulation.addLeaf(content)
                return content
            else:
                raise JsonNotFound

        except HTTPException as httpException:
            logging.error(httpException)
            raise HTTPException(httpException)

        except Exception as e:
            logging.error('Failed to add Leaf' + str(e))

    @app.route("/read", methods=['GET'])
    def readLeaf():
        try:
            if exists(json_file_path):
                json_manipulation = JsonManipulation(json_file_path)
                return json_manipulation.readLeaf()
            else:
                raise JsonNotFound

        except HTTPException as httpException:
            logging.error(httpException)
            raise HTTPException(httpException)

        except Exception as e:
            logging.error(e)
            raise Exception(e)

    @app.route("/pretty", methods=['GET'])        
    def printMM():
        try:
            if exists(json_file_path):
                json_manipulation = JsonManipulation(json_file_path)
                return json_manipulation.prettyLeaf()
            else:
                raise JsonNotFound

        except HTTPException as httpException:
            logging.error(httpException)
            raise HTTPException(httpException)

        except Exception as e:
            logging.error(e)
            raise Exception(e)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')