import twitter
import requests
import json
import os

from flask import Flask
from requests_oauthlib import OAuth1
from flask import jsonify


from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = twitter.Api(os.environ['CONSUMER_KEY'],os.environ['CONSUMER_SECRET'],os.environ['ACCESS_TOKEN_KEY'],os.environ['ACCESS_TOKEN_SECRET'])

@app.route("/")
def Home():
    r = api.GetHomeTimeline()
    return jsonify(r)

@app.route("/user-timeline/<username>")
def UserTimeline(username):
    r = api.GetUserTimeline(username)
    return jsonify(r)

@app.route("/list-status/<list_id>")
def ListStatus(list_id):
    r = api.GetListStatuses(list_id)
    return jsonify(r)

@app.route("/get-lists")
def GetLists():
    r = api.GetLists()
    return jsonify(r)