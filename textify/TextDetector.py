from __future__ import print_function
from google.cloud import vision

def getText(image_uri):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_uri

    response = client.text_detection(image=image)

    # for text in response.text_annotations:
        # print('=' * 30)
        # print(text.description + " ", end = '')
        # vertices = ['(%s,%s)' % (v.x, v.y) for v in text.bounding_poly.vertices]
        # print('bounds:', ",".join(vertices))
    
    return response.text_annotations

getText('https://image.zmenu.com/menupic/4612715/072d7a11-2c4d-4d2d-bd6b-7b32b10d9721.jpg')
