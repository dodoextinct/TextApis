import json,paralleldots,csv

filename = "your_posts.json"
with open(filename,'r') as j:
	data = json.load(j)
a = []
for i in data.get('status_updates'):
	if i.get('data') is not None:
		a.append(i.get('data'))
b = []
for i in a:
	b.append(i[0].get('post'))

paralleldots.set_api_key("2eJksCHNsoqj7uZYHmEcgG9P3hiF7A9nHb4tmwvUmH8")

di = {}
new = {}
li = [paralleldots.sentiment,paralleldots.emotion, paralleldots.abuse,paralleldots.ner,paralleldots.keywords,paralleldots.taxonomy,paralleldots.phrase_extractor]
for j in li:
	for i in b[0:51]:
		di = j(i)
		new[i] = di
	for i in new:
		with open('{}.csv'.format(("{}".format(j)).split(" ")[1][4:]), 'a') as csvfile:
			writer = csv.writer(csvfile, delimiter = ',')
			writer.writerow([i,new.get(i)])
