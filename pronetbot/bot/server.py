from flask import Flask, request ,render_template,jsonify
from config import VERIFY_TOKEN
from bot import bot



app = Flask(__name__)
bot_ = bot
bot_.Constants()

@app.route("/", methods=["GET","POST"])
def receive_message():
    
    if request.method == "GET":
        token_sent = request.args.get("hub.verify_token")
        return verify_token(token_sent)
        
    else:
        data_json = request.get_json()
        data = message(data_json)
        save_sender_id(data["id"])
        try:
            bot_.send_manage(data)
        except:
            print ('ERROR')
        
    return 'DONE'


def verify_token(token):
	if token == VERIFY_TOKEN:
		return request.args.get("hub.challenge")
	return 'Verification token is invalid'


def message(message):
    for i in message['entry']:
        id =  (i['messaging'][0]['sender']['id'])        
        if 'postback' in i['messaging'][0].keys():
            text = i['messaging'][0]['postback']['title']
            payload = i['messaging'][0]['postback']['payload']
            type_ = 'postback'
            return {'id':id,'text':text,'type':type_,'payload':payload}

        else:    
            try:
                if 'quick_reply' in i['messaging'][0]['message'].keys():
                    text =  (i['messaging'][0]['message']['text'])
                    payload = i['messaging'][0]['message']['quick_reply']['payload']
                    type_ = 'quick_reply'
                    return {'id':id,'text':text,'type':type_,'payload':payload}
                else:
                    text =  (i['messaging'][0]['message']['text'])
                    type_ = 'text'
                    return {'id':id,'text':text,'type':type_}
            except:
                return 'UNKOWN MESSAGE TYPE'
 
def save_sender_id(id):
     with open(r"bot\users_id.text","a") as file:
         with open (r"bot\users_id.text","r") as _file_:
             get_ids = _file_.read()
             if not (id in get_ids):
                 file.write(f"{id}\n")

if __name__=='__main__':
    app.run()


