import json,paralleldots,csv

#file name from facebook downloaded files
filename = "your_posts.json"

#loading the files of json component
with open(filename,'r') as j:
	data = json.load(j)
	
#extracting the post data from the raw data ibtained
a = []
for i in data.get('status_updates'):
	if i.get('data') is not None:
		a.append(i.get('data'))
b = []
for i in a:
	b.append(i[0].get('post'))

#authorising api key
paralleldots.set_api_key("<apikey>")

di = {}
new = {}

#list of all the methods
li = [paralleldots.sentiment,paralleldots.emotion, paralleldots.abuse,paralleldots.ner,paralleldots.keywords,paralleldots.taxonomy,paralleldots.phrase_extractor]
for j in li:
#evaluating each functional apis
	for i in b[0:51]:#evaluating for list of first 50 values
		di = j(i)
		new[i] = di
	for i in new:
		#writing the values in csv files
		with open('{}.csv'.format(("{}".format(j)).split(" ")[1][4:]), 'a') as csvfile:
			writer = csv.writer(csvfile, delimiter = ',')
			writer.writerow([i,new.get(i)])
