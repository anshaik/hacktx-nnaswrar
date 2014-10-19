import requests

# returns google trends for query

query = 'ebola' #example
data = '3' # return data as json
graph = '5' # return related google graph

url = 'http://www.google.com/trends/fetchComponent?q='+query+',qwerty&cid=TIMESERIES_GRAPH_0&export='+data

#or graph
# url = 'http://www.google.com/trends/fetchComponent?q='+query+
		#',qwerty&cid=TIMESERIES_GRAPH_0&export='+graph

r = requests.get(url)

result = r.text # holds json data

#TODO: parse relevant data and dump to UI
