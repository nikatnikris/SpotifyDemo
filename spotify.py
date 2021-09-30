# stub module pretending to be doing spotify things.  Track changes every 6 seconds

from datetime import datetime, timedelta

rawData = [
	{"track":{"number":"1", "name":"Crazy", "artist":"Gnarls Barkley", "up":0, "down":0}},
	{"track":{"number":"2", "name":"Maneater", "artist":"Nelly Furtado", "up":0, "down":0}},
	{"track":{"number":"3", "name":"From Paris To Berlin", "artist":"Infernal", "up":0, "down":0}},
	{"track":{"number":"4", "name":"Voodoo Child", "artist":"Rogue Traders", "up":0, "down":0}},
	{"track":{"number":"5", "name":"Don't Stop Me Now", "artist":"McFly", "up":0, "down":0}},
	{"track":{"number":"6", "name":"Who Knew", "artist":"Pink", "up":0, "down":0}},
	{"track":{"number":"7", "name":"I Wish I Was A Punk Rocker (With Flowers in My Hair)", "artist":"Sandi Thom", "up":0, "down":0}},
	{"track":{"number":"8", "name":"She Moves In Her Own Way", "artist":"The Kooks", "up":0, "down":0}},
	{"track":{"number":"9", "name":"Fill My Little World", "artist":"The Feeling", "up":0, "down":0}},
	{"track":{"number":"10", "name":"Is It Any Wonder?", "artist":"Keane", "up":0, "down":0}},
	{"track":{"number":"11", "name":"You're All I Have", "artist":"Snow Patrol", "up":0, "down":0}},
	{"track":{"number":"12", "name":"In The Morning", "artist":"Razorlight", "up":0, "down":0}},
	{"track":{"number":"13", "name":"Bright Idea", "artist":"Orson", "up":0, "down":0}},
	{"track":{"number":"14", "name":"Valerie", "artist":"The Zutons", "up":0, "down":0}},
	{"track":{"number":"15", "name":"Bang Bang You're Dead", "artist":"Dirty Pretty Things", "up":0, "down":0}},
	{"track":{"number":"16", "name":"Monster", "artist":"The Automatic", "up":0, "down":0}},
	{"track":{"number":"17", "name":"Faster Kill Pussycat", "artist":"Oakenfold", "up":0, "down":0}},
	{"track":{"number":"18", "name":"Stoned In Love", "artist":"Chicane", "up":0, "down":0}},
	{"track":{"number":"19", "name":"Country Girl", "artist":"Primal Scream", "up":0, "down":0}},
	{"track":{"number":"20", "name":"Who Says You Can't Go Home", "artist":"Bon Jovi", "up":0, "down":0}},
	{"track":{"number":"21", "name":"Up All Night", "artist":"Matt Willis", "up":0, "down":0}},
	{"track":{"number":"22", "name":"Dance, Dance", "artist":"Fall Out Boy", "up":0, "down":0}},
	{"track":{"number":"23", "name":"Smile", "artist":"Lily Allen", "up":0, "down":0}},
	{"track":{"number":"24", "name":"SOS", "artist":"Rihanna", "up":0, "down":0}},
	{"track":{"number":"25", "name":"Pump It", "artist":"Black Eyed Peas", "up":0, "down":0}},
	{"track":{"number":"26", "name":"Buttonz", "artist":"Pussycat Dolls", "up":0, "down":0}},
	{"track":{"number":"27", "name":"So Sick", "artist":"Ne-Yo", "up":0, "down":0}},
	{"track":{"number":"28", "name":"Touch It", "artist":"Busta Rhymes", "up":0, "down":0}},
	{"track":{"number":"29", "name":"Say I", "artist":"Christina Milian", "up":0, "down":0}},
	{"track":{"number":"30", "name":"Mas Que Nada", "artist":"Sergio Mendes", "up":0, "down":0}},
	{"track":{"number":"31", "name":"Nine2Five", "artist":"The Ordinary Boys", "up":0, "down":0}},
	{"track":{"number":"32", "name":"Red Dress", "artist":"Sugababes", "up":0, "down":0}},
	{"track":{"number":"33", "name":"Somebody's Watching Me", "artist":"Beatfreakz", "up":0, "down":0}},
	{"track":{"number":"34", "name":"First Time", "artist":"Sunblock", "up":0, "down":0}},
	{"track":{"number":"35", "name":"World, Hold On (Children of the Sky)", "artist":"Bob Sinclar", "up":0, "down":0}},
	{"track":{"number":"36", "name":"Tell Me Why", "artist":"Supermode", "up":0, "down":0}},
	{"track":{"number":"37", "name":"Horny As A Dandy", "artist":"Mousse T.", "up":0, "down":0}},
	{"track":{"number":"38", "name":"Sensitivity", "artist":"The Shapeshifters", "up":0, "down":0}},
	{"track":{"number":"39", "name":"Piece of My Heart", "artist":"Beverley Knight", "up":0, "down":0}},
	{"track":{"number":"40", "name":"You Give Me Something", "artist":"James Morrison", "up":0, "down":0}},
	{"track":{"number":"41", "name":"Who Am I", "artist":"Will Young", "up":0, "down":0}},
	{"track":{"number":"42", "name":"All Over Again", "artist":"Ronan Keating", "up":0, "down":0}},
	{"track":{"number":"43", "name":"Whole Lotta History", "artist":"Girls Aloud", "up":0, "down":0}},
]

#initial values
currentTrackNumber = 1
currentTrack = rawData[currentTrackNumber-1]
nextTrackAt = datetime.now() + timedelta(seconds=10)


# returns a document with stuff in it
def getCurrentTrack():
	global rawData, currentTrack, nextTrackAt, currentTrackNumber
	if datetime.now() > nextTrackAt:
		currentTrackNumber += 1
		if currentTrackNumber >= 44:
			currentTrackNumber=1
		currentTrack = rawData[currentTrackNumber-1]
		currentTrack["track"]["up"] = 0
		currentTrack["track"]["down"] = 0
		nextTrackAt = datetime.now() + timedelta(seconds=10)
		currentTrack["track"]["until"] = nextTrackAt.strftime("%H:%M:%S")
	return currentTrack

def upvote():
	currentTrack["track"]["up"] += 1
	if currentTrack["track"]["up"] - currentTrack["track"]["down"] < -1:
		nextTrack()

def downvote():
	currentTrack["track"]["down"] += 1
	if currentTrack["track"]["up"] - currentTrack["track"]["down"] < -1:
		nextTrack()

def nextTrack():
	global rawData, currentTrack, nextTrackAt
	nextTrackAt = datetime.now()
	getCurrentTrack()
