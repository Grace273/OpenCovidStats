import json, requests

url = 'https://api.opencovid.ca/summary'
response = requests.get(url)
json_data = json.loads(response.text) # data turn into JSON object

with open ("opencovid.json", "w") as import_file:
    import_file.write(json.dumps(json_data))
    
# with open ("opencovid.json", "w") as import_file:
#     import_file.write(response.text) #when you code it response.text is json but when you print onto the file turns to ASCII letters and is string
    

print(json_data['data'][0]['date']) #accessing data