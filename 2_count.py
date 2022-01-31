import json

# Opening JSON file
f = open('res.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

label_counter = {}
label_threshold = 0.5

landmark_counter = {}
landmark_threshold = 0.1

for d in data:
    for l in d['labels']:
        # print(l['name'])
        if l['score'] > label_threshold:
            if l['name'] not in label_counter:
                label_counter[l['name']] = 1
            else:
                label_counter[l['name']] = label_counter[l['name']] + 1
    
    if d['landmark']:
        # print("d['landmark']", d['landmark'])
        if d['landmark']['score'] > landmark_threshold:
            if d['landmark']['name'] not in landmark_counter:
                landmark_counter[d['landmark']['name']] = 1
            else:
                landmark_counter[d['landmark']['name']] = landmark_counter[d['landmark']['name']] + 1

print('label_counter', label_counter)
print('landmark_counter', landmark_counter)
