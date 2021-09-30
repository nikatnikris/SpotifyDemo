from app import app
from flask import render_template
import json
import spotify
#import time
#import sys
#from flask import abort

votes = {"up": 0, "down": 0}

@app.route('/', methods=['GET'])
def getUI():
	return render_template('index.html')

@app.route('/api/currenttrack', methods=['GET'])
def apiCurrenttrack():
	return json.dumps(spotify.getCurrentTrack())

@app.route('/api/upvote', methods=['POST'])
def apiUpvote():
	spotify.upvote()
	return json.dumps(True)

@app.route('/api/downvote', methods=['POST'])
def apiDownvote():
	spotify.downvote()
	return json.dumps(True)
	