import httplib, urllib, base64, sys, json, cv2, time

path = "C:\\Users\\HP\\Desktop\\try\\"

def get_emo(file):
    r = open("C:\\Users\\HP\\Desktop\\try\\"+ file, 'rb')
    body1 = r.read()
    r.close()
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': 'c87f38940bdc4811b4ea44fa16dcc6d8',
    }

    params = urllib.urlencode({
    })

    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body1, headers)
    response = conn.getresponse()
    data = json.loads(response.read())
    return data
    conn.close()

 
# Captures a single image from the camera and returns it in PIL format
def get_image(file):
    camera = cv2.VideoCapture(0)
    time.sleep(1)
    retval, im = camera.read()
    cv2.imwrite(file, im)
    del(camera)
    return 

get_image('temp.jpg')

t = get_emo('temp.jpg')
print t
print "\n"
input()
