from werkzeug.exceptions import HTTPException


class BadRequest(HTTPException):
    pass


class JsonError(Exception):
    pass


class JsonNotFound(HTTPException):
    code = 400
    description = "Exception: MindMap does not exist, use /create"


class JsonNotCorrect(HTTPException):
    code = 400
    description = "Exception: Your json is not correct, check API docs"


class LeafNotExisting(HTTPException):
    code = 400
    description = "Exception: Create Leaf before using this method"


