import requests
import pathlib
import os
import errno
import urllib

page = 'https://www.vgmusic.com/music/other/miscellaneous/piano/'
dl = []
source = requests.get(page).text
part = source.split(".mid")
print(len(part), " "*(4-len(str(len(part)))))
counter = 1

for p in part[:len(part)-1]:
	dl.append(page + (p + ".mid").split("<a href=\"")[-1])
	# print("-- ", new)
	print("|", end="")
	if counter % 100 == 0:
		print("\n")
	counter += 1
    
print("\n")

path = pathlib.Path(".") / "piano_midi"

try:
	os.makedirs(path)
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
        
counter = 0
print("downloading files")

for file in dl:
	counter += 1
	urllib.request.urlretrieve(file, path / file.split("/")[-1])
	print("|", end="")
	if counter % 100 == 0:
		print("\n")
    
print(counter, "songs downloaded")