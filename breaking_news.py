import requests

# returns top x amount of top stories
url = 'http://api.usatoday.com/open/breaking?expired=true&api_key=cahyrc6mkz4behdvc569vc9a'
r = requests.get(api_auth_link)

xml = r.text # holds XML data

#TODO: parse relevant data and dump to UI
