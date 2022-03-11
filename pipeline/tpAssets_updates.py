import sys
import requests
import os

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

sha = ""
repo_url = ""
if len(sys.argv) >= 2:
    sha = sys.argv[2]
    repo_url = sys.argv[1]
    url = r"%s/commits/%s" %(repo_url, sha)
    author = ""
    touchedFiles = []
    receive = requests.get(url)
    if receive.status_code == 200:
    ret = receive.json()
    if "author" in ret.keys() and "login" in ret["author"]:
      author = ret["author"]["login"]
    if "files" in ret.keys():
      for f in ret["files"]:
        if "filename" in f: touchedFiles.append(f["filename"])
    
    print("\n\n%s modified files [\n%s\n]" %(author, ',\n'.join(touchedFiles)))
    
  else:
    print("url: '%s' error in request." %url)
else:
    print("necessary args not included.")