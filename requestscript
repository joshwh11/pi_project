import requests
import sys

# To use, in terminal type:
# python3 requestscript.py <Pin ID> <on or off>
# For example, to turn the red pin on, you would use the command:
# python3 requestscript.py 1 on

url = 'http://localhost:9999/pins/' + str(sys.argv[1])
payload = {'state': str(sys.argv[2])}

rpatch = requests.patch(url, json=payload)
