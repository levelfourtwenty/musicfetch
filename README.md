# musicfetch
A neofetch-like program that fetches info about the music you listen to and displays it in a neofetch-like output.


## Setup 
1. Edit `config.ini` to match your username in the username section.
2. Create a developer account on LastFM, this can be done at https://www.last.fm/api/account/create, edit `config.ini` to match the API key and secret you recieved there.
3.  Edit the displayinfo entry in the `config.ini` file to either *spotify*, *lastfm* or *both*, currently only LastFM is supported, Spotify support will be added later, so, you should only enter *lastfm*.
4.  Either move `config.ini` to a static location on your system and change the path of it on line 11 of `main.py` or ensure it is always in the same directory as main.py.
5.  Run the program, it should work.

## Todo
- [x] LastFM Support
- [ ] Spotify Support 
- [ ] Include album cover in output
- [ ] Make code more efficient
