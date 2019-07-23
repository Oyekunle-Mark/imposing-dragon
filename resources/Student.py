from flask import request
from flask_restful import Resource
from data import students


class StudentResource(Resource):
    """
    Manages the student data
    """

    def get(self):
        return {"status": 200, "data": students}

    def post(self):
        data = request.get_json()
        students.append(data)
        return {"status": 201, "data": data}, 201

    def put(self, id):
        data = request.get_json()
        students[id - 1] = data
        return {"status": 200, "data": data}

    def delete(self, id):
        del students[id - 1]
        return {"status": 200, "data": students}
