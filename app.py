from flask import Flask
from flask_restful import Resource, Api, reqparse
from sos_scraper import webScraper


# initializes api
app = Flask(__name__)
api = Api(app)

BALLOTS = webScraper()

parser = reqparse.RequestParser()

# This returns all our ballot information including, ballot number, title, representative and co, address
class BallotDetails(Resource):
  def get(self):
    return BALLOTS


api.add_resource(BallotDetails, '/ballots/')


if __name__ == '__main__':
    app.run(debug=True)


