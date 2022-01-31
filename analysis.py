import json

# Opening JSON file
f = open('res.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

label_counter = {}

for d in data:
    for l in d['labels']:
        print(l['name'])
        if l['name'] not in label_counter:
            label_counter[l['name']] = 1
        else:
            label_counter[l['name']] = label_counter[l['name']] + 1

print('label_counter', label_counter)
