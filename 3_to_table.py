import json

def score_of_label(name,labels):
    for l in labels:
        if name == l['name']:
            return l['score']
    return 0




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

# columns in the table
table_str = "uri,"

for key in label_counter:
    table_str += f"{key},"
for key in landmark_counter:
    table_str += f"{key},"

table_str += "\n"
print('1st row', table_str)

for d in data:
    new_row = f"{d['uri']},"

    for key in label_counter:
        new_row += f"{+score_of_label(key,d['labels'])},"
    for key in landmark_counter:

        if d['landmark'] and d['landmark']['name'] == key:
            new_row += f"{+d['landmark']['score']},"
        else:
            new_row += "0,"
    
    new_row += "\n"
    table_str += new_row
    
print('table_str', table_str)

with open('table.csv', 'w') as f:
    f.write(table_str)
    print('saving complete!!!')






