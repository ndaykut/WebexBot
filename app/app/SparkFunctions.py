import requests, json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def post_message_markdown(message_text, room_id, token):# post_file=''
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        headers = {'Authorization': 'Bearer ' + token,
                   'Content-Type': 'application/json'}

        body = json.dumps({'roomId': room_id, 'markdown': message_text})
        #if post_file:
        #    body = json.dumps({'roomId': room_id, 'markdown': message_text,
        #                       'files': post_file})


        resp = requests.post('https://api.ciscospark.com/v1/messages',
                             verify=False, headers=headers, data=body)

        return resp


def get_message(message_id, token):

    header = {"Authorization": "Bearer " + token}
    get_rooms_url = "https://api.ciscospark.com/v1/messages/" + message_id
    api_response = requests.get(get_rooms_url, headers=header, verify=False)
    response_json = api_response.json()
    text = response_json["text"]

    return text
