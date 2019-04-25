import requests, json
from config import *


def main():
    token = "Bearer " + bearer
    header = {"Authorization": "%s" % token, "content-type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    post_message_url = "https://api.ciscospark.com/v1/webhooks"
    payload = {
               "resource": "messages",
               "event": "created",
               #"filter": "mentionedPeople=me",
               "targetUrl": webhook_URL + '/webhook',
               "name": webhook_name
               }
    api_response = requests.post(post_message_url, json=payload, headers=header, verify=False)
    response_code = api_response.status_code
    print api_response.text

    return response_code

if __name__ == '__main__':
    print(main())
