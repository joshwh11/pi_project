import json
import requests

# Configure url
url = "https://api.github.com/repos/<your username>/<your repo>/contents/syntheticHealth.txt"

r = requests.get(url).text
rText = json.loads(r)
filesha = str(rText["sha"])
print(filesha)
