from flask import Flask
from flask_restful import Resource, Api
import wikiRequests
#import Converter here

app = Flask(__name__)
api = Api(app)

articles = {}

class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}

class Quiz(Resource):
    article = None
    def put(self, topic, limit):
        if topic not in articles.keys():
            article = wikiRequests.createSectionsByCategory (topic, limit)
            articles[topic] = article
        return list(map(lambda x: x.serialize(), articles[topic]))
    def get(self, topic):

        #should return converted list of questions and leave it to ui
        return list(map(lambda x: x.serialize(), articles[topic]))

class Categories(Resource):
    def get(self):
        return wikiRequests.getRandomCategories()

api.add_resource(HelloWorld, '/')
api.add_resource(Quiz, '/trivia/<string:topic>/<int:limit>', '/trivia/<string:topic>')
api.add_resource(Categories, '/categories')

if __name__ == '__main__':
    app.run(debug=True)
