import configparser
#import spotipy
import pylast


config = configparser.ConfigParser()
config.sections()


def readconfig():
	config.read('config.ini')
	global confinfo
	class confinfo:		
		apikey = config['login']['apikey']
		secret = config['login']['secret']
		displayinfo = config['default']['displayinfo']
		fetchcover = config['default']['fetchcover']
		username = config['login']['user']

def initlastfm():
	global network
	network = pylast.LastFMNetwork(
		api_key=confinfo.apikey,
		api_secret=confinfo.secret,
	)

def lastfm():
	user = network.get_user(confinfo.username)
	track = user.get_recent_tracks(limit=1)[0]
	# this is probably super inefficient but I'm a lazy bastard
	nowplaying = user.get_now_playing()
	topartist = user.get_top_artists(limit=3, period='PERIOD_3MONTHS')
	topartist1 = topartist[0]
	topartist2 = topartist[1]
	topartist3 = topartist[2]
	toptracks = user.get_top_tracks(limit=3, period='PERIOD_3MONTHS')
	toptrack1 = toptracks[0]
	toptrack2 = toptracks[1]
	toptrack3 = toptracks[2]
	url = user.get_url()

	if(nowplaying == None):
		print(f"\nLastFM Username: {confinfo.username}")
		print(f"Last Played:\n {track.track}")
		print(f"Favourite artists:\n {topartist1.item.get_name()} ")
		print(f" {topartist2.item.get_name()}\n {topartist3.item.get_name()}")
		print(f"Favourite songs:")
		print(f" {toptrack1.item.get_name()} - {toptrack1.item.get_artist()}\n {toptrack2.item.get_name()} - {toptrack2.item.get_artist()}\n {toptrack3.item.get_name()} - {toptrack3.item.get_artist()}")
		print(f"Profile URL:\n {user.get_url()}")
	else:
		print(f"\nLastFM Username: {confinfo.username}")
		print(f"Now Playing:\n {nowplaying}")
		print(f"Favourite artists:\n {topartist1.item.get_name()} ")
		print(f" {topartist2.item.get_name()}\n {topartist3.item.get_name()}")
		print(f"Favourite songs:")
		print(f" {toptrack1.item.get_name()} - {toptrack1.item.get_artist()}\n {toptrack2.item.get_name()} - {toptrack2.item.get_artist()}\n {toptrack3.item.get_name()} - {toptrack3.item.get_artist()}")
		print(f"Profile URL:\n {user.get_url()}")	
def main():
	readconfig()
	initlastfm()
	if(confinfo.fetchcover == "lastfm"):
		lastfm()
	# This part of the program is still under development
	#
	# if(confinfo.fetchcover == "spotify"):
	# 	exit()

if __name__ == "__main__":
	main()
