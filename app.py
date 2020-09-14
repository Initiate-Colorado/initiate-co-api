from flask import Flask
from flask_restful import Resource, Api, reqparse
from sos_scraper import webScraper
from co_ga_scraper import coGaScraper


# initializes api
app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello():
    return "Welcome to Initiate Colorado!"
if __name__ == '__main__':
    app.run()

BALLOTS = webScraper()
DATES = coGaScraper()

parser = reqparse.RequestParser()

# This returns all our ballot information including, ballot number, title, representative and co, address
class BallotDetails(Resource):
  def get(self):
    return BALLOTS

class BallotDueDates(Resource):
  def get(self):
    return DATES


api.add_resource(BallotDetails, '/ballots/')
api.add_resource(BallotDueDates, '/ballots/duedates/')


if __name__ == '__main__':
    app.run(debug=True)


