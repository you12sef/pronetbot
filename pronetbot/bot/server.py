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
        try:
            bot_.send_manage(data)
        except:
            print ('ERROR')
        
    return 'DONE'


#@app.route("/privacy", methods=["GET"])
#def submit():   
#       return 'there is no privacy.'

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
    

if __name__=='__main__':
    app.run()


