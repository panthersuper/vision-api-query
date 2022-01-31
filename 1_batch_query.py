
from __future__ import print_function
from google.cloud import vision
import time
import json

def queryAPI(image_uri):
    result = {
        'uri':image_uri,
        'labels':[],
        'landmark':None
    }

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_uri

    response = client.label_detection(image=image)
    print('Labels (and confidence score):')
    print('-' * 30)
    for label in response.label_annotations:
        print(label.description, '(%.2f%%)' % (label.score*100.))
        result['labels'].append({
            'name': label.description,
            'score': label.score
        })

    time.sleep(1)

    response = client.landmark_detection(image=image)
    for landmark in response.landmark_annotations:
        print('=' * 30)
        print(landmark.description, '(%.2f%%)' % (landmark.score*100.))
        result['landmark'] = {
            'name': landmark.description,
            'score': landmark.score
        }

    print(result)
    time.sleep(1)
    return result


res = []

image_uris = [
    'http://pwz.mit.edu/img/bos_st/download%20(1).jpeg',
    'http://pwz.mit.edu/img/bos_st/download%20(2).jpeg',
    'http://pwz.mit.edu/img/bos_st/download%20(3).jpeg',
    'http://pwz.mit.edu/img/bos_st/download%20(4).jpeg',
    'http://pwz.mit.edu/img/bos_st/download%20(5).jpeg',
    'http://pwz.mit.edu/img/bos_st/download%20(6).jpeg',
    'http://pwz.mit.edu/img/bos_st/download%20(7).jpeg',
    'http://pwz.mit.edu/img/bos_st/download%20(8).jpeg',
    'http://pwz.mit.edu/img/bos_st/download%20(9).jpeg',
    'http://pwz.mit.edu/img/bos_st/download%20(10).jpeg',
]

for uri in image_uris:
    print('+' * 30)
    print("URI",uri)

    res.append(queryAPI(uri))

print(json.dumps(res, indent=4))

# save all the results to res.json
with open("res.json", "w") as result_file:
    json.dump(res, result_file, indent=4, sort_keys=True)
    print('saving complete!!!')




