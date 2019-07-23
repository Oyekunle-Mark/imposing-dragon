from flask import Flask
from flask_restful import Api
from resources.Student import StudentResource

app = Flask(__name__)
api = Api(app)

api.add_resource(StudentResource, '/', '/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
