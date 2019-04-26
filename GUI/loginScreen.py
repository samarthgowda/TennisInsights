from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json

def loginMousePressed(event, data):
    for button in data.loginButtons:
        cx, cy, rw, ry = data.loginButtons[button]
        if event.x in range(cx-rw, cx+rw) and event.y in range(cy-ry, cy+ry):
            if button == "Sign in with Google+":
                runGoogleAuthentication(data)
                data.mode = "home"


def loginKeyPressed(event, data):
    if event.keysym == "l":
        runGoogleAuthentication(data)

def loginRedrawAll(canvas, data):
    canvas.create_image(0, 0, anchor = "nw", image = data.homeScreenBackground)
    for button in data.loginButtons:
        cx, cy, rw, ry = data.loginButtons[button]
        canvas.create_rectangle(cx - rw, cy - ry, cx + rw, cy + ry,
                                outline="white", width=0, fill= data.accentColor, activefill=data.accentColor2)
        canvas.create_text(cx + 25, cy, text=button, anchor="center", font=data.h3, fill="white")
        canvas.create_image(cx-rw + 10, cy-ry, anchor = "nw", image = data.googlePlusImg)

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/userinfo.email'

# using google plus api for authentication https://developers.google.com/+/web/api/rest/latest/
def runGoogleAuthentication(data):
    """Shows basic usage of the Admin SDK Directory API.
    Prints the emails and names of the first 10 users in the domain.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('plus', 'v1', http=creds.authorize(Http()))
    result = service.people().get(userId="me").execute()
    data.name = result['displayName']
    data.id = result['id']
    data.imgUrl = result['image']['url']
    data.email = result['emails'][0]['value']
    data.playerInfoDict = {'displayName': data.name, 'email': data.email, 'id': data.id, 'imgUrl': data.imgUrl}
    try:
        data.playerInfoDict = readFile("users/"+data.email+".json")
        data.name = data.playerInfoDict['displayName']
        data.id = data.playerInfoDict['id']
        data.imgUrl = data.playerInfoDict['image']['url']
        data.email = data.playerInfoDict['emails'][0]['value']
        print(data.playerInfoDict)
        print(type(data.playerInfoDict))
    except:
        writeFile("users/"+data.email+".json", data.playerInfoDict)


# based off of read and write scripts from 15112 Course Notes -- uses json files
def readFile(path):
    with open(path) as f:
        d = json.load(f)
        return d

def writeFile(path, contents):
    with open(path, "w") as f:
        jsonData = json.dump(contents, f)
        return jsonData

