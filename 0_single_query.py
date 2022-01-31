
from __future__ import print_function
from google.cloud import vision
import time
import json

image_uri = 'https://3m4r5618el913vtfz3jffby9-wpengine.netdna-ssl.com/wp-content/uploads/Landmarks-in-China-CCTV-735x490.jpg'

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

res.append(queryAPI(image_uri))

print(json.dumps(res, indent=4))

# save the results to res.json
with open("res.json", "w") as result_file:
    json.dump(res, result_file, indent=4, sort_keys=True)
    print('saving complete!!!')




