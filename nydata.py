

import requests

nydata_app_token = 'QXXAcUts45qgPHyLsdabAwyB4'

def sortit(a):
	return a["test_date"]

#d = requests.get('https://api.covidtracking.com/v1/us/daily.json').json()
d = requests.get('https://health.data.ny.gov/resource/xdss-u53e.json?$limit=20000'.format(nydata_app_token),headers={"X-App-Token": nydata_app_token, "limit": "5000"}).json()

e = [x for x in d if x["county"] == "Westchester"]

e.sort(key=sortit)
xval = []
yval = []
for i,x in enumerate(e):
	xval.append(i)
	yval.append(x["total_number_of_tests"])

print (yval)
