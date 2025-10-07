import json
import requests
import datetime
import os

CLIENT_ID = "d676a99a6401e791249d4e7e0b52c4fa"

KAKAO_TOKEN_FILENAME = 'kakao_message/kakao_token.json'

# url = "https://kauth.kakao.com/oauth/token"
    
def save_tokens(filename, tokens):
    with open(filename, 'w')as fp:
        json.dump(tokens, fp)
        
def load_tokens(filename):
    with open(filename)as fp:
        tokens = json.load(fp)
    return tokens

def update_tokens(app_key, filename):
    tokens = load_tokens(filename)
    
    data = {
        "grant_type" : "authorization_code",
        "client_id" : CLIENT_ID,
        "refresh_token" : tokens['refresh_token']
    }
    
    reseponse = requests.post(url, data=data)
    
    if reseponse.status_code != 200:
        print("error", reseponse.json())
    else:
        token = reseponse.json()
        print("token", token)
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = filename + '.' + now
        os.rename(filename, backup_filename)
        
        token['access_token'] = reseponse.json()['access_token']
        
        save_tokens(filename, tokens)
        
    return tokens

def send_message(tokens, msg):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": "Bearer " + tokens['access_token']
    }
    data = {
        "template_object" : json.dumps(
            {"object_type" : "text",
             "text" : msg,
             "link" : { "web_url" : "www.naver.com"}
            })
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    if reseponse.status_code != 200:
        print("error", reseponse.json())
    else:
        print("success",)
    

# https://kauth.kakao.com/oauth/authorize?client_id=d676a99a6401e791249d4e7e0b52c4fa&response_type=code&redirect_uri=http://localhost.com

data = {
    "grant_type" : "authorization_code",
    "client_id" : CLIENT_ID,
    "redirect_url" : "http://localhost.com",
    "code" : "mUqIHClvl1X9F0MN4M19OgYhaw2Xd6nLnH4ru4yCENBtPUFoun-2JAAAAAQKDRlTAAABmbvcNK2SBpCp5rpDbg" 
}

reseponse = requests.post(url, data=data)

if reseponse.status_code != 200:
    print("error", reseponse.json())
    if (reseponse.json()['error_code'] == 'KOE320'):
        print(get_code(CLIENT_ID))
        
else:
    token = reseponse.json()
    print("token", token)
    
    save_tokens(KAKAO_TOKEN_FILENAME, token)
    send_message(token, "K2025029 금동환 파이썬매시업프로젝트")
        
    