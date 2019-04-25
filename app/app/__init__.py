import requests
import re, random
from flask import Flask, request
from SparkFunctions import *
from config import *



def fetch(message):
     resp = requests.get(message)


def lights_on():
    url = "philips_api_url"
    resp = requests.post(url)
    if resp.status_code == 200:
        return "Lights are ON"
    else:
        return "Failed to turn lights ON"


app = Flask(__name__)
@app.route("/isok")
def isok():
    return "Flask is OK"

@app.route("/webhook", methods=['POST'])
def webhooks():
    js_data = request.json['data']
    actor_id = request.json['actorId']
    creator_id = request.json['createdBy']

    message_id = js_data['id']
    person_id = js_data['personId']
    person_mail = js_data['personEmail']
    room_id = js_data['roomId']

    if actor_id == creator_id:
        return "Ignoring BOT MSG"

    message = get_message(message_id, bearer)

    if 'fetch' in message:
        message = message.split(' ')[1]
        img = fetch(message)
        post_message_markdown(message, room_id, bearer)#post_file=img
        #return "IMG OK"

    post_message_markdown("Your message is %s" % (message), room_id, bearer)

    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
